# větvení:
a = 1
if a == 1:
    print("jedna")
elif a == 2:
    print("dva")
else:
    print("ani jedna ani dva")

# analogie ternárního operátoru:
b = 10 if a == 1 else 20
print(b)

#cykly:
while(a < 10):
    a += 2
    if a == 4:
        continue
    print(a)
    if a > 8:
        break
# else se vykoná pokud se cyklus while ukončí standartním způsobem (např. nedojde k break),
# nepovinné
else:
    print("else: a:{}".format(a))
# cyklus for
for i in range(5):
    print(i)
    if(i==3):
        break
else:
    print("ukončeno, i= {}".format(i))
    

        