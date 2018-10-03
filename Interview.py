# str = " I am having python interview today"
# list = str.split()
# print (list)
#
# str1 = "Vivekananth Palanivel"
# list1 =str1.split()
# print(" ".join(list1))
#
# my_list = " ".join(list)
# print(my_list)
#
# list1 = ['a','b',['ab','ba']]
# list2 = list1
# list2[2][1] = 'd'
# print(list2)
# print(list1)
#
# a= " I am having python interview today"
# list = a.split()
# for i in list:
#     print(i)
# itr = iter(list)
# print(itr)
# print(next(itr))

#Printing the dictionary in alphabetical Order
# my_dict = {"Name": "Vivek", "DU" : "NAT", "SAP":"NOne","Alpha":"COde"}
# for i,j in sorted(my_dict.items()):
#     print("{0} is {1}".format(i,j))


int = ['gig1/2','fa0/1','fa0/2','gig0/1']
val = [23,45,67,78]
util ={}
for i,j in (zip(int,val)):
    util[i]=j
print(util)


list = [1,2,3,4,5,6]
for i in list:
    if i%3==0:
        continue
    else:
        square=i*i
    print(square)



dict = {"z":10, "y":20, "a":10, "x":30}
for i,j in sorted(dict.items(),key=dict.get):
    #print("{0}:{1}".format(key,value))
    print (i, j)





