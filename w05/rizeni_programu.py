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
#    if a == 8:
#        break
# else se vykoná pokud se cyklus while ukončí standartním způsobem (např. nedojde k break),
# nepovinné
else:
    print("else: a:{}", a)
# cyklus for
for i in range(5):
    print(i)
else:
    print("ukončeno, i= {}", i)
    
# Příklad použití výjimek. funkce list_find(lst, target) vrátí index prvku target v seznamu
# lst. Při nenalezení prvku vrátí -1
def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines

# Vyvolání výjimky:
# raise výjimka(argumenty)

# Definice vlastní výjimky:
# class názevVýjimky(bázováVýjika):
#    pass
        