from sys import argv
from os.path import exists

print "Copying from %s to %s" % (argv[1], argv[2])
open(argv[2], 'w').write(open(argv[1]).read())

