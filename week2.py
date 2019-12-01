# Median of three numbers
a = 4
b = 2
c = 10
median = 0
if (a >= c and b >= a) or (c >= a and a >= b):
    median = a
elif (b >= c and a >= b) or (c >= b and b >= a):
    median = b
else:
    median = c
print median

# Triangle number
n = int(raw_input())
i = 0
for num in range(1, n+1):
    for _ in range(num):
        print i,
        i += 1
    print