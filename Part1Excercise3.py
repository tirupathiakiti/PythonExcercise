#Write a Python program to display the current date and time.
#Sample Output : 
#Current date and time : 
#2014-07-05 14:34:14

import datetime
dt= datetime.datetime.now()
print('Current date and time :')
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
