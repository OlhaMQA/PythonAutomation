class TL:
    def __init__(self, id):
        self.id = id
        id = 5

obama = TL(100)
obama.__dict__['age'] = 49

import copy


a = [1, 2]
b = [3, 4]

kv = {1:a, 2:b}
c = copy.deepcopy(kv)
kv[1][0] = 5
print(kv[1][0]+c[1][0])
f = {1:1, 2:2}
f = {}
print(len(f))
f[1] = 1
f["1"] = 2
f[1.0] = 4

sum = 0
for k in f:
    sum += f[k]

print(sum)

def func(x, **y):
    print(type(y))
def extendList(item, list=[]):
    list.append(item)
    return list

list1 = extendList(11)
list2 = extendList(156,[])
list3 = extendList('c')

print("list1 = {}".format(list1))
print("list2 = {}".format(list2))
print("list3 = {}".format(list3))
print(len(a+b))
def is_isogram(word):
    return len(word) == len(set(word.lower()))

print(is_isogram('abc'))
print(is_isogram('Aabc'))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        comparing = 'the same age as'
        if other.age < self.age:
            comparing = 'younger than'
        elif other.age > self.age:
            comparing = 'older than'
        return f'{other.name} is {comparing} me'