#!/usr/bin/python3
import os,sys


names  = input()
name1,name2 = names.split()


if(name1 =='' or name2 ==''):
    print('Usage: ./markdown2html.py README.md README.html')
    sys.exit(1)


current_directory = os.getcwd()
files_in_current_directory = os.listdir(current_directory)

if not name1 in files_in_current_directory:
    print(f"Missing {name1}")
    sys.exit(1)
elif not name2 in files_in_current_directory:
    print(f"Missing {name2}")
    sys.exit(1)



else:
    sys.exit(1)

