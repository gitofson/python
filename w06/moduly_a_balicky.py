# importování balíčků pomocí příkazu import

filename="moduly_a_balicky.py"

# bezpečný přístup
import os
print (os.path.basename(filename)) 

# riziko kolize názvů s path
import os.path as path
print (path.basename(filename)) 

# riziko kolize názvů s basename
from os.path import basename
print (basename(filename))

# riziko kolize spousty názvů - z daného  modulu importujeme vše
from os.path import *
print (basename(filename)) 

# Balíček založíme tak, že vytvoříme adresář a do něj vytvoříme soubor __init__.py, viz balíček
# Graphics a v něm balíček Vector