import time
import datetime


class Stopwatch:
    """A stopwatch simulator with functions start, stop, lap, and reset."""

    __startTime__ = None
    __currentLap__ = 0
    laps = []
    summary = None
    state = "Stopped"

    def __init__(self, precision=None):
        if precision:
            self.__precision__ = precision
        else:
            # Default to tenths of a second.
            self.__precision__ = 1

    def start(self):
        # Start the stopwatch.
        if not self.state == "Stopped":
            print("Stopwatch is already running.")
            return None

        self.__startTime__ = time.time()
        self.state = "Started"

    def lap(self):
        # Start tracking a new lap.
        self.__update__()
        self.laps.append(self.__currentLap__)
        self.__currentLap__ = 0
        self.__startTime__ = time.time()
        self.__update__()

    def stop(self):
        # Stop/Pause the stopwatch without clearing it.
        if self.state == "Stopped":
            print("Stopwatch isn't running.")
        else:
            self.__update__()
            self.state = "Stopped"

    def reset(self):
        # Reset the entire stopwatch back to zero.
        self.__startTime__ = None
        self.__currentLap__ = 0
        self.laps = []
        self.summary = None
        self.state = "Stopped"

    def __update__(self):
        # Internal function to update stopwatch summary.
        now = time.time()

        lapCounter = 1
        lapTime = 0
        lapSummary = ""
        for lap in self.laps:
            # Tally the laps into the total laptime.
            lapTime = round(lapTime + lap, self.__precision__)
            # Generate a pretty summary.
            lapSummary += (
                "\nLap "
                + str(lapCounter)
                + ": "
                + str(datetime.timedelta(seconds=round(lap, self.__precision__))).rjust(
                    14 - len(str(lapCounter))
                )
            )
            lapCounter += 1

        if not self.state == "Stopped":
            self.__currentLap__ += now - self.__startTime__

        totalTime = lapTime + self.__currentLap__
        self.summary = (
            "Total time: "
            + str(
                datetime.timedelta(seconds=round(totalTime, self.__precision__))
            ).rjust(8)
            + lapSummary
            + "\nCurrent Lap: "
            + str(
                datetime.timedelta(
                    seconds=round(self.__currentLap__, self.__precision__)
                )
            ).rjust(7)
        )