import random
b = input()
a = list(random.sample(range(100), 10))
if b in a:
    print(b)
else:
    print("-1")