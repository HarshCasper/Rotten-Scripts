#!/usr/bin/env python3
import os
import subprocess
import time
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import yaml


def execute_terminal_command(command):
    """
    THIS FUNCTION EXECUTES A TERMINAL COMMAND USING SUBPROCESS MODULE
    """
    try:
        return subprocess.check_output(command).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        pass


def update_pie_chart(labels, sizes, log_dir):
    """
    THIS FUNCTION SAVES/UPDATES PIE CHART USING: labels, sizes
    AND SAVES IT INTO log_dir
    """
    # Plotting pie chart
    fig = plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%",
            shadow=True, startangle=140)
    plt.axis("equal")
    plt.savefig(logdir + "/time_tracking_pie_chart.png")
    plt.close(fig)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        required=False,
        default="config.yaml",
        help="path to config",
    )
    args = parser.parse_args()

    with open(args.config, mode="r") as fp:
        config = yaml.safe_load(fp)

    update_frequency = config["update_frequency"]  # Uodate time in seconds

    # Update time in seconds
    pie_chart_update_frequency = config["pie_chart_update_frequency"]
    # List that stores all apps names
    applist = []

    # List that stores corresponding information to those apps in applist
    winlist = []

    # Logs folder within the same working directory
    logdir = os.getcwd()

    while True:
        # Wait for the update frequency
        time.sleep(update_frequency)

        # Get the current opened window process id
        frpid = execute_terminal_command(
            ["xdotool", "getactivewindow", "getwindowpid"])

        # Get the current opened window name
        frname = execute_terminal_command(
            ["xdotool", "getactivewindow", "getwindowname"]
        )

        # Obtain the app name using ps terminal command
        app = execute_terminal_command(["ps", "-p", frpid, "-o", "comm="])

        # adding the app to the app list
        if not app in applist:
            applist.append(app)
        checklist = [item[1] for item in winlist]
        if not frname in checklist:
            winlist.append([app, frname, 1 * update_frequency])
        else:
            winlist[checklist.index(frname)][2] = (
                winlist[checklist.index(frname)][2] + 1 * update_frequency
            )

        update_pie_chart(applist, [x[-1] for x in winlist], logdir)
