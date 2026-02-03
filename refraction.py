import tkinter as tk

#Canvas setup
window = tk.Tk()
canWidth,canHeight = 600,400
centerX, centerY = canWidth/2, canHeight/2
canvas = tk.Canvas(window, width=canWidth, height=canHeight, bg='light grey')
canvas.pack()

#Mouse pos detection
mouseX, mouseY = 0, 0
def callback(event):
   global mouseX, mouseY
   mouseX = event.x
   mouseY = event.y
canvas.bind('<Motion>', callback)

def render():
    canvas.delete("all")

    canvas.create_line(0, centerY, canWidth, centerY, width=1, dash = 2) #x axis
    canvas.create_line(centerX, 0, centerX, canHeight, width=1, dash = 2) #y axis
    
    #Draw focus points
    focusDistance = 100
    focus1X = (centerX - focusDistance)
    focus2X = (centerX + focusDistance)
    pointRad = 5
    canvas.create_oval(focus1X - pointRad, centerY - pointRad,
                       focus1X + pointRad, centerY + pointRad,
                       fill = "black"
    )
    canvas.create_oval(focus2X - pointRad, centerY - pointRad,
                       focus2X + pointRad, centerY + pointRad,
                       fill = "black"
    )


    def line(x1, y1, x2, y2, x3):
        canvas.create_line(x1, y1, x3, ((y2-y1)/(x2-x1)) * (x3-x1) + y1, fill = "red")

    def horizLine(x1, y1, x2, y2, x3, x4):
        y = ((y2-y1)/(x2-x1)) * (x3-x1) + y1,
        canvas.create_line(x3, y, x4, y, fill = "red")


    canvas.create_line(mouseX, mouseY, centerX, mouseY, fill = "red")
    line(centerX, mouseY, focus2X, centerY, canWidth)
    #canvas.create_line(centerX, mouseY, focus2X, centerY, fill = "red")

    #canvas.create_line(mouseX, mouseY, focus1X, centerY, fill = "red")
    #canvas.create_line(mouseX, mouseY, centerX, ((centerY-mouseY)/(focus1X-mouseX)) * (centerX-mouseX) + mouseY, fill = "red")
    #canvas.create_line(centerX, ((centerY-mouseY)/(focus1X-mouseX)) * (centerX-mouseX) + mouseY, canWidth, ((centerY-mouseY)/(focus1X-mouseX)) * (centerX-mouseX) + mouseY, fill = "red")

    line(mouseX, mouseY, focus1X, centerY, centerX)
    horizLine(mouseX, mouseY, focus1X, centerY, centerX, canWidth)

    line(mouseX, mouseY, centerX, centerY, canWidth)

    window.after(16, render) #loop func


render()
window.mainloop()