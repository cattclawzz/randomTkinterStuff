import tkinter as tk
from math import sin, cos, radians

window = tk.Tk()
canWidth,canHeight = 500, 500
canvas = tk.Canvas(window, width=canWidth, height=canHeight, bg='light grey')
canvas.pack()

rgb = [255,0,0]

def rgbToHex(z):
    return "#" + ''.join([f"{hex(i)[2:].rjust(2, '0')}" for i in z])

def render(z):
    for i in range(360):

        canvas.create_line(canWidth/2, canHeight/2, (sin(radians(i))*z)+(canWidth/2), (cos(radians(i))*z)+(canHeight/2), width = 5, fill= rgbToHex(rgb))

        for j in range(3):
            if i//60 == j*2:
                rgb[(j+1)%3] += 255//60

            if i//60 == (j*2)+1:
                rgb[j] -= 255//60


render(250)
window.mainloop()