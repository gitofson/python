# Zdroj: https://www.itnetwork.cz/python/oop/typovy-system-a-type-hints-v-pythonu
# Přestože je Python dynamicky (ale silně) typovaný jazyk, může být výhodné i tak někdy typy uvádět.
# Základní typy v pythonu:
#    int, float, bool, str, None
#
# Explicitní uvedení typu proměnné pomocí operátoru dvojtečka. Takto uvádíme, že proměnná text je typu str:
text: str = "Ahoj světe!"


# Lze uvést i typ návratové hodnoty metod, resp. funkcí:
def generuj_ahoj(jmeno: str) -> str:
    return "Ahoj, " + jmeno + "!"

# Lze to i s kolekcemi, např. list, dict, ...
muj_list: list = [1, 2, 3]
# Ještě lepší je použít knihovnu typing a pomocí hranatých závorek definovat typy uložené v kolekcích:
from typing import List, Set, Dict, Optional, Callable
muj_list: List[int] = [1, 2, 3]
muj_set: Set[int] = set(muj_list)
muj_slovnik: Dict[int, str] = {1: 'jedna', 2: 'dva', 3: 'tri'}
# I složitější konstrukce lze typovat:
muj_slovnik2: Dict[int, List[str]] = {1: ['jedna', 'one'], 2: ['dva', 'two'], 3: ['tri', 'three']}

# Optional
# Typ Optional umožňuje přidat k námi zvolenému typu typ None. Zde využito pro ošetření dělení nulou:
def deleni(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

# Callable
# Možnost volání funkcí pomocí proměnné:
def pridej_jedna(a: int) -> int:
    return a + 1

operace: Callable = pridej_jedna
print(operace(5))  # vypíše 6

# Typové aliasy:
# Výhodnější (a přehlednější) je zavést si typový alias pro častěji používaný komplikovanější typ. Např.:
matice: List[List[int]] = [[1, 2], [3, 4]]
# lze převést, jako:
Matrix = List[List[int]]
matice: Matrix = [[1, 2], [3, 4]]

# Pokud potřebujeme použít typ v momentě, kdy ho parser ještě nezná (např. třídu uvnitř téže třídy),
# měli bychom pro parser v tu chvíli neznámou třídu dát do uvozovek. Příklad pro spojový seznam:
from typing import Optional, Any

class LinkedList:
    def __init__(self):
        self.value: Optional[Any] = Noneprvky
        self.next: Optional["LinkedList"] = None

# Typovaný slovník:

# Klasický slovní v pythonu udržujeme jako klíč:hodnota. Obojí může být libovolného typu.
# Typovaný slovník zde znamená, že klíč bude vždy typu str a typ hodnoty dáme vědět předem
# některou možností níže:

# možná potřeba instalace:
# python3 -m pip install --upgrade typing-extensions
from typing import TypedDict

# 1. možnost
class AdresaDomu(TypedDict):
    mesto: str
    ulice: str
    cislo_domu: int
# 2. možnost
AdresaDomu = TypedDict('AdresaDomu', mesto=str, ulice=str, cislo_domu=int)
# 3. možnost
AdresaDomu = TypedDict('AdresaDomu', {'mesto': str, 'ulice': str, 'cislo_domu': int})
# použití
moje_adresa: AdresaDomu = {'mesto': 'Stare Mesto', 'ulice': 'Nova ulice', 'cislo_domu': 52}



