from printing import *
from iterative_depthSearch import *
from GUI import *

string = input("Name of the initial state?\n")
try:
    file = open(string, "r")
except:
    print("File doesnt exists")
    exit(1)

map = Map("X", [5, 2], "root", "root", 0, file)     # inicializovanie prého stavu
map.actualMap()     # aktualizovanie mapy pre autá
printMap(map)       # výpis mapy
stack = [map]       # zásobník s nespracovanými stavmi (uzlami)
oldStack = []       # zásobník s mapami spracovaných stavov

start_time = time.time()  # meranie času
solvedMap = iterative_depthSearch(stack, oldStack)  # hladanie riešenia
end_time = time.time()      # koniec merania
moves = []
maps = []
print("Done in %s\n" % (end_time - start_time))

if solvedMap != 0:      # ak si našiel riešenie
    printMap(solvedMap)

    currMap = solvedMap

    while currMap.beforeMap != "root":  # rekurzívne sa vráť a pozbieraj uzly cestou
        moves.append(currMap.lastMove)
        maps.append(currMap.map)
        currMap = currMap.beforeMap

    moves.reverse()     # otoč polia aby riešenia sa vypísalo od začiatku po koniec
    maps.append(currMap.map)
    maps.reverse()

    for i in moves: # vypíš pohyby
        print(i)

    canvas.pack() # vykresli mapy

    drawMap(maps)
    canvas.mainloop()
