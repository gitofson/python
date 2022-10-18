import os, sys

def main():
    dirty = False
    #items = []
    filename, items = chose_file()
    while True:
        print_list(items)
        choice = get_choice(items, dirty)
        if choice == 1:
            dirty = add_item(items, dirty)
        elif choice == 3:
            dirty = delete_item(items, dirty)
        elif choice == 2:
            if dirty: 
                save_items(filename, items)
        else: 
            break
    
    
    
# choose_file(): zjistí počet ".lst" souborů v aktuální adresáři, pokud je nulový, zadá
#               výzvu k zadání souboru. Pokud není nulový, zadá výzvu k výběru souboru.
#               Vrací filename, items
def chose_file():
    items = []
    file_list = list(filter(lambda x:x.endswith(".lst"), os.listdir(".")))
    if len(file_list) == 0:
        filename = get_string("zadej název souboru")
        if filename.endswith(".lst"):
            pass
        else:
            filename += ".lst"
        save_items(filename, [])
    else:
        cnt = 0
        for fn in file_list:
            print("{:d} - {:s}".format(cnt, fn))
            cnt += 1
        selected_idx = get_integer("Zvolte index souboru")
        filename = file_list[selected_idx]
        items = load_list(filename)
    return filename, items

# load_list(filename): otevře soubor a načte položky.
#               Vrací items
def load_list(filename):
    try:
        fn = open(filename, "r")
        items = fn.readline().split(" ")
    except:
        print("Chyba při čtení souboru {}".format(filename), file = sys.stderr)
    finally:
        fn.close()
    return items

#    fn.read
# save_list(filename, items): uloží položky do souboru filename
def save_items(filename, items):
    try:
        fn = open(filename, "w")
        fn.writelines(" ".join(items))
    except:
        print("Chyba při zápisu do souboru {}".format(filename), file = sys.stderr)
    finally:
        fn.close()


def add_item(items, dirty):
    polozka = get_string("Zadej polozku:")
    if polozka in items:
        return dirty
    else:
        items.append(polozka)
        return True

    # get_choice(items, dirty): vypíše volbu, co dělat s položkami
    #               Vrací choice
def get_choice(items, dirty):
    if items:
        vyber = get_integer("Vyber položku:\n" +
                            "0 - konec \n"  +
                            "1 - add položku \n"  + 
                            ("2 - uložit \n" if dirty else "\n") +
                            "3 - vymazat položku \n"
                            )
        return vyber

    else:
        vyber = get_integer('Vyber položku:\n'+
                            '0 - konec \n'+
                            '1 - add položku \n'+
                            ('2 - uložit \n' if dirty else '\n'))
        return vyber

# print_list(items): vypíše položky  
def print_list(items):
    for item in items: 
        print(item, end=", ") 
    print()    

def delete_item(items, dirty):
    polozka = get_string("Zadej polozku")
    if polozka in items:
        items.remove(polozka)
        return True
    else:
        return dirty
def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                        "{minimum_length} and at most "
                        "{maximum_length} characters".format(
                        **locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                        "and {maximum} inclusive{0}".format(
                        " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))
main()
