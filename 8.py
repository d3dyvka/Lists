a = int(input())
n = list()
c = list()
while a != 0:
    n.append(int(input()))
    a -= 1

for i in range(len(n)):
    if i % 2 != 0:
        c.append(i)

c.reverse()

for i in c:
    n.pop(i)

print(n)