
# for Loop

a = [1,2,3,4,5]
for i in a:
        print (i, end='')

#for loop using range()
for i in range(len(a)):
    print(a[i])

for i in range(10,30,2):
    print(i)


#to check the even numbers in the list
a = [11,33,55,39,55,75,37,21,23,41,13]
for num in a:
    if num%2 == 0:
        print('the list contains even number')
else:
    print('the list doesnt contain even number')

count = 0
while(count<5):
    print(count,"is less than 5")
    count = count + 1
else:
    print(count,'is not less than 5')

for i in range(1,11):
    print(i, end='')


list = [12, 23, 34, 45, 56, 67, 78, 89, 90]
myinput = int (input("Enter the number"))
for i in list:
    if i==myinput:
        print('the current number is', i)
        print('number found in list')
        break
else:
    print('number not found in list')

list = [ 1,2,3,4,5,6]
it = iter(list)
print (next(it))

for count in range (10):
    print (count)