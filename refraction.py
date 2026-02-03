import tkinter as tk

#Canvas setup
window = tk.Tk()
canWidth,canHeight = window.winfo_screenwidth(), window.winfo_screenheight()
centerX, centerY = canWidth/2, canHeight/2
canvas = tk.Canvas(window, width=canWidth, height=canHeight, bg='light grey')
canvas.pack()

#focus points
focusDistance = 50
focus1X = centerX - focusDistance
focus2X = centerX + focusDistance

#Mouse pos detection
mouseX, mouseY = 0, 0
def callback(event):
   global mouseX, mouseY
   if event.x < focus1X:
    mouseX = event.x
    mouseY = event.y
canvas.bind('<Motion>', callback)

def drawPoint(x, y, radius = 5, colour = "black"):
    canvas.create_oval(
        x - radius, y - radius,
        x + radius, y + radius,
        fill = colour
    )

def diagLine(startX, endX, x1, y1, x2, y2, colour = "red", reflection = 0):
    '''
    draw line from startX to endX that passes through points (x1, y1) and (x2, y2)
    y1 = y2-(m)(x2-x1)
    y2 = (m)(x2-x1)+y1
    '''
    m = (y2-y1)/(x2-x1)
    startY = y2 - m * (x2 - startX)
    endY = m * (endX - x1) + y1
    canvas.create_line(startX, startY, endX, endY, fill = colour)

    if reflection != 0:
        horizLine(endX, reflection, endY)


def horizLine(x1, x2, y, colour = "red", reflection = 0, focus = 0):
    canvas.create_line(x1, y, x2, y, fill = colour)
    if reflection != 0:
        diagLine(x2, reflection,  x2, y,  focus, centerY)

def render():
    canvas.delete("all")

    canvas.create_line(0, centerY, canWidth, centerY, width=1, dash = 2) #x axis
    canvas.create_line(centerX, 0, centerX, canHeight, width=1, dash = 2) #y axis
    
    #Draw focus points
    drawPoint(focus1X, centerY)
    drawPoint(focus2X, centerY)
    drawPoint(focus1X - focusDistance, centerY) #2f
    drawPoint(focus2X + focusDistance, centerY)

    #draw lines
    diagLine(0, centerX,  mouseX, mouseY,  focus1X, centerY,  reflection = canWidth)
    horizLine(0, centerX, mouseY, reflection = canWidth, focus = focus2X)
    diagLine(0, canWidth,  mouseX, mouseY,  centerX, centerY)

    window.after(16, render) #loop function


render()
window.mainloop()