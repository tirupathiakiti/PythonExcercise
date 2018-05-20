#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
def test_num(x,y):
    if x==y or abs(x-y) ==5 or (x-y) ==5:
        return True
    else:
        return False

print (test_num(7,2))
