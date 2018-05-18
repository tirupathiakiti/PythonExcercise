#Write a Python program to get the difference between a given number and 17,
#if the number is greater than 17 return double the absolute difference

n = int(input('Enter input value :'))
Diff = int(17 - n)
if n >= 17:
    print(int(abs(Diff*2)))
else:
        print(Diff)
