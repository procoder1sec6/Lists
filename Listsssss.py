import random
list30 = []
list31 = []
list70 = []
for i in range(10):
    c = random.randint(0,100)
    if c <= 30:
        list30.append(c)
    elif c >= 31 and c <= 69:
        list31.append(c)
    elif c >= 70:
        list70.append(c)
print(list30)
print(list31)
print(list70)