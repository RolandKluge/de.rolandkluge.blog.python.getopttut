import getopt
import sys

try:
  opts, args = getopt.getopt(sys.argv[1:], "hfv:m:", ["help", "flag", "valueoption", "multivalue"])
except getopt.GetoptError as err:
  print str(err)
  usage()
  sys.exit(2)

flag = False
valueoption = None
multivalue = []
  
for o, a in opts:
  if o in ("-h", "--help"):
    print "Usage: " + __file__ + """ [-h] [-f] [-v]
    
    -h,--help   print help
    
    -f,--flag   set flag
    
    -v,--valueoption
                assign a single value
    -m,--multivalue
                store values in a list
    """
    sys.exit()
  elif o in ("-f", "--flag"):
    flag = True
  elif o in ("-v", "--valueoption"):
    valueoption = a
  elif o in ("-m", "--multivalue"):
    multivalue.append(a)  

print "Flag is set? " + str(flag)
print "Single value option: " + str(valueoption)
print "Multi-value option: " + str(multivalue)