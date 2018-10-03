def match_ends(list):
    count = 0
    for i in list:
        if len(i)>=2 and i[0] == i[-1]:
          count += 1
    return count

print(match_ends(["Python",'is', 'little', 'difficult', 'to','understand', 'pip', 'bob']))

def front_x(list):
    x_list=[]
    other_list=[]
    for i in list:
        if i[0] == 'x':
            x_list.append(i)
        else:
            other_list.append(i)
    return sorted(x_list) + sorted(other_list)

print(front_x(['abc','xyz','ijk','xyx','xavier']))


tuple = [(1,3,99),(2,1,1),(1,2,00)]
print(sorted(tuple, key= lambda x:x[-1]))


tuple1 = ['aab','caza', 'bca']
print(sorted(tuple1, key=len()))

list1 = [1,3,4,5]
list2 = [2,6,1]
list3 = set(sorted(list1) + sorted(list2))
print(list3)





