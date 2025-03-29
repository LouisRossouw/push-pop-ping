import os
import asyncio
import schedule
from time import sleep

import lib.utils as utils
import lib.expo_requests as ER
from lib.save_data import save_data
from lib.session import check_auth_tokens

root_dir = os.path.dirname(__file__)

main_config = utils.read_json(os.path.join(root_dir, "main.json"))
projects = utils.read_json(os.path.join(root_dir, "projects.json"))
notifications = utils.read_json(os.path.join(root_dir, "notifications.json"))

main_interval = main_config.get('interval_seconds', 20)


def run():
    # Set schedules for Fetch expo push tokens.
    set_schedules(fetch_expo_tokens, schedules=projects)

    # Set schedules for Send Notifications.
    for project in projects:

        project_name = project.get("name")
        notification_list = notifications.get(project_name)

        if notification_list:
            set_schedules(send_push_notification, notification_list)

    while True:
        schedule.run_pending()
        sleep(main_interval)


def set_schedules(function, schedules):
    """ Builds and Sets the shedules. """

    for schedule in schedules:
        if schedule.get('active'):
            build_schedules(
                function,
                schedule,
                schedule.get('interval', 1),
                schedule.get('interval_type', "days")
            )


def build_schedules(function, data, interval, interval_type):
    """ Sets a schedule based on interval and interval type. """

    if interval > 0:
        sch = schedule.every(interval)

        if interval_type == "days":
            sch.days.do(function, data)
        elif interval_type == "seconds":
            sch.seconds.do(function, data)
        else:
            print(f"Invalid - {data.get('name')}: {interval}")


def fetch_expo_tokens(data):
    """ Fetches expo tokens from endpoints, and saves them to a json file. """

    start_time = utils.start_time()
    success, result = ER.get_expo_push_tokens(data)
    res_time = utils.calculate_request_time(start_time)

    print('--- fetch_expo_tokens', res_time)

    if success:
        save_data(
            'fetch_expo_tasks_results',
            data.get('name'),
            {
                'task': "fetch_expo_tokens",
                "res_time": res_time,
                "result": result
            }
        )


def send_push_notification(schedule):
    """ Sends expo push notifications. """

    start_time = utils.start_time()
    success, result = ER.send_expo_notifications(schedule)
    res_time = utils.calculate_request_time(start_time)

    print('--- send_push_notification', res_time)

    if success:
        reciepts = result.get('data')

        ok_status_count = 0
        ok_status_count_total = len(reciepts)

        for reciept in reciepts:
            if reciept.get('status') == 'ok':
                ok_status_count += 1

        save_data(
            'notifications_results',
            schedule.get('name'),
            {
                'task': "send_push_notification",
                "res_time": res_time,
                "result": {
                    "success_sent_notifications": ok_status_count,
                    "success_sent_notifications_total": ok_status_count_total
                }
            }
        )

    # TODO: Maybe save receipts / id, and have another process that confirms that receipts were sent successfully?
    # if not successfull, maybe remove expo push token from db or make a list of expo push tokens that are
    # inactive and remove them eventually


async def main():
    # Before running, check if tokens are expired.
    await asyncio.create_task(check_auth_tokens())

    # while True:
    #     try:
    #         run()
    #     except Exception as e:
    #         print(e)
    #         sleep(60)


if __name__ == "__main__":
    print('starting..')
    asyncio.run(main())
