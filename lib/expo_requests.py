import os
import requests


def send_expo_notifications(data):
    """ todo """

    EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

    HEADERS = {
        "host": "exp.host",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "content-type": "application/json",
    }

    to_users = data.get('to_users')
    notification = data.get('notification')

    # TODO: Get a list of expo push tokens that were saved locally (maybe direct from server?) in .json
    # Filter out tokens based on the to_users values.

    data = {
        "to": "TODO",
        "title": notification.get('title'),
        "body": notification.get('body'),
        "data": notification.get('data')
    }

    response = requests.post(EXPO_PUSH_URL, json=data, headers=HEADERS).json()

    # TODO: Maybe save receipts / id, and have another process that confirms that receipts were sent successfully?
    # if not successfull, maybe remove expo push token from db or make a list of expo push tokens that are
    # inactive and remove them eventually

    # response:
    # {
    # 	"data": {
    # 		"status": "ok",
    # 		"id": "xxxxxxxc-xxxx-xxxx-xxx-xxxxxxxxxx"
    # 	}
    # }

    return True


def get_expo_push_tokens(data):
    """ Fetches a list of expo push tokens from a given endpoint. """

    TOKEN = ""
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    URL = f"{data.get('base_url')}/{data.get('fetch_expo_tokens_api')}"

    print(data)
    print('URL')
    print(URL)

    # response = requests.get(URL, headers=HEADERS)

    return True


def get_expo_push_receipts(self, url):
    """ Fetches a list of receipts """

    # TODO: Fetch all the successfull receipts that were sent via expo push notifications,
    # Remove push notifications tokens that have failed receipts.

    pass
