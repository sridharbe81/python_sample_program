import re

def find(pat, text):
    match = re.search(pat, text)
    if match : print(match.group())
    else: print('Not Found')
find(r'\d.*', '192.168.1.0/24 is my Ip address')


mystr = ["vivek",'is','good']
print(''.join(mystr))


filename = 'CEC.txt'
with open(filename,'r') as read_file:
    for lines in read_file.readlines():
        new_list=[]
        cec = lines[0:7]
        print(new_list.append(cec))


text = 'vivpalan@cisco.com'


# def firstn(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
# print(firstn(100))
# print (firstn(100).__next__())
# print (firstn(100).__next__())
# print (dir(xx))
# print(xx.next)


def test(n):
    i = 0
    while i < n:
        yield i

obj = test(10)
print (next(obj))
print (next(obj))