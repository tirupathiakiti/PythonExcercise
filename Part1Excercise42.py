#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
import struct
import sys

print(struct.calcsize('p')*8)
print(sys.version)
