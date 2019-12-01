# Histogram Sort
def histogram_sort(nums):
    count = [0] * 256
    for num in nums:
        count[num] += 1
    result = []
    for key, value in enumerate(count):
        if value > 0:
            result += [key] * value 
    return result

import time
from random import randint

arr = [
    1, 3, 5,  7,  9,  3,  4, 4, 5, 6,
    1, 3, 5,  7,  9,  3,  4, 4, 5, 6,
    1, 3, 5,  7,  9,  3,  4, 4, 5, 6,
    1, 3, 5, 20, 25, 24, 33, 5, 6, 4,
    1, 3, 5, 22, 35, 24, 32, 5, 6, 4,
    1, 3, 5, 20, 28, 34, 23, 5, 6, 4,
    1, 3, 5, 21, 25, 27, 23, 5, 6, 4,
    1, 3, 5,  7,  9,  3,  4, 4, 5, 6,
    1, 3, 5,  7,  9,  3,  4, 4, 5, 6,
    1, 3, 5,  7,  9,  3,  4, 4, 5, 6
]
start_time = time.time()

print(histogram_sort(arr))

end_time = time.time()

print("Execution time for Histogram:", end_time - start_time)