import random
a = list(random.sample(range(100), 10))
n = a.copy()
b = max(a)
c = min(a)
mx = a.index(b)
mn = a.index(c)
a[mx] = c
a[mn] = b

print(n)
print(a)
