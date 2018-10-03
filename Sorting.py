class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('thanigai', 35, 30000)
e2 = Employee('sakthi', 34, 20000)
e3 = Employee('vivek', 33, 30000)

employee_list = [e1,e2,e3]

'''
def e_sort(emp):
    return emp.age

employees = sorted(employee_list,key=e_sort)
'''
employees = sorted(employee_list, key=lambda e : e.name)  #=> Lambda function can also use instead of custom function (e_sort())
print(employees)

#Sorting a List
li = [1,9,10,6,2,3,78]
print(sorted(li))
print(li.sort())

#sorting a Tuple
li2 = (12,2,4,67,89,345,11)
print(sorted(li2))

#sorting a Dictionary
dict = {'a':10, 'z':20,'c':30,'00':'a','01':'b'}
for i, j in sorted(dict.items()):
    print(i,j)

