#
# #!/usr/src/env python3
# expresivní jazyk (vykoná hodně práce při minimálním zápisu programu)
# v pythonu je vše objekt 
# přiřazení:
a = 3 + 5
a = b = c = d = 0
# metoda vars() vypíše všechny použité proměnné v dictionary 
# (asociativním poli)
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

#délka pole
l=[2,1,5,3,6,9]
len(l)
#konkrétní index
l[4]
#slice - od
l[1:]
#slice - od do, poslední index tam nepatří
l[1:3]
#konkrétní index od zadu
l[-4]
l[-5:]
l[:-1]
l[:-5]
#metody pro práci s polem
# výmaz konkrétního prvku
l.remove()
# seřazení vzestupně
l.sort()
# otočení
l.reverse()
# vyndání posledního
l.pop()
# přidání dalšího na poslední místo
l.append()
# přidání dalšího na konkrétní pozici
l.insert(0,12)
# all = všechny hodnoty dávají True
all(l)
# any = alespoň jedna hodnota dává False
h=[0,0,0,0,0,None, ""] 
any(h)
# součet řady
sum(l)
sum(list(range(1,100)))

# filtrace - z range(20) beru jen ty, co vyhovují podmínce x**2 < 20
list(filter (lambda x: x**2 < 20, range(20)))

print("hello")