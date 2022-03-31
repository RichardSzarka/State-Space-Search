from dictionaries import *

#   trieda auto
class Car:

    # inicializácia auta
    def __init__(self, color, size, position, rotation):
        self.color = color # farba daného auta
        self.size = size # veľkosť auta
        self.postion = position # pozícia auta
        self.rotation = rotation # rotácia auta
        self.map = [] # mapa áut

    # pohyb dopredu
    def forward(self):
        if self.rotation == "h":    # ak je horizontálne
            if self.postion[0] + self.size - 1 < 5:     # ak nevyjde z mapy
                if self.map[self.postion[1]][self.postion[0]+self.size] == ".":     # ak by nenarazil do auta
                    self.postion[0] += 1
                    return 1    # pohni sa a vrát 1 (pohyb)
                else:
                    return 0    # ináč vráť 0 - nemôže sa pohnúť
            else:
                return 0
        else:   # ak je vertikálne
            if self.postion[1] + self.size - 1 < 5:     # ak nevyjde z mapy
                if self.map[self.postion[1] + self.size][self.postion[0]] == ".":    # ak by nenarazil do auta
                    self.postion[1] += 1
                    return 1        # pohni sa a vrát 1 (pohyb)
                else:
                    return 0        # ináč vráť 0 - nemôže sa pohnúť
            else:
                return 0

    # pohyb dozadu je na ten istý princíp ako pohyb dopredu
    def backward(self):
        if self.rotation == "h":    # ak je horizontálne
            if self.postion[0] > 0:      # ak nevyjde z mapy
                if self.map[self.postion[1]][self.postion[0] - 1] == ".":        # ak by nenarazil do auta
                    self.postion[0] -= 1
                    return 1     # pohni sa a vrát 1 (pohyb)
                else:
                    return 0      # ináč vráť 0 - nemôže sa pohnúť
            else:
                return 0
        else:       # ak je vertikálne
            if self.postion[1] > 0:     # ak nevyjde z mapy
                if self.map[self.postion[1] - 1][self.postion[0]] == ".":        # ak by nenarazil do auta
                    self.postion[1] -= 1
                    return 1    # pohni sa a vrát 1 (pohyb)
                else:
                    return 0    # ináč vráť 0 - nemôže sa pohnúť
            else:
                return 0

#   trieda pre mapy
class Map:

    def __init__(self, cars, exitPosition, beforeMap, lastMove, depth, file):
        self.cars = cars # pole áut
        self.exitPosition = exitPosition # pozícia na výstup
        self.beforeMap = beforeMap # rodič
        self.lastMove = lastMove # aký bol krok z rodičia na vytvorenie tohoto stavu
        self.depth = depth # hĺbka stavu
        self.map = [] # pole vykreslenej mapy

        # ak sú autá X tak sa jedná o inicializáciu prvej mapy, inicializuj autá zo súboru
        if self.cars == "X":
            self.cars = []    # otvor súbor s pozíciou áut
            lines = file.readlines()
            counter = 0
            for i in lines:     # každý riadok je 1 stav auta, inicializuj
                parameters = i.strip("\n").split(",")
                self.cars.append(Car(CarColorList[counter+1], int(parameters[0]), [int(parameters[1]), int(parameters[2])], parameters[3]))
                counter += 1

    def actualMap(self):    # aktualizuj mapu ak sa pohli autá a rozpošli všetkým autám aktuálnu pozíciu v uzle
        self.map = []
        for y in range(6):
            vector = ""
            for x in range(6):
                printed = 1
                for car in self.cars:
                    if car.postion[0] == x and car.postion[1] == y:
                        printed = 0
                        vector += car.color[0]
                    elif car.rotation == "h" and car.postion[0] <= x <= car.postion[0] + car.size - 1 and car.postion[
                        1] == y:
                        vector += car.color[0]
                        printed = 0
                    elif car.rotation == "v" and car.postion[1] <= y <= car.postion[1] + car.size - 1 and car.postion[
                        0] == x:
                        vector += car.color[0]
                        printed = 0
                if printed:
                    vector += "."
            self.map.append(vector)

            for i in range(len(self.cars)):
                self.cars[i].map = self.map


