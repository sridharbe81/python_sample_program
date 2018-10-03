d = {"johri":40, "mayank":45}
print(list(d.keys()))

d = {"johri":40, "mayank":45}
print("johri" in d)

d1 = {"johri":40, "mayank":45}
d2 = {"johri":466, "mayank":45}
print(d1 == d2)


a=[1,2,3,4,5,6,7,8,9]
a[::2] = 10,20,30,40,50
print(a)

a=[1,2,3,4,5]
print(a[0:3:1])

def pow(x,y=2):
    r =1
    for i in range(y):
        r = r * x
    return r

print(pow(3,3))
