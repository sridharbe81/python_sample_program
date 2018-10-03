import subprocess
from subprocess import Popen, PIPE

#subprocess.run(['ls' '-l'],)

#subprocess.call(['cmd'])
#subprocess.call('du -hs $HOME')
#subprocess.call(['df', '-h'])

# out = subprocess.check_output(['arp','-a'])
# print(out)
#
#
#
# print('*'*200)
# p = subprocess.Popen(['arp','-a'], stdout= subprocess.PIPE)
# print(p.communicate())
# #subprocess.Popen(['ls','-l'],stdout=subprocess.STDOUT)

#Learnt with Ram (ramarram)

#s = subprocess.Popen(['ping','127.0.0'], stdout= open('out.txt','w'), stderr= open('err.txt','a'))
#out, error = s.communicate()

# Import the module
import subprocess

# Ask the user for input
host = raw_input("Enter a host to ping: ")

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]

print output







