# Python Script to Heat your CPU Cores in Cold Temperatures

from multiprocessing import Process, cpu_count
from sys import argv

defaultProcessCount: int = cpu_count()
processCount: int = int(argv[1]) if len(argv) > 1 else defaultProcessCount


def heat():
    for i in range(1 * 10**16):
        i = i ** i


for i in range(processCount):
    print("Starting process number:", i + 1)
    t = Process(target=heat)
    t.start()
