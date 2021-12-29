#!/usr/bin/python3
import os
import sys
import time
import random


k = int(sys.argv[1])
print(f"Program Child is running in process with PID {os.getpid()} and with arg {k}.")
time.sleep(k)
print(f"Process with PID {os.getpid()} is done.")
status = random.choice([0, 1])
os._exit(status)