import random
a = list(random.sample(range(100), 10))

for i in a:
    if a.count(i) > 1:
        print(i)
