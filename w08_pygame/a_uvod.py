# PyGame [https://www.pygame.org] - množina Pythom modulů, která byla navržena pro tvorbu videoher a multimediálních aplikací
# v jazyce Python. Je postavena na známé knihovně SDL (Simple DirectMedia Layer [http://www.libsdl.org]). 
# Jednoduchá, přenositelná, často používaná, nepotřebuje GUI pro návrh her, podporovaná vývojáři, expresivní
# (stačí malé množství kódu), modulární.
# instalace:
# py -m pip install -U pygame --user
# případně
# pip install pygame --pre
# test:
# python3 -m pygame.examples.aliens

# herní smyčka v PyGame  (game loop) - místo, kde se odehrává zpracování událostí, herní logika a vykreslování na obrazovku :
while True:
    events()        # zpracování událostí (z klávesnice, myši, ...)
    loop()          # výpočet změn ve hře (např. pohyp spritu)
    render()        # samotné vykreslení scény

