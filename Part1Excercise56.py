#Write a Python program to get height and width of the console window.
import shutil
WH = shutil.get_terminal_size()
print("Terminal size is %d * %d" % WH)
