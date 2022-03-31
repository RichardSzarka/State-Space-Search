import time
import tkinter

canvas = tkinter.Canvas(width=640, height=800)
canvas.pack()

colors = {
    "R": "Red",
    "G": "Green",
    "B": "Blue",
    "C": "Cyan",
    "P": "Pink",
    "Y": "Yellow",
    "O": "Orange",
    "S": "Silver",
    "N": "Navy",
    "M": "Magenta",
    "K": "Khaki",
    "L": "Lime",
    "F": "Fuchsia",
    ".": "White"
}

def drawMap(maps):
    #   vykreslenie máp podla prechadzania stavov máp
    for i in range(len(maps)):
        for row in range(len(maps[i])):
            for cell in range(len(maps[i][row])):
                canvas.create_rectangle(20+cell*100,20+row*100,20+cell*100+100,20+row*100+100,fill=colors[maps[i][row][cell]])
                if cell == 5 and row == 2:
                    canvas.create_rectangle(20+cell * 100+100, 20+row * 100, 20+cell * 100 + 110, 20+row * 100+100,
                                            fill="Black")
        canvas.update()
        time.sleep(1)

