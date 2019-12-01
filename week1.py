# switch two number
a = 5
b = 6
a, b = b, a

# find max of three numbers
a = 1
b = 2
c = 3

max = - sys.maxint - 1
if a > max:
    max = a
if b > max:
    max = b
if c > max:
    max = c
print max

# find max of five numbers
arr = [1, 2, 3, 4, 5]
max = - sys.maxint - 1
for n in arr:
    if n > max:
        max = n
print max
