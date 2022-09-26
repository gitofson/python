import sys

#nevypíše nový řádek:
print("ahoj", end ="")
#volba oddělovče:
print("asdf", "bflm", sep="\n", end="")
#výstup do stderr:
print("ahoj", file = sys.stderr)

# formátování výstupu:
print("cislo:{}, text:{}".format(0.25, "sd"))
print("cislo:{:f}, text:{:s}".format(0.25, "sd"))
print("{m}, {n}, {m}".format(m=0.25, n="sd"))
print("{m:f}, {n:s}, {m:f}".format(m=0.25, n="sd"))
print("{m}, {n}, {m}".format(**{'m':0.25, 'n':3}))

print("{v:_>20}".format(v=2/3)) #__0.6666666666666666
print("{v:_<20}".format(v=2/3)) #__0.6666666666666666
for i in range(-200,200,10):
    print("| {v:>+9} |".format(v=i))