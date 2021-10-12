def add_num(x,y):
    # print(x+y)
    a = x+y

# add_num(2,4)

def add_num_2(x,y):
    a = x+y
    return x+y
    a += 1

a = add_num(2,4)
b = add_num_2(2,4)

print(a)
print(b)

def func_one(*names):
    print("Hello" + names[1])
func_one("James", "Harley", "Stones")