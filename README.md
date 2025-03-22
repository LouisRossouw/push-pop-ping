# push-pop-ping

Expo push notifications automation ~ maybe

## Projects

./projects.json

```
[

    {
        "name": "project_name",
        "interval": 5,
        "interval_type": "seconds",
        "base_url": "https://www.something.com",
        "fetch_expo_tokens_api": "api/get-push-notification-tokens"
    }

]
```

## Notifications

./notifications.json

```
{
    "project_name": [
        {
            "name": "Test Notification 1",
            "to_users": ["all"],
            "interval": 1,
            "interval_type": "days",
            "notification": {
                "title": "test title 1",
                "body": "test body 1",
                "img": null,
                "data": {"advertise": true, "promoImg": "/todo"}
            }
        },
        {
            "name": "Test Notification 2",
            "to_users": ["anonymous"],
            "interval": 1,
            "interval_type": "days",
            "notification": {
                "title": "test title 2",
                "body": "test body 2",
                "img": null,
                "data": {}
            }
        }
    ]
}
```
