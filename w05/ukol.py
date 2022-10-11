# Napište interaktivní program, který udržuje seznam řetězců v souborech.
# Po spuštěí programu by program měl vytvořit seznam všech souborů v aktuálním adresáři,
# které mají příponu .lst. Použijte os.listdir(".") pro získání
# všech souborů a odfiltrujte ty, které nemají příponu .lst. Pokud žádné takové soubory neexistují,
# program by měl vyzvat uživatele k zadání názvu souboru a připojit
# příponu .lst, pokud ji uživatel nezadá. Pokud existují, měly by bát k dispozici jako číslovaný
# seznam a uživatel by měl být vyzván k zadání čísla vybraného souboru P, resp. zadat 0, pokud
# chce vytvořit nový soubor.

# Pokud byl zvolen existující soubor, měly by se načíst jeho prvky.
# Pokud je prázdný, nebo pokud byl zadán nový soubor, program by měl vypsat:
# "V seznamu nejsou žádné prvky"

# Pokud nejsou v seznamu prvky, měly by být nabídnuty možnosti "Přidat" a "Konec".
# Pokud jsou v seznamu prvky, měly by být nabídnuty možnosti "Přidat", "Vymazat" a "Uložit".

# Snažte se o co nejkratší funkci main() (cca 30 řádků) a umístěte do ní hlavní cyklus programu. 
# Dále napište:
#     - funkci pro získání nového, nebo stávajícího názvu souboru,
#     - funkci pro přeložení možností uživateli a pro získání jeho volby,
#     - funkci pro přidání prvku,
#     - funkci pro výmaz prvku,
#     - funkci pro vypsání seznamu prvků, či názvů souborů,
#     - funkci pro načtení seznamu,
#     - funkci pro uložení seznamu.

# Prvky udržujte v abecedním pořadí nezávislém na velikosti písmen. Kontrolujte,
# zda je seznam špinavý (tj. změněn bez uložení). Možnost uložení nabídněte pouze tehdy,
# pokud je seznam špinavý.

# Nápověda: řešte implementací následujících funkcí:
# choose_file(): zjistí počet ".lst" souborů v aktuální adresáři, pokud je nulový, zadá
#               výzvu k zadání souboru. Pokud není nulový, zadá výzvu k výběru souboru.
#               Vrací filename, items

# print_list(items): vypíše položky

# get_choice(items, dirty): vypíše volbu, co dělat s položkami
#               Vrací choice 

# add_item(items, dirty): zeptá se jakou položku má do seznamu přidat a přidá jí tam.
#               Vrací dirty

# delete_item(item, dirty): zeptá se jakou položku má ze seznamu vymazat a pokud tam je,
#                           vymaže jí.
#               Vrací dirty

# load_list(filename): otevře soubor a načte položky.
#               Vrací items

# save_list(filename, items): uloží položky do souboru filename


