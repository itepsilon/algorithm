import time

def fibo_r(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_r(n - 1) + fibo_r(n - 2)

def fibo_i(n):
    a = 0
    b = 1
    for i in range(n-1):
        b = a + b
        a = b - a
    return b

start = time.time()
fibo_r(35)
end = time.time()
print(str((end - start) * 1000000) + " microseconds")

start = time.time()
fibo_i(35)
end = time.time()
print(str((end - start) * 1000000) + " microseconds")
