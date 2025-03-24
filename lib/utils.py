import os
import time
import json
import random
import string
import datetime
import calendar
import requests
from colorama import Fore, Back, Style, init


def remove_ext(files_path):
    """ Simply removes the format extension no matter how long it is. """

    get_extension = len(str(files_path).split(".")[-1])
    clean_path = str(files_path)[:-get_extension]

    return clean_path


def generate_random(value_min, value_max):
    """ Generates random number. """

    generated_value = random.randint(value_min, value_max)

    return generated_value


def write_to_json(json_path, data):
    """ Create and write to json file """

    with open(json_path, 'w') as f:
        json.dump(data, f, indent=6)


def read_json(json_path):
    """ Reads json file """

    with open(json_path) as f:
        json_file = json.loads(f.read())

    return (json_file)


def check_path_exists(path):
    """ Check if path exists, if not, create it. """

    if os.path.exists(path) != True:
        os.mkdir(path)

    return True


def return_current_time_H_M():
    """ Return time in format 14:30 """

    time_struct = time.localtime(time.time())
    formatted_time = time.strftime("%H:%M", time_struct)
    return formatted_time


def convert_to_timestamp(time_str):
    """ convert a str 14:30 format to a timestamp. """

    current_date = time.localtime()[:3]
    time_str_with_date = f"{current_date[0]}-{current_date[1]}-{current_date[2]} {time_str}"
    time_struct = time.strptime(time_str_with_date, "%Y-%m-%d %H:%M")
    return time.mktime(time_struct)


def is_internet_available():

    try:
        response = requests.get("http://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        print("No Internet.")
    return False


def start_time():
    """ Prints when an API is called. """

    start_time = time.time()
    return start_time


def calculate_request_time(start_time, to_print=False):
    """ Calculates the Database queries. """

    end_time = time.time()
    elapsed_time = end_time - start_time
    if to_print:
        print(Fore.YELLOW, 'DB time: ', elapsed_time, Style.RESET_ALL)
    return elapsed_time


def generate_random_code(length=5):

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_datetime():
    """ Returns date time """

    now = datetime.datetime.now()

    return {
        'day_num': now.day,  # Day of the month
        'date_now_full': now,  # Full datetime object
        'date_year': now.year,  # Year
        'day_month_num': now.month,  # Month number
        'current_time': now.time(),  # Current time object
        'timestamp': now.timestamp(),  # Unix timestamp
        'date_now': now.strftime('%Y-%m-%d'),  # Date in YYYY-MM-DD format
        'date_time': now.strftime('%H:%M:%S'),  # Time in HH:MM:SS format
        'date_time_now': now.strftime('%Y-%m-%d %H:%M:%S'),  # Date in YYYY-MM-DD format # nopep8
        'day_name': calendar.day_name[now.weekday()],  # Day of the week
        'day_month_name': calendar.month_name[now.month],  # Month name


    }


if __name__ == "__main__":
    print(datetime.datetime.now().time())
