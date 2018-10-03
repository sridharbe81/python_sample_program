
#Examples for OS modules
import os
from datetime import datetime
print(os.chdir('C:\Python\MyPythinFiles\Python Bascis'))
print(os.getcwd())    #--> displays the Current working Directory
print(os.listdir())   #--> displays the contents of the directory

print(os.getcwd())
#mod = os.stat('CEC.txt').st_mtime     #--> getting the statistics of the file and especially the last modification time
#print(datetime.fromtimestamp(mod))    #---> importing the datetime
#print(os.makedirs('test'))
#print(os.removedirs('test'))
#print(os.makedirs('C:\Python\MyPythinFiles\test'))  #---> Create a Directory, we can also use mkdir, However it will not allow to create sub directory
#print(os.removedirs('test'))
for dirpath, dirnames, filenames in (os.walk(os.getcwd())):
    print('Current Path:', dirpath)
    print('Directory Name:', dirnames)
    print('Filename:', filenames)
    #print()

print(os.path.join(os.getcwd(),'test1.py'))


#Listing the Name of the Directory and printing the path file with in that directory as well as any files contained
import os
path = os.getcwd()
def print_directory_contents(path):
    for files in os.listdir(path):
        filepath = os.path.join(path, files)
        if os.path.isdir(filepath):
            print_directory_contents(filepath)
        else:
            print(filepath)

        #print(files)
print_directory_contents(path)

# def prints(path):
#     path = os.getcwd()
#     for files in os.listdir(path):
#         filepath = os.path.join(path,files)
#         if os.path.isdir(filepath):
#             prints(filepath)
#         else:
#             print(filepath)

'''Write a program to list all the files in the given directory along with their length and last modification time.
The output should contain one line for each file containing filename, length and modification date separated by tabs.'''

# cd = os.getcwd()
# file = os.listdir(cd)
# for i in file:
#     print(i.stats)
import time
def fileinfo(path):
    path = os.getcwd()
    for i in os.listdir(path):
        print(i, ':' ,os.path.getmtime(i))
fileinfo(path)







