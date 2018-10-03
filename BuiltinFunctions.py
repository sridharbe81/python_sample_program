#List
my_list = [10,20,30,40,50]
for i in my_list:
    print (i)

#Tuple
my_tuple = (10,20,30,40,50)
for i in my_tuple:
    print (i)

#Dictonary
my_dic = {'name': 'sridhar', 'age': '35', 'sex': 'male'}
for key,val in my_dic.iteritems() :
    print key, val

my_dic.values()


# def greater_than_10(num):return num>10
list = [23,34,10,9,8,7]
print(filter(greater_than_10,list))
#
# def starts_with_fa (text, prefix='fa'):
#     return text.startswith(prefix)
#     list = ['fa0/1', 'fa0/2', 'gi0/1']
# print (filter(starts_with_fa,list))
#

list = [ "a","a", "b", "c", "b"]
result = {}
temp = set (list)
for i in temp:
    result[i] = list.count(i)
print (result)

def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1) + fib (n-2)
print(fib(3))

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
for i in range (11):
    print (i, fact(i))

s = "hello this is hello this is baby baby baby baby hello"
my_list = s.split()
result = {}
for i in my_list:
    result[i] = my_list.count(i)
print (result)

text = "hello cruel world. This is a sample text"
result = {}
for i in text:
    result[i] = text.count(i)
print (result)