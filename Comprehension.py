num = [ 1,2,3,4,5,6,7,8,9,10]
my_list = []
for i in num:
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

#List comprehension to print the even numbers in the list
print([i for i in num if i%2 == 0])

#List comprehension to print the square of each number in the list
print([n*n for n in num])

#Program for squaring each number in the list
num = [ 1,2,3,4,5,6,7,8,9,10]
my_list1 = []
for i in num:
    my_list1.append(i*i)
print(my_list1)

#Program - Nested For Loop
list = []
for letter in 'abcd':
    for num in range(4):
        list.append((letter,num))
print(list)

#List comprehension for nested loop
print([(letter,num) for letter in 'abcd' for num in range(4)])

#Creating a Dictionary from 2 List
key = ['a','b','c','d']
value = [10,20,30,40]
# my_dict={}
# for key, value in sorted(zip(key,values)):
#     my_dict[key] = value
# print(my_dict)

#dictionary comprehension
my_dictcomp = {i:j for i,j in sorted(zip(key, value))}
print("Dictonary comprehension",my_dictcomp)

key1 = ['x','y','z']
value1 = [100,200,300]
my_dict1={}
for i,j in sorted(zip(key1,value1)):
    my_dict1[i]=j
print(my_dict1)



