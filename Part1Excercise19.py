#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
str = input( 'Input a string')
str2= "Is"
if str.startswith("Is"):
    print ("string unchanged")
else:
    str3=str2+str
    print(str3)
