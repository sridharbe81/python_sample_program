# # multiply 2 numbers
# def multiply(x,y):
#     return x*y
# print(multiply(2,3))
#
# # If we use Lmabda, we need not to define functions,
r = lambda x,y : x*y
print (r(2,5))
#
# print(sum(range(1,101)))
# a=[[1,2,3],[4,5,6]]
# b = list(a)
# a[0][1] = 10
# print (a,b)
#
#
# list1 = ['a','b',['ab','ba']]
# list2 = list1[:]
# list2[2][1] = 'd'
# print(list2)
# print(list1)
#
# def foo():
#     print("begin")
#     for i in range(3):
#         print("before yield", i)
#         yield i
#         print("after yield", i)
#     print("end")
# f = foo()
# f.next()
items = [1,2,3]
f = ((lambda x:x*2), items)
print (f)

nums = [1,2,3,4,5]
my_list = map(lambda n: n*n, nums)
print(my_list)