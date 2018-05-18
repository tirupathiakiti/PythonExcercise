#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
str = input('Enter String')
n = int(input('Enter the Number of repitations: '))
if len(str) <=2:
    print(str*n)
else:
    print(str[:2]*n)
