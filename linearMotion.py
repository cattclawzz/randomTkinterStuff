import tkinter as tk

window = tk.Tk()
canWidth,canHeight = 500, 500
canvas = tk.Canvas(window, width=canWidth, height=canHeight, bg='light grey')
canvas.pack()

radius = 25
x = 250
y = 250
velocityY = 0
gravity = 9.8 / 100 #px per 10 ms
floor = canHeight-radius

def drawBall(x, y, radius):
    canvas.create_oval(x-radius,y-radius, x+radius,y+radius, fill = "black")

def render():
    global x, y, velocityY

    canvas.delete("all")

    drawBall(x, y, radius)

    if y <= floor:
        velocityY += gravity
    else:
        velocityY = 0
        y = floor

    y += velocityY

    window.after(10, render)

render()
window.mainloop()