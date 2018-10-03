sentence = "Laksmi Renuka have completed  and Networking and Virtualization and currently learning python"
print(len(sentence))
print(sentence[82:88])
split_list =(sentence.split())

#Write a Program to iterate over the list (split_list)
for word in split_list:
    print("current word:", word)
   # word=word+1

#write a program to print the list with identical values
list=[]
for word in split_list:
    if word not in list:
        list.append(word)
print(list)

# write a program to print until networking in list(list)
for word1 in list:
    if word1=='and':
        continue
    else:
        if word1 == 'Virtualization':
            break
    print("current word :", word1)

# Functions , to add 2 numbers
def sum(a,b):
    sum=a+b
    print("sum of 2 nums is:", sum)
sum(10,20)
sum(20,33)

#Function, to add 2 numnbers and return the sum to the calling Function
def sum1(a,b):
    sum1=a+b
    return "Sum of numbers:", sum1
print(sum1(10,10))

#Function, variable length Arguments
def sum2(*j):
    sum =0
    for i in j:
        sum = sum + i
    return sum

print(sum2 (100,200))
print(sum2 (100,200,300))

#scope ,

def scope():
    x = 'outer'
    def scope1():
        #nonlocal x
        #x ='inner'
        print(x)
    scope1()
    print(x)

scope()




