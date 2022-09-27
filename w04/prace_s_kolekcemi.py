import random
import copy
r = list(range(1,12))
l1 = []

# vygenerování bnáhodné posloupnosti ze seznamu
for i in range(len(r)):
    l1.append(random.choice(r))
# totéž jednodušeji (ale bez opakování)
l2 = copy.deepcopy(r)
random.shuffle(l2)
print(l1)
print(l2)
print(r)