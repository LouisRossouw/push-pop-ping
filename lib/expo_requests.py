import os
import json
import requests
from dotenv import load_dotenv

from .get_users import get_users
from .save_expo_tokens import save_expo_tokens

load_dotenv()

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

HEADERS = {
    "host": "exp.host",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate",
    "content-type": "application/json",
}


def send_expo_notifications(schedule):
    """ Send Expo push notifications to users """

    project_name = schedule.get('name')
    to_users = schedule.get('to_users', [""])  # anonymous / auth / is_staff
    notification = schedule.get('notification')

    users = get_users(project_name, to_users[0])

    # TODO: Get a list of expo push tokens that were saved locally (maybe direct from server?) in .json
    # Filter out tokens based on the to_users values.

    # TODO: Calculate total users and plit them up
    # into multiple requests; Expo allows sending up 100 notifications per request.

    # TODO: How to send personalized notifications to specific users?

    expo_push_tokens_list = []

    for user in users:
        expo_push_tokens_list.append(user.get('token'))

    data = json.dumps({
        "to": expo_push_tokens_list,
        "title": notification.get("title"),
        "body": notification.get("body"),
        "data": notification.get("data"),
    })

    response = requests.post(EXPO_PUSH_URL, headers=HEADERS, data=data)

    return True, response.json()


def get_expo_push_tokens(project):
    """ Fetches a list of expo push tokens from a given endpoint. """

    TOKEN = os.getenv('TEMP_ACCESS_TOKEN')
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    URL = f"{project.get('base_url')}/{project.get('fetch_expo_tokens_api')}"

    response = requests.get(URL, headers=HEADERS).json()
    maybe_expo_tokens = response.get('data')

    if maybe_expo_tokens:
        return save_expo_tokens(project.get('name'), maybe_expo_tokens)

    return True, "todo"


def get_expo_push_receipts(self, url):
    """ Fetches a list of receipts """

    # TODO: Fetch all the successfull receipts that were sent via expo push notifications,
    # Remove push notifications tokens that have failed receipts.

    pass
