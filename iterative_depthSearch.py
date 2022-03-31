import sys
from classes import *
from copy import deepcopy


# cyklické hladanie do hĺbky
def iterative_depthSearch(stack, oldstack):
    depth_treshold = 2  # hĺbka do akej sa má vnoriť - hranica vnorenia sa

    while True:
        sys.stdout.write("\r" + str(len(stack)) + " unprocessed states " + " | " + str(len(oldstack)) + " processed states " + " | " + str(depth_treshold) + " depth ")
        if len(stack) == 0:  # ak dĺžka zásobníka stack je 0 tak neexistujú nové neprebádané stavy - vrát neúspech
            print(" no solution")
            return 0

        currMap = stack[0]  # vyber hned 1. čo máš na zásobníku
        found = True
        if currMap.depth == depth_treshold:  # ak to čo si vybral už je na hranici vnorenej hĺbky nájdi stav ktorý nie
            # je ešte na hranici
            for i in range(len(stack)):
                if stack[i].depth < depth_treshold:  # ak existuje stav ktorý je v hĺbke menšej ako je hranica vnorenia sa
                    stack[i], stack[0] = stack[0], stack[i]  # daj nájdený na 1. miesto v zásobníku
                    found = False
            if found:   # ak si taký stav nenašiel a stále nemáme riešenie, prhĺb sa
                depth_treshold += 2

        currMap = stack.pop(0)      # priraď stav a zároveň ho odstráň zo zásobníka

        if currMap.map in oldstack:     # ak stav uzla ktorý sme vybrali už sa rovnal stavu prebádaných uzlov, preskoč
            # tento cyklus
            continue

        #   ak je červené auto na správnej pozícii vrát tento uzol - úspech
        if currMap.cars[0].postion[0] + currMap.cars[0].size - 1 == 5 and currMap.cars[0].postion[1] == 2:
            return currMap

        #   cyklus kde sa skúsi s každým autom pohnúť dopredu a dozadu
        for i in range(len(currMap.cars)):
            #   pomocné mapy aby som nezmenil stav aktuálneho uzla
            helpMap = Map(deepcopy(currMap.cars), [5, 2], currMap.beforeMap, currMap.lastMove, currMap.depth, None)
            helpMap.actualMap()

            helpMap2 = Map(deepcopy(currMap.cars), [5, 2], currMap.beforeMap, currMap.lastMove, currMap.depth, None)
            helpMap2.actualMap()

            #   ak sa vieš pohnuť dopredu s daným autom vytvor nový uzol a kde si sa pohol a vlož ho na zásobník
            if helpMap.cars[i].forward():
                newMap = Map(deepcopy(helpMap.cars), [5, 2], currMap, helpMap.cars[i].color + " moves forward",
                             currMap.depth + 1, None)
                newMap.actualMap()
                stack.insert(0, newMap)
            #   ak sa vieš pohnuť dozadu s daným autom vytvor nový uzol a kde si sa pohol a vlož ho na zásobník
            if helpMap2.cars[i].backward():
                newMap2 = Map(deepcopy(helpMap2.cars), [5, 2], currMap,helpMap2.cars[i].color + " moves backward",
                              currMap.depth + 1, None)
                newMap2.actualMap()
                stack.insert(0, newMap2)

        #   ak si uplne spracoval jeho stav, priraď jeho mapu do zásobníka spracovaných znakov
        oldstack.append(currMap.map)
