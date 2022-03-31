

def printMap(map):
    print("\n")
    print("  ", end="")
    for x in range(6):   # označenie x osi
        print(x, end=" ")
    print("")
    print("# " * 8)

    #   cyklus na výpis mapy
    for y in range(6):
        print("|", end=" ")
        for x in range(6):
            printed = 1
            for car in map.cars:
                if car.postion[0] == x and car.postion[1] == y:
                    printed = 0
                    print(car.color[0], end=" ")
                elif car.rotation == "h" and car.postion[0] <= x <= car.postion[0] + car.size-1 and car.postion[1] == y:
                    print(car.color[0], end=" ")
                    printed = 0
                elif car.rotation == "v" and car.postion[1] <= y <= car.postion[1] + car.size-1 and car.postion[0] == x:
                    print(car.color[0], end=" ")
                    printed = 0
            if printed:
                print(".", end=" ")
        if map.exitPosition[1] != y:
            print("|", y)
        else:
            print("=", y)

    print("# " * 8)
    print("\n")