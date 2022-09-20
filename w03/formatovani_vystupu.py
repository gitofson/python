import sys

#nevypíše nový řádek:
print("ahoj", end ="")
#volba oddělovče:
print("asdf", "bflm", sep="\n", end="")
#výstup do stderr:
print("ahoj", file = sys.stderr)

# formátování výstupu:
print("{}, {}".format(0.25, "sd"))
print("{m}, {n}, {m}".format(m=0.25, n="sd"))
print("{m}, {n}, {m}".format(**{'m':0.25, 'n':3}))
