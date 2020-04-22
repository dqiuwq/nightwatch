# observer.py
# ##############################################################################
# Author:           Desmond Qiu
# Date Created:     20/03/2020
# Purpose:          Using watchdog to trigger file system events in real-time 
# Version:          1.0 Draft
# ##############################################################################
import os
import sys
from pathlib import Path

# initialise dict
FILE_FORMATS = dict()

FILE_FORMATS['EXCEL'] = ['.xls', '.xlxs']
FILE_FORMATS['WORD'] = ['.doc', '.docx']
FILE_FORMATS['PDF'] = ['.pdf']
FILE_FORMATS['SCRIPTS'] = ['.sh', '.cmd', '.bat', '.py']
FILE_FORMATS['OTHERS'] = ['.jar']
print(FILE_FORMATS, type(FILE_FORMATS))

# extract home dir of user
path = os.path.expanduser("~\\Desktop")
directoryFiles = os.listdir(path)

# print entire list
print(directoryFiles, type(directoryFiles))

# print name if it is a folder/directory
for item in directoryFiles:
    #if os.path.isdir(path + "\\" + item): # check if is dir
    print(Path(item).absolute(), Path(item).suffix)
quit()