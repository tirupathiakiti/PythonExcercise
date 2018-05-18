#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def copyString(num,string):

    if num < 0:
        print(' Enter positive value')
    else:
            print(string*num)
num = int(input('Enter Number : '))
string = input('Enter String : ')
CopiedString = copyString(num,string)
