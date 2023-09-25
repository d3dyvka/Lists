import random
c = 1
b = 0
a = list(random.sample(range(100), 10))
for i in a:
    c *= i
    b += i
print("sum =", b, "umn =", c)