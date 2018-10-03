# #
# # tup = (1,2,3,4)
# #
# # tup1 = tuple()
# # for t in range(len(tup):
# #     if tup[t] == 2:
# #         tup1[t] = 'e'
# #     else:
# #         tup1[t] = tup[t]
# # print(tup1)
#
#
# dic = {
#     "a" : "value1",
#     "b" : "value2",
#     'name' : 'Divya',
#     'visa' : 'H1',
#     'Location' : 'sanjose'
# }
#
# print(sorted(dic, x = lambda x : dic))
#
#
# lis = [
#     (1,2,3,4),
#     ('divya', 'vivek','abc'),(1,4,7,8,9)
# ]
#
# lis.sort(key=lambda t : len(t[1]))
#
#
#
# def wraper(foo):
#     print("starting wraper")
#     foo()
#     print("End wrapper")
#
# @wraper
# def foo():
#     print("into foo function")
#
# foo()
#
# #Generator
# def gen():
#     for i in range(10):
#         yield(i)
#
# print(gen().next)

import os
from datetime import datetime
list = os.listdir(os.getcwd())
# for file in list:
#     mod_time = os.stat(file).st_mtime
#     print(file,'\t', datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Currentpath:", dirpath)
    print("Dirname:", dirnames)
    print("Filename:", filenames)

path = os.getcwd()
def print_dir_contents(path):
     for files in os.listdir(path):
        filepath = os.path.join(path,files)
        if os.path.isdir(filepath):
            print_dir_contents(filepath)
        else:
            print(filepath)
print_dir_contents(path)




