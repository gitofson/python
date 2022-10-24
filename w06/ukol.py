# Napište progam vypisující obsah adresáře jako příkaz dir ve windows nebo ls v Unixu.
# Výhoda vytvoření našeho vlastního program spočívá v tom, že do něj můžeme zabudovat preferované výchozí chování
# a hodnoty a používat na všech platformách stejný program bez toho, abychom si museli pamatovat odlišnosti
# mezi příkazy dir a ls
#
#
# Rozhraní: Usage
# Usage ls.py [volby] [cesta1 [cesta2 [... cesta3]]]
# (cesty jsou volitelné, nejsou-li zadány použije se aktuální adresář)
# Options:
#   -h, --help
#   -H, --hidden (skryté)
#   -m, --modified (zobrazí čas poslední modifikace)
#   -o ORDER, --order=ORDER (seřadí výstup podle ('name' {výchozí}, 'n', 'modified', 'm', 'size', 's'))
#   -r, --recursive (sestupuje rekurzivně do pod-adresářů)
#   -s, --sizes (zobrazí velikosti souborů)
#
#
#
#
#
