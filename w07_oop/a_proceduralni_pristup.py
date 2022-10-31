# Představme si situaci, že potřebujeme reprezentovat spoustu kruhů. Nezbytná data
# pro reprezentaci představuje pozice a poloměr (x, y, r). Použijme pro 
# reprezentaci např. n-tici (tuple) pro každý kruh:
circle = (11, 60, 8)
# to přináší ale nevýhody:
# 1. nevíme co jednotlivé elementy n-tice představují
# 2. k elementům se dostaneme pouze přes indexové pozice. Např. voláme funkci
distance = distance_from_origin(*circle[:2])

#Tyto problémy se dá vyřešit pomocí pojmenované n-tice:
import collections
Circle = collections.namedtuple("Circle", "x y radius")
circle = Circle(13,84,9)
distance = distance_from_origin(circle.x, circle.y)

# Stále však zůstává problém validace dat. Např. vždy půjde napsat
circle = circle(33, 56, -5)
