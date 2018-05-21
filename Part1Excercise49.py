#Write a Python program to list all files in a directory in Python
#from os import listdir
#from os.path import isfile,join
#files_list = [f for f in listdif ('/home/students') if isfile(join('/home/students',f))]
#print(files_list);

import os
d = os.getcwd()
for i in os.listdir(d):
    print(i)
