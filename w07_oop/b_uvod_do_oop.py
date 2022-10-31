# Termíny třída, typ a datový typ znamenají v Pythonu totéž.
# Jednou z výhod objektového přístupu je možnost specializace třídy pomocí dědění.
# Bázová třída (base class), či nadtřída (super class) jsou předci, podtřída pak
# potomek. Princip, kdy máme v bázové třídě a podtřídě definovanou stejnou metodu
# a Python zavolá správně metodu z podtřídy, nazýváme polymorfismem.

import math

# definice vlastní třídy (zde je bázovou třídou třída object)
class Bod:
    # definice konstruktoru, self je zde odkaz na samotný objekt (resp. instanci třídy)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # definice metody
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)
    
    # přetížení operátoru ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # přetížení samotné reprezentace objektu (vrátí reprezentační formu)
    # za vykřičníkem specifikujeme převod:
    # r - reprezentační forma
    # s - řetězcová forma
    # a - reprezentační forma jen s ASCII znaky
    def __repr__(self):
        return "Auto({0.x!r}, {0.y!r})".format(self)
    
    # přetížení (str) (vrátí řetězcovou formu)
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

# definice podtřídy s bázovou třídou Bod
class Kruh(Bod):
    def __init__(self, x=0, y=0, r=0):
        # volání konstruktoru z nadtřídy
        super().__init__(self, x, y)
        self.r = r

a = Bod()
repr(a)
b = Bod(4, 6)
str(b)
b.distance_from_origin()
a == b, b != a