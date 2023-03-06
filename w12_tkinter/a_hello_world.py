# tkinter - standardní Python rozhraní pro Tcl/Tk GUI toolkit.
# spuštěním 
# python -m tkinter 
# se zobrazí jednoduché okno s verzí Tcl/Tk
# Tcl (čti tykl) - dynamický interpretovaný programovací jazyk, často používaný
#                  k zapouzdření skriptů do alpikací napsaných v jazyce C.
# Tk             - Tcl balíček napsaný v C, který přidává možnost manipulace s GUI widgety.
# Ttk            - Themed Tk - novější rodina tk widgetů s propracovanějším vzhledem. 

# https://docs.python.org/3/library/tkinter.html
from tkinter import *
from tkinter import ttk
class Gui:
    def __init__(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        root.mainloop()
if __name__=="__main__":
    gui = Gui()