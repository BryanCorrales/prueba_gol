# prueba_gol
import time
from tkinter import*
tk =Tk()
posx=200
posy=200
canvas =Canvas(tk,width=400,height=400)

img = PhotoImage(file="gol1.png")
widget = Label(tk, image=img)

def movertri(event):
    global posx
    global posy

    if event.keysym == 'Up':
        canvas.move(1,0,-3)
        posx=posx-3
        if posx<=110:
            widget.pack()
            print("GOL")

        print(posx)
    elif event.keysym == 'Down':
        canvas.move(1,0,3)
        posy=posy+3
        if posy==220:
            print("GOL")
        print(posy)
    elif event.keysym == 'Left':
        canvas.move(1,-3,0)
        posx = posx - 3
        print(posy)
    else:
        canvas.move(1,3,0)
        posy = posy + 3
        print(posy)


canvas.bind_all('<KeyPress-Up>', movertri)
canvas.bind_all('<KeyPress-Down>', movertri)
#canvas.bind_all('<KeyPress-Left>', movertri)
#canvas.bind_all('<KeyPress-Right>', movertri)
canvas.pack()
my_image =PhotoImage(file="pelota.png")
canvas.create_image(50,200,ancho =NW,image= my_image)
my_image1 =PhotoImage(file="arco.png")
canvas.create_image(0,0,ancho =NW,image= my_image1)

tk.mainloop()