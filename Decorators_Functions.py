# def myFunction(in_function):
#    def out_function():
#       print("Entry: ", in_function.__name__)
#       in_function()
#       print("Exit: ", in_function.__name__)
#    return out_function

#Decorators without logging Module
# import time
# import datetime
# def decorator(original_function):
#    def inner_function(*args,**kwargs):
#       print('before',datetime.datetime.now())
#       x = original_function(*args,**kwargs)
#       print (x)
#       time.sleep(5)
#       print('after', datetime.datetime.now())
#       #return x
#    return inner_function
#
# @decorator
# def sum(*args):
#    total = 0
#    for i in args:
#       total = total + i
#    return total
#
# sum(2,3,4)
#
# @decorator
# def print_test():
#    message = 'Kaipulla,with out error'
#    return message
#
# print_test()

#-----------------------------------------------------------------------------
#Decorators without logging - Example 2

def decorator(original_function):
   def wrapper_function():
      print("Decoration Started")
      x = original_function()
      print("Decoration Ended", '\n')
      return x

   return wrapper_function

@decorator
def message():
   print('Trying my Best')

@decorator
def message1():
   print('I think I succeeded')

message()
message1()
#-----------------------------------------------------------------------------
#Decorators without logging and also DECORATORS PASSING ARGUMENT
def prefix_decorator(prefix):
   def decorator(original_function):
      print(prefix,"Decoration Started")
      def wrapper_function():
         y = original_function()
         print(prefix, "Decoration Ended")
         return y
      return wrapper_function
   return decorator

@prefix_decorator('Testing:')
def message2():
   print('Lets Try the Decorator with Argument')

message2()
#-----------------------------------------------------------------------------
# Decorators with Logging module
# import logging
# import datetime
# import time
#
# def decorator1(original_function):
#    logging.basicConfig(filename='decorator.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
#    logging.info('started Decoration')
#    def wrapper_function(*args):
#       logging.info(datetime.datetime.now())
#       logging.info('Ran with Arguments : {} and {}'.format(args[0], args[1]) )
#       x= original_function(*args)
#       print('The sum of {} and {} is :'.format(args[0],args[1]), x)
#       time.sleep(5)
#       logging.info(datetime.datetime.now())
#    return wrapper_function
#
# @decorator1
# def sum(*args):
#    total =0
#    for i in args:
#       total = total + i
#    return total
#
# sum(45,56)
# sum (65, 99)
