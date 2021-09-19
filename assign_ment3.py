my_list = ['this', True, 'student', 45, 66.43]
new_list = my_list[:]
print(new_list)
newlist = my_list.copy()
print(newlist)

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list.pop(0)
sample_list.pop(4)
sample_list.pop(3)
print(sample_list)

colour_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
fav_colour = input('Please enter your favourite colour: ')
colour_list.append(fav_colour)
print(colour_list)

list1 = [10, 20, [300, 400,[5000, 6000], 500], 30, 40]
a = list1[2]
print(a)
b = a[2]
print(b)
a[2].append(7000)
print(list1)