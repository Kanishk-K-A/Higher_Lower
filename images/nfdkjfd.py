import random

d = {1:1, 2:1, 'A':5, 'K':6}
dl = list(d.keys())
print(type(dl))
for i in range(5):
    print(random.choice(dl))