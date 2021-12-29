#!/usr/bin/python3
import os
import sys
import random


N = int(sys.argv[1])
ppid = os.getpid()

for i in range(N):
	if ppid == os.getpid():
		child = os.fork()
		if child == 0:
			k = random.randint(5, 10)
			path = os.path.abspath("child.py")
			os.execl(path, "child", str(k))

for i in range(N):
	done = os.wait()
	print(f"Child process with PID {done[0]} is done. Status {done[1]}")
