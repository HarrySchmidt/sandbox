"""For a reason unknown to me i cannot pull the readme file from github.
so it is not printed in this file"""

import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
    