x = 5
def test ():
    global x
    x = 3
    print (x)

print(x)
test()
print(x)

#Explaining Enclosing
print('X'*20)
x = 'global x'
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'               #----> If you comment this x in inner function, the output for the x will be outer,
                                            # it will check for local if not found fetch the value of outer function

        print("The Local value of the x in inner function is",x)
    inner()
    print("The Local value of the x in outer function is",x)

outer()
print("The Global value of the x is",x)

#Explaining Builtin
import builtins
# def min():              # ----> min is an builtin function, this should not be used for user defined function
#     pass
m = min([34,33,45,56])
print("The Minimal Value of the list given is:", m)




# Explaining the Local and Global scope of the variable , "global x present inside the function insists to use the local variable as Global"
x = 'global x'
def test():
    global x
    print('x'*20)
    x= 'local x'
    print(x)

test()
print(x)

#Local, Enclosing, Global All in One

x = 'global x'
def outer():
    print('Y'*20)
    #x = 'outer x'
    def inner():
        nonlocal x
        x='inner x'
        print(x)
    inner()
    print(x)
outer()