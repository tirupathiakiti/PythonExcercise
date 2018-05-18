#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum

a= int(input('First value: '))
b= int(input('First value: '))
c= int(input('First value: '))
sum = a+b+c
if a==b==c:
    print(3*sum)
else:
        print(sum)
