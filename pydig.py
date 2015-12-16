import os
from subprocess import Popen, PIPE, STDOUT
infile = open('./ips.txt', 'r')
outfile = open('./dig-output.txt', 'w')
cmd1 = "/usr/bin/dig +short -x "

for line in infile:
	ip = line.rstrip()
	cmd = ("/usr/bin/dig +short -x")
	cmd1 = " ".join((cmd, ip))
	#print cmd1
	output = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)
	output1 = output.stdout.read().rstrip()
	output2 = " ".join((ip, output1))
	#print output2
	outfile.write( output2 + '\n' )

infile.close()
outfile.close()
#fin
