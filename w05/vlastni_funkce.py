# Rozbalení argumentů parametrů
from os import system

import sys
# poziční argumenty - lze pomocí operátoru hvězda (*) použít jako
# funkci s proměnným počtem argumentů
# klíčované argumenty - uvádíme za pozičními, mají vždy název (klíč).
# zde "sep", "end" a "file"
def mujprint(*args, sep="\n", end="", file=sys.stdout):
    print(args, sep=sep, end=end, file=file)

mujprint("ahoj", "ahoj2")