import time
from stopwatch import Stopwatch
myStopwatch = Stopwatch()

myStopwatch.start()
time.sleep(2)
myStopwatch.lap()
time.sleep(3)
myStopwatch.stop()
print (myStopwatch.summary)