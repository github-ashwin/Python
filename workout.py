# List operations
li = ['HTML', 'CSS', 'JS', 'BOOTSTRAP', 'PYTHON', 'DJANGO', 'POSTGRESQL']
print(li[-1])
li.append("ASHWIN")
print(li)
li.insert(2, "MANGO")
print(li)
li.reverse()
print(li)

# Number list operations
num = [1, 2, 3, 4, 4, 4, 5, 6]
print(num.count(4))
print("MAX =", max(num))

# Tuple operations
tpl = (10, 20, 70, 50, 10, -5, -99)
print(len(tpl))
n = int(input("Enter number to be checked:"))
sum_val = 0
flag = False
for i in tpl:
    sum_val = sum_val + i
    if i == n:
        flag = True

if flag:
    print("Element found")
else:
    print("Element not found")

print(sum_val)

# Conversion and modification of a tuple
li = list(tpl)
print(type(li))
print(li)
rem = input("Enter the item to be removed")
li.remove(int(rem))
print(li)

# Sorting the list
li.sort()
print(li)

# Average calculation
avg = sum(tpl) / len(tpl)
print(avg)

# Count occurrences and check for equality in a tuple
print(tpl.count(10))
o = 0
e = 0
chk = tpl[0]
flag = True
for i in tpl:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
    if i != chk:
        flag = False

if flag:
    print("Equal")
else:
    print("Not Equal")

print("Odd elements:", o)
print("Even elements:", e)

# Tuple comparison
tpl = (1, 2, 3)
lpt = (1, 2, 3)

if tpl == lpt:
    print("EQUAL")
else:
    print("NOT EQUAL")

# Dictionary operations
my_dict = {'name': 'Ashwin', 'roll': 23, 'subject': 'Coding', 'marks': 100}
my_dict['age'] = 21
print(my_dict['marks'])
