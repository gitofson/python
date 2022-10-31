# Python obsahuje mnoho speciálních metod (např. pro porovnávání objektů)
# __lt__(self, other)           x < y
# __le__(self, other)           x <= y    
# __eq__(self, other)           x == y
# __ne__(self, other)           x != y
# __ge__(self, other)           x <= y
# __gt__(self, other)           x > y

# __bool__(self)                bool(x)     Vrací pravdivostní hodnotu pro objekt x
# __format__(self, format)      "{0}".format(x)
# __hash__(self)                hash(x)     Je-li uvedena, pak lze x použít jako klíč slovníku, nebo uchovat v množině.
# __init__(self, args)          x=X(args)
# __new__(cls, args)            x=X(args)
# __repr__(self)                repr(x)   
# __repr__(self)                ascii(x)
# __str__(self)                 str()       Reprezentace objektu srozumitelná pro člověka.
# __abs__(self)                 abs()
# __float__(self)               float()
# __index__(self)               bin(x) oct(x) hex(x)
# __pos__(self)                 +x
# __add__(self, other)          x+y
# __iadd__(self, other)         x+=y
# __radd__(self, other)         y+x
# __mul__(self, other)          x*y
# __imul__(self, other)         x*=y
# __rmul__(self, other)         y*x
# __floordiv__(self, other)     x//y
# __ifloordiv__(self, other)    x//=y
# __rflordiv__(self, other)     y//x
# __complex__(self)             complex(x)
# __int__(self)                 int(x)
# __round__(self, number)       round(x, number)
# __neg__(self)                 -x
# __sub__(self, other)          x-y
# __isub__(self, other)         x-=y
# __rsub__(self, other)         y-x
# __mod__(self, other)          x%y
# __imod__(self, other)         x%=y
# __rmod__(self, other)         y%x
# __truediv__(self, other)      x/y
# __itruediv__(self, other)     x/=y
# __rtruediv__(self, other)     y/x

