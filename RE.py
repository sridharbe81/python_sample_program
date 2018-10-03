
string = "Python interview today Python easy to learn"
s = string.split()
dict={}
for i in s:
    dict[i] = s.count(i)
print(dict)


str1 = 'fknwngiwngkjnkjnjnhvihtbpihvpyjewhjyqnjbsgvmq'
result ={}
for i in str1:
    result[i] = str1.count(i)
print(result)

import copy
parlist = [1,2,3,]

childlist1 = parlist
print("parentlist object reaference", id(parlist))
print("childlist1 object reaference", id(childlist1))
print (parlist , childlist1, '\n')

parlist = [1,2,3,[4,5,[6,'seven']]]
childlist2 = copy.copy(parlist)
print("parentlist object reaference", id(parlist))
print("childlist1 object reaference", id(childlist2))
print ( childlist2, '\n')

parlist = [1,2,3,[4,5,[6,'seven']]]
childlist3 = copy.deepcopy(parlist)
print("parentlist object reaference", id(parlist))
print("childlist1 object reaference", id(childlist3))
print ( childlist3, '\n')
