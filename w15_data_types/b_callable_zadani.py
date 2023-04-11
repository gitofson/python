# Nadefinujte si 4 metody (sčítání, odečítání, násobení a dělení) dvou čísel typu
# float.
# Pomocí třídy Callable proveďte vlastní operaci na základě náhodného čísla.
# U všeho uveďte typ.

from typing import Callable
import random
cislo: int = random.randint(0, 3)

def scitani(a: float, b: float) -> float:
    print("Sčítání")
    return a + b
def odecitani(a: float, b: float) -> float:
    print("Odečítání")
    return a - b
def nasobeni(a: float, b: float) -> float:
    print("Násobení")
    return a * b
def deleni(a: float, b: float) -> float:
    print("Dělení")
    return a / b
operace: Callable = None
if cislo == 0:
    operace = scitani
elif cislo == 1:
    operace = odecitani
elif cislo == 2:
    operace = nasobeni
elif cislo == 3:
    operace = deleni

print(operace(5.88526, 2.4562))
