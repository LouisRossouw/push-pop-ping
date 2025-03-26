
import os
from .utils import check_path_exists, get_datetime, write_to_json

this_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(this_dir)


def save_expo_tokens(name, tokens):
    """ saves expo push tokens. """

    current_date = get_datetime()

    data_dir = os.path.join(f"{root_dir}", "data")
    tokens_dir = os.path.join(f"{root_dir}", "data", 'expo_push_tokens')

    check_path_exists(data_dir)
    check_path_exists(tokens_dir)

    json_name = f"{str(name)}_tokens.json"
    file_path = os.path.join(tokens_dir, json_name)

    data = {
        "timestamp": current_date.get('timestamp'),
        "last_updated": current_date.get('date_time_now'),
        "expo_push_tokens": tokens
    }

    write_to_json(file_path, data)

    return True


if __name__ == "__main__":

    data = [{'user': 'username', 'token': 'ExponentPushToken[xxxxx]', 'active': True}, {
        'user': None, 'token': 'ExponentPushToken[xxxxx]', 'active': True}]

    save_expo_tokens('project_name', data)
