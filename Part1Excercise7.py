#Write a Python program to accept a filename from the user and print the extension of that
FileName = input(' provide file name with extension : ')
FileName_ext = FileName.split(".")
print (' Provided filename is :' + FileName + 'and extension is :'+ (FileName_ext[-1]))
