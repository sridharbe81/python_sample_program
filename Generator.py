'''class Fib():
    def __init__(self):
        self.current=1
        self.previous=0
        self.max=5

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        if value > self.max:
            raise StopIteration
        self.current += self.previous
        self.previous = value
        return value
f=Fib()
itr = iter(f)
print(next(itr))
print(nextr))
print(next(itr))
'''

# G = (c * 5 for c in 'Python')
# print(list(G))
#
# num = [1,2,3,4]
# def gen_fun(num):
#     for i in num:
#         yield i*i
#
# my_gen = gen_fun(num)
# for i in my_gen:
#     print(i)

#Regular Method for Squaring Numbers given the list as an argument
def square_numbers(num):
    sq=[]
    for i in num:
        sq.append(i*i)
    return sq

print(square_numbers([1,2,3]))

#Generator Method for Squaring the number given the list as an argument  ( Generator = will not hold all the value in the memory)
def square_numbers(num):
    for i in num:
        yield(i*i)                                 # A Method which has the YIELD keyword is called Generator Function
sq_num = square_numbers([1,2,3])
for num in sq_num:
    print(num)

# # Squaring the number using List comprehension
# sq_num1 = [i*i for i in [1,2,3,4]]
# print(sq_num1)
#
# #Squaring the number , Generator using comprehension
# sq_num2 = (i*i for i in [1,2,3,4,5])
# for num in sq_num2:
#     print(num)




