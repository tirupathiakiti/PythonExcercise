#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def EvenOdd(Num):
         if int(Num)%2 == 0:
             print('You Entered even number')
         else:
             print('You Entered odd number')
         
EvenOdd(input('Enter Random number : '))
