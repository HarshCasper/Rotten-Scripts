#!/usr/bin/python3
import os
import sys
import time
import threading
import subprocess as sp

class network():
	def monitor(self, limit, unit):
		check = "vnstat"
		proc = sp.Popen(check, shell=True, stdout=sp.PIPE)
		output = proc.communicate()
		output = str(output)
		l = []
		for t in output.split():
			try:
				if t=="MiB" or t=="GiB":
					l.append(t)
				else:
					l.append(float(t))
			except ValueError:
				pass
		if unit==l[5] and limit < l[4]:
			print("Network usage limit exceeded!")
			top.mainloop()
		arg = [limit, unit]
		threading.Timer(60.0, monitor, arg).start()

	def main():
		if len(sys.argv) > 3 or len(sys.argv) < 3:
			print("Command usage: Python data.py <data usage in MiB or GiB")
			print("example: python data.py 500MiB")
			print("or python data.py 2GiB")
			exit(1)
		else: 
			limit = float(sys.argv[1])
			unit = str(sys.argv[2])
			monitor(limit, unit)
	if __name__ == '__main__':
		main()