import os
from .utils import read_json

this_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(this_dir)


def get_users(project_name, group=None):
    """ Returns expo tokens from json and filters out by group. """

    tokens_dir = os.path.join(f"{root_dir}", "data", 'expo_push_tokens')
    data = read_json(f"{tokens_dir}/{project_name}_tokens.json")

    if not data:
        return None

    tokens_raw = data.get('expo_push_tokens', [])
    tokens = get_users_by_group(tokens_raw, group)

    # Filter for active tokens.
    return [token for token in tokens if token.get("active")]


def get_users_by_group(tokens_raw, user_group):
    """ Filters out users by group name """

    users = [token for token in tokens_raw if token.get('group') == user_group]

    if users:
        return users

    return tokens_raw


if __name__ == "__main__":
    tokens = get_users('timeinprogress', 'anonymous')
    print(tokens)
