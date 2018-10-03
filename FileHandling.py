#
# # creating a new file which is a copy of CEC
# # Read the file CEC and writing it to CEC_Copy
#
# with open('CEC.txt', 'r') as rf:
#     with open('CEC_COPY.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
#
# '''
# with open('CEC_COPY.txt', 'w') as wf:
#     for line in wf.writelines():
#         if line == 'vivpalan@cisco.com':
#             wf.seek(9)
#             wf.write('')
# '''
#
#
# #Python program to read first n lines of a file.
# # with open('CEC.txt','r') as rf:
# #     readfile = rf.readlines()
# #     print(readfile[0:5])
#
# #3. Appending a line in to a file [Doubt]
# with open('CEC.txt','a') as af:
#     lines = '\namuthuku@cisco.com'
#     af.write(lines)
#
# # with open('CEC.txt','r') as rf:
# #     for i in rf.readlines():
# #         print(i)
#
# #Python program to read a file line by line and store it into a list
# with open('CEC.txt','r') as rf:
#     newlist=[]
#     for eachline in rf.readlines():
#         newlist.append(eachline)
#     print(newlist)

#6 . Python program to read a file line by line store it into a variable.   ---> even
with open('CEC.txt', 'r') as rf:
    for aa in rf.readlines():
        print(aa)

    #aa = rf.readline()

#
# #13.Python program to copy the contents of a file to another file
# with open('CEC.txt', 'r') as rf:
#     with open('CEC_COPY1.txt', 'w') as wf:
#         for line in rf.read():
#             wf.write(line)


# list = [1,2,4,5]
# print(list[0:2])
#
# def list(val,[]):
#     list.append(val)
#     return list
#
# print(list(10,[]))