first_tuple = (False, "True", 100)
second_tuple = (1, 4, 9)
full_tuple = first_tuple+second_tuple
print(full_tuple)

tuple1 = (1, 3, 5, "False", 2, True)
del tuple1
print(tuple1)

my_tuple = "This", "is", "A", "tuple"
print(type(my_tuple))
print(my_tuple)

first = "John"
second = "Bull"
first, second = second, first
print(first)

aTuple = ("Orange")
print(type(aTuple))

aTuple = ("100",)
print(aTuple*2)

s = {"True", "Born", 45, "water"}
s.remove("Johnson")
print(s)
s.discard("Johnson")
print(s)
s.add("Johnson")
print(s)

b = {"Mary", "Favour", "Tunde", 50}
u = s.union(b)
print(u)

setA = {10, 20, 30, 40, 80}
setB = {100, 30, 80, 40, 60}
setC  = setA - setB
setD = setB - setA
print(setC)
print(setD)
A = setA.intersection(setB)
print(A)

c = setA.difference(setB)
print(c)
setA.difference_update(setB)
print(setA)

d = setA.symmetric_difference(setB)
print(d)
setA.symmetric_difference_update(setB)
print(setA)

s = {"True", "Born", 45, "Water"}
b = {"Mary", "Favour", "Tunde", 50}

u = s.union(b)
print(u)
s.update(b)
print(s)

a = {"True", "Born", 50, "Water"}
b = {"Mary", "Favour", "Tunde", 50}
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))
print(a.pop())
print(b.pop())

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# a = set1.intersection(set2)
# print(a)

b = set1.union(set2)
print(b)

set_1 = {10, 20, 30}
set_2 = {20, 40, 50}
set_1.difference_update(set_2)
print(set_1)

Set1 = {10, 20, 30, 40, 50}
Set1.difference_update({10, 20, 30})
print(Set1)

set1.symmetric_difference_update(set2)
print(set1)

set1.intersection_update(set2)
print(set1)

import timeit
from decimal import Decimal

# starttime = time.time()
arr = [-4, 3, -9, 0, 4, 1]
pos = []
neg = []
zero = []

for i in arr:
    if i > 0:
        pos.append(i)
    elif i < 0:
        neg.append(i)
    else:
        zero.append(i)

pos_ratio = len(pos)/len(arr)
neg_ratio = len(neg)/len(arr)
zero_ratio = len(zero)/len(arr)

print(round(Decimal(pos_ratio), 6))
print(round(Decimal(neg_ratio), 6))
print(round(Decimal(zero_ratio), 6))