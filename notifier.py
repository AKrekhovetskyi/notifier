#!/usr/bin/python3.8

from time import sleep, strftime

import notify2

config = {
    "hour of enabling notifications": 8,  # In a 24-hour format.
    "hour of turning off notifications": 20,  # In a 24-hour format.
    "days without notifications": {},  # E.g. "Sunday".
    "waiting interval": 20,  # In minutes.
    "summary": "Reminder!",
    "message": "Time to stretch your eyes!",
    "icon": "",  # Path to the icon.
}


def show_notification() -> None:
    while True:
        current_hour = int(strftime("%H"))
        if (
            strftime("%A") in config["days without notifications"]
            or config["hour of enabling notifications"] > current_hour
            or current_hour > config["hour of turning off notifications"]
        ):
            return

        # Initialise the d-bus connection.
        notify2.init("News Notifier")

        # Create Notification object.
        notify = notify2.Notification(
            config["summary"], config["message"], config["icon"]
        )

        # Set urgency level.
        notify.set_urgency(notify2.URGENCY_CRITICAL)

        # Sho the notification, wait for 3 seconds and close it.
        notify.show()
        sleep(3)
        # Prevents the notification from being saved to the stack.
        notify.close()

        sleep(60 * config["waiting interval"])


show_notification()
