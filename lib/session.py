import os
from time import time
from .utils import read_json

this_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(this_dir)


async def check_auth_tokens():
    """ Check all the auth tokens if any has expired. """
    projects = read_json(root_dir, "projects.json")

    print('checking auth tokens')

    for project in projects:
        is_expired = await is_token_expired(project.get('name'))

        if (is_expired):
            await run_authentication(project)

        print(is_expired)


def get_minutes_until_expiration(expires_at):
    current_time = int(time())  # Get current time in seconds
    return (expires_at - current_time) // 60  # Convert seconds to minutes


async def token_expire_time(project_name):
    auth = read_json(root_dir, "auth.json")
    expires_at = auth.get(project_name).get("expiresAt")
    expires_at = int(expires_at) if expires_at else 0

    minutes_until_expiration = get_minutes_until_expiration(expires_at)
    return minutes_until_expiration


async def is_token_expired(project_name):
    minutes_until_expiration = await token_expire_time(project_name)
    return minutes_until_expiration < 5


async def run_authentication(project):
    print('TODO: auth needed for:', project.get('name'))

    # TODO: Open the browser,
    # open the projects auth url,
    # get access token, refresh token, expires,
    # save locally to auth.json

    # TODO: How to secure acceess tokens? consider keyring,
    # or leave it for now, this is a local project that is intended only for my use.

    # TODO TODO: Would be fun to automate the auth flow with selenium.
