'''
list = ["mon","tue","wed"]
a = iter(list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''

class NextInList():
    def __init__(self) -> object:
        self.list = ["mon","tue","wed"]
        self.index = -1

    def __iter__(self):
        return(self)

    def __next__(self):
        self.index+=1
        if self.index == len(self.list):
            raise StopIteration
        return self.list[self.index]

obj=NextInList()
#itr=iter(obj)
print(next(obj))
print(next(obj))








