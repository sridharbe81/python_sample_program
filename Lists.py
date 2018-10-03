mylist = ['vivek', 51388990, 'NAT']
print(mylist)
#Updating the list, replacing the index value
mylist[2] = 'India'
print(mylist)
# deleting the list,
del mylist[2]
mylist3 = [ 1,2,3,4,5,6,7,'a','c','d',]
print(mylist3)
del mylist3[0]
mylist3.clear()
print (mylist3)
mylist1 = [ 51388990, 51388991]
print (max(mylist1))

# #String to List
mylist2 = "vivekananth palanivel"
list = list(mylist2)
print (list)

print(" ".split(mylist2))
#
#
#
int = ['fa0/1','fa0/2']
value = [20,30]
for int, value in zip (int,value):
    print ("The interface is %s, The Value of the Interface is %d" %(int, value))

 # print ( "Range and xRange\n")
for i in range (1,10):
     print(i)

mydict = {'Name':"Vivek", 'EmpId':51388990, 'Name':'NAT'}
print (mydict)
for k,v in mydict.items():
     print(v)

list = [1,2,3,4,5,6,7,8,9]
print("slice", list[-4:-1])

dict = {1:'a', 2:'b', 3:'c', 4:'d'}
for i,j in dict.items():
    print(i,j)
print ("Dictonary Items",dict)


list = [1,2,1,3,5,5]
my_list=[]
for i in list:
    if i in my_list : pass
    else: my_list.append(i)
print (my_list)

list = [1,2,1,3,5,5]
temp = set (list)
my_dict = {}
for i in temp:
    my_dict[i] = list.count(i)
print (my_dict)

list = [ 1,2,3,467,87,89,10]
x= [i for i in list if i>10]
print (x)

list = [ 1,2,3,467,87,89,10]
result = sorted(set(list))[-2]
print (result)

string = " My name is vivek"
print ( string[-2])

def power (x,y):
    z= pow(x,y)
    print (z)
power (2,10)

my_dict= {"name":"Vivek", "DU" : "Nat", "sap":51388990}
for i,j in my_dict.items():
    print (i,j)

items = [1,2,3,4,5]
y=0
for i in items:
    y = y + i
print(y)

mylist = [45,32,12,34]
print(sorted(mylist))


with open('CEC.txt', 'r') as rf:
    dict ={}
    for i in rf.read():
        for char in i:
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
print(dict)



