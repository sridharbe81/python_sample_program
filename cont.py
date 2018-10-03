
# Normal Fibonacci
def fib(max):
    numbers = []
    a,b = 0,1
    while a<max:
        numbers.append(a)
        a,b = b, a+b
    return numbers
print(fib(10))

#Fibonacci using Generator
def fib(max):
    a,b = 0,1
    while a<max:
        yield a
        a,b = b, a+b
obj = fib(10)
print(obj)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))






