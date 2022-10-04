d = []
try:
    x = d[5]
except LookupError:
    print("prvek v seznamu nenalezen")
except KeyError: # tahle výjimka nikdy nenastane
    print("neplatný klíč")
    
try:
    x = d[k / n]
except:
    print("něco se stalo")

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