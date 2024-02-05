import sys
sys.path.insert(0, 'IMGS')
sys.path.insert(0, 'LIBS')

import math
from tkinter import *
from graphics import *

win = GraphWin("eSTUDO de cores", 640, 720)
win2 = GraphWin("eSTUDO de cores", 640, 720)
im = PhotoImage(file ='Sonic2 (1).png')
im2 = Image(Point(300, 350), 'Sonic2 (1).png')


for i in range (0, 150):
    for j in range (0, 197):
        r, g, b = im.get(i, j)
        px = int(i  + 50)
        py = int(j + 50)

        media = int ((r+g+b)/3)
        colorval = "#%02x%02x%02x" % (media, media, media)

        
        
        win.create_rectangle(
            px, py, px, py, width = 0, fill=(colorval))


im2.draw(win)
win.mainloop()
win.close()
