import math
from functools import reduce
my_list = [11, 2, 3, 4, 5, ]

result = reduce(lambda x, y: x * y, my_list)

print(result)
