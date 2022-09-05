#!/usr/src/env python3
# expresivní jazyk (vykoná hodně práce při minimálním zápisu programu)
# přiřazení:
a = 3+5
a = b = c = d = 0
a,b = 3,4
a,i = b,a
dir()
#zabudované metody v pythonu
dir(__builtins__)

#metody dané třídy:
dir("ahoj")
#nápověda k metodě:
help(tuple)
# n-tice (tuples) - read only pole
a=(1,2,3)
a[0] = 'b'
# list - pole
l=[1,2,3]
l[0] = 'b'
# identifikace typu
type(l)

#čitelnější výpis
import pprint
pprint.pprint(dir("asdf"))

#identita typu:
id("ahoj")
#identita - záleží, co máme uvnitř proměnné
hash("ahoj")

#mocniny
pow(2,10)
2**10
#modulo
pow(3,3,20)
3**3%20

#převody mezi číselnými soustavami
int('1001',2)
hex(int("11001",2))
oct(int("11001",2))
bin(int("11001",2))
int("beef",16)

#hodnota None
#False bool(None) = bool(0) = bool("")



print("hello")