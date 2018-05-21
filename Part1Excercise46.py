#Write a python program to get the path and name of the file that is currently executing
import os,sys
print(os.path.dirname(os.path.realpath(sys.argv[0])))
#print("Current file name : ",os.path.realpath(_file_))



