
import os
from .utils import read_json, check_path_exists, write_to_json, get_datetime

this_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(this_dir)

# Wip


def save_data(parent_dir, child_dir, data):
    """ Saves general data. """

    current_date = get_datetime()

    timestamp = current_date["timestamp"]
    date_year = current_date["date_year"]
    day_month_name = current_date["day_month_name"]
    date_time_now = current_date["date_time_now"]

    data_dir = os.path.join(f"{root_dir}", "data")
    save_dir = os.path.join(f"{root_dir}", "data", parent_dir)

    if child_dir:
        data_log_dir = os.path.join(save_dir, str(child_dir))
    else:
        data_log_dir = save_dir

    check_path_exists(data_dir)
    check_path_exists(save_dir)
    check_path_exists(data_log_dir)

    current_data_list = os.listdir(data_log_dir)
    data_count = len(current_data_list)

    json_name = f"{str(data_count)}_{str(date_year)}_{day_month_name}.json"
    file_path = os.path.join(data_log_dir, json_name)

    # Json file.
    if os.path.exists(file_path) != True:
        data_count = len(current_data_list) + 1
        json_name = f"{str(data_count)}_{str(date_year)}_{day_month_name}.json"
        file_path = os.path.join(data_log_dir, json_name)
        write_to_json(file_path, [])

    current = read_json(file_path)

    current.append({
        'timestamp': timestamp,
        'date_full': str(date_time_now),
        "data": data
    })

    write_to_json(file_path, current)


if __name__ == "__main__":
    save_data(None, 'push_pop_ping', {"test": "hellos"})
