num = [1,2,3,4,5,6,1,4,7,8,2,9]
sorts = sorted(no)
num = {}
print(sorts)

# def mean(x):
#     a = (sum(x)/len(x))
#     print(a)
#     return a

# mean(no)

# index = len(sorts)//2
# print(index)

# def median(x):
    
#     index = len(sorts)//2
#     print(index)

#     if len(no)%2 != 0:
#         return sorts[index]
#     else:
#         return (sorts[index-1] + sorts[index])/2

# print(median(no))
    

# def mode(x):
#     for i in no:
        

# def SD(x):
#     SD = ((((x-X)**2)/n))**0.5
#     return SD
# print(SD(no))


# def var(x):
#     for i in no:
#         (i-mean(no))**2
#     num =sum((x-mean(no))**2)
#     denom = sum(no)
#     equ = num/denom


# a = str(sorts)
# print(a)
# " ".join(a)
# a.split()
# print(a)
# def prime_no(x):

#     if no


def mean(num):
    return sum(num)/len(num)

def median(num):
    sorted(num)
    if len(num)%2 == 0:
        mid_point = len(num)//2
        first = num[mid_point-1]
        second = num[mid_point]
        return (first+second)/2
    else:
        mid_point = len(num)//2
        return num[mid_point]


def mode(num):
    freq = {}
    for i in num:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1

    max_key = max(freq, key = freq.get)

    return max_key

a = mode([0,1,2,4,1,1])
print(a)

def std(num):
    m = mean(num)
    return ((sum([a-m for a in num]))**2/len(num))**0.5


def variance(num):
    st = std(num)
    return st**2


def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def prime_in_list(num):
    return list(filter(lambda x: prime(x), num))

print(prime_in_list)