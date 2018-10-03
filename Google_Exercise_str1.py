

s='fast ethernet'
list = [word[0].upper() + word[1:] for word in s.split()]
print(" ".join(list))


def mix(s):
    return (s[0] + s[1:].replace(s[0], '*'))
print(mix('vivvek'))

def donuts(n):
    if n >= 10:
        return('Number of donuts : many')
    else:
        return('Number of donuts:', n)
print(donuts(34))

def both_ends(s):
    if len(s)==2:
        return
    else:
        return(s[0:2]+s[-2:])
print(both_ends('vivek'))


def mix_up(a,b):
    c= b[:2] + a[2:]
    d = a[:2] + b[2:]
    return c+d

print(mix_up('mix','pod'))

def verbing(s):
    if len(s)<3:
        return s
    elif ((len(s) >= 3) and (s[-3:] == 'ing')):
        return s+'ly'
    elif len(s)>= 3:
        return s+'ing'

print(verbing('working'))

def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if n!= -1 and b!= -1 and b > n:
        s=s[:n] + 'good' + s[b+3:]
    return s
print(not_bad('The Dinner is not that bad'))

# def front_back(a, b):
#    a_middle = len(a) / 2
#    b_middle = len(b) / 2
#    if len(a) % 2 == 1:
#        a_middle = a_middle + 1
#    if len(b) % 2 == 1:
#        b_middle = b_middle + 1
#    return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]
#
# print(front_back('abcde', 'xy'))

a = ['aaz','bb','c','dd']
print(sorted(a, key = len))
print("".join(a))

a = "Hello World"
print(a.split())














