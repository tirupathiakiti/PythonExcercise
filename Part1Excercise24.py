#Write a Python program to test whether a passed letter is a vowel or not
str = input('Enter text : ')
vowels = frozenset("aeoiu")
for char in str:
    if char in vowels:
        print ('vowel')
    else:
        print(' Not vowels')
