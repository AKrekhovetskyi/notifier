#!/usr/bin/env bash

# Config
excluded_days=("Sunday") # Array of days without notifications.
wait_interval=20         # In minutes.
summary="Reminder!"
message="Time to stretch your eyes!"
icon_path="/home/andrii/Projects/notifier/eyes.png" # Optional: full path to icon

export DISPLAY=:1
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

# Check if today is excluded
for day in "${excluded_days[@]}"; do
    if [[ "$current_day" == "$day" ]]; then
        exit 0
    fi
done

# Show notification
zenity --notification --text "$message" --icon "$icon_path"
# notify-send -u normal -t 20000 -a Notifier "$summary" "$message" ${icon_path:+-i "$icon_path"}
# zenity --info --title="Reminder!" --text="Time to stretch your eyes!" --ellipsize
