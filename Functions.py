# def changeme(mylist):
#     print('values before change', mylist)
#     mylist[1]=40
#     print('values after change in the function', mylist)
#
# mylist =[10,20,30]
# changeme(mylist)
# print('values outside the function', mylist)
#
# #Return
# def sum(arg1,arg2):
#     total = arg1 + arg2
#     print('Total inside function', total)
#     return total
#
# total = sum(10,20)
# print('Total outside function', total)
#
# def foo(bar):
#     return bar+1
# print(type(foo))
#
#
# list=[12,12,33,33,34]
# new_list = []
# for i in list:
#     if i not in new_list:new_list.append(i)
# print(new_list)
#
# str = "My name is vivek and vivek is a Man"
# word = str.split()
# word_count = {}
# for i in word:
#     word_count[i] = str.count(i)
# print (word_count)
#
# #find common items in start and end of lists
# def common_start_end_lists(list1, list2):
#     first_match = list1[0] == list2[0]
#     end_match = list1[-1] == list2 [-1]
#     return first_match and end_match
# print (common_start_end_lists( [1,2,4],[1,3,4] ))
#
# #finding largest number in the list
# def largest_number(list):
#     second_max= sorted(set(list))[-2]
#     print (second_max)
#     large_number = 0
#     for number in list:
#         if number > large_number:
#             large_number = number
#     print (large_number)
# largest_number([1,2,3,4,5])
#
# #Using *args and **Kwargs
# def sum_no(*numbers):
#     total=0
#     for number in numbers:
#         total = total + number
#     return total
# print (sum_no(1,2,3,4))
#
print("Function Return")
def get_adder():
    def add(a,b):
        def double(n):
            return n*2
        return double(a) + double(b)
    return add
my_adder = get_adder()
print (my_adder(4,5))

print("Filter usage")


#Assigning a function to a veriable
def outer_function():
    message = 'HI'
    def inner_function():
        print (message)
    return inner_function()

outer_function()









