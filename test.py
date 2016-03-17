from subprocess import call
import os

out = open("bigOutput.txt", 'w')

with open('batchfile.txt', 'rU') as f:
	for line in f:
		temp = open("tempCommandOutput.txt", 'w')
		test1 = line.strip()
		test1 = test1 + " >> tempCommandOutput.txt"
		call([test1],shell=True)
		sizeOfFile = os.stat('tempCommandOutput.txt').st_size

		print
		print test1 + " has size of " + str(sizeOfFile) + " bytes"

		if sizeOfFile > 100:
			out.write(line)
		temp.close()

f.close()
out.close()
