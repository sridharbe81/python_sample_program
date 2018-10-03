
dict = {'Name':'Vivek', 'Age':'33'}
print('My Name is {} and I am {} Old.'.format(dict['Name'],dict['Age']))

print('My name is {Name} and I am {Age} years old'.format(**dict))

pi = 3.14378
print('The Value of pi is {:.02f}'.format(pi))

import datetime
my_date = datetime.datetime(2017,4,17, 7,16,15)
print('{:%B %d, %Y }'.format(my_date))


for i in range(11):
    print("The Value is {:02}".format(i))