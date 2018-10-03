import copy

print('SHALLOW COPY')
lst1 = [10,20,[30,40]]
lst2 = lst1
print('Mem of list1 before change in Object',id(lst1))
print('Mem of list2 before change in Object',id(lst2))
lst1[2][1] = 90
print('Value of lst1 after change is',lst1)
print('Mem of list1',id(lst1))
print('Value of lst2 after change is',lst2)
print('Mem of list2',id(lst2))

print('*' *200)

print('DEEP COPY')

dclist1 = [50,60,[70,80]]
dclist2 = copy.deepcopy(dclist1)
print('Mem of dclist1',id(dclist1))
print('Mem of dclist2',id(dclist2))
dclist1[2][1] = 100
print('Value of dclist1 after change is',dclist1)
print('Mem of dclist1',id(dclist1))
print('Value of dclist2 after change is',dclist2)
print('Mem of dclist2',id(dclist2))