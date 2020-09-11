import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Totaltime taken  %s ' % (totalTime), end='')
        if totalTime > 500.00:
            print("Program is taking too long to run.Press ctrl+c to stop")
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
       # Handle the Ctrl-C exception to keep its error message from displaying.
       print('\nDone.')