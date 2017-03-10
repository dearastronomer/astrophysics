import sys
import numpy
import matplotlib

number_of_args = len(sys.argv)
cmdflags = str(sys.argv)

def numeric(s):
 try:
  int(s)
  return True
 except:
  return False

f1 = filter(numeric,open(str(sys.argv[1])).read().split("\n"))
f2 = filter(numeric,open(str(sys.argv[2])).read().split("\n"))

print f1
print f2
print (sys.argv[1])
print (sys.argv[2])
