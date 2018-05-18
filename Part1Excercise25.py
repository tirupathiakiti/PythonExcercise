#Write a Python program to check whether a specified value is contained in a group of values.
#Test Data : 
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

num = int(input(' Enter value : '))
values = (1,5,8,3)
if num in values:
    print ('True')
else:
    print('False')
