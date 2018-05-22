#Write a Python program to print to stderr.
#from _future_ import print_function
#import sys

#def eprint(*args,**kwargs):
 #   print(*args, file = sys.stderr, **kwargs)
  #  eprint("abc","efg","xyz",sep = "--")


import sys

sys.stderr.write('error\n')
