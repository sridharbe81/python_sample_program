
import os
print(os.getcwd())
try:
    with open('sample1','r') as rf:
        line = rf.readline()
except FileNotFoundError as e:
    print(e)
else:
    print(line)

with open('sample') as f:
    for line in f:
        row=line.split(" ")
        print(row[0]+"\n----------------")
        for i in range(1, len(row)):
            print(row[i])

try:
    with open('sample1','r') as rf1:
        print(rf1)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


string = 'fast ethernet'
list = [s[0].upper() + s[1:] for s in string.split()]
print(" " .join(list))


