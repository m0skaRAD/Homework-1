
name = "Arkadii "
surname = "Pavliuk"
b = True
f = 12.4


import random

l = [12, True, "test", 35.353, name, random.randint(1, 1000)]
print(l)

l.pop(2)
print(l)

l.remove(True)
print(l)

l.clear()
print(l)

print(name + surname)


if True:
    print("Hello")