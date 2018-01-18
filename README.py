# prueba_gol
import time
from tkinter import*
tk =Tk()
canvas =Canvas(tk,width=400,height=200)
canvas1 =Canvas(tk,width=400,height=200)
canvas2 =Canvas(tk,width=400,height=200)





def movertri(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-3)
        canvas1.move(1,0,-3)
        canvas2.move(1,0,-3)
    elif event.keysym == 'Down':
        canvas.move(1,0,3)
        canvas1.move(1,0,3)
        canvas2.move(1,0,3)
    elif event.keysym == 'Left':
        canvas.move(1,-3,0)
        canvas1.move(1,-3,0)
        canvas2.move(1,-3,0)
    else:
        canvas.move(1,3,0)
        canvas1.move(1,3,0)
        canvas2.move(1,3,0)
canvas.bind_all('<KeyPress-Up>', movertri)
canvas.bind_all('<KeyPress-Down>', movertri)
canvas.bind_all('<KeyPress-Left>', movertri)
canvas.bind_all('<KeyPress-Right>', movertri)

canvas =Canvas(tk,width=400,height=400)
canvas.pack()
my_image =PhotoImage(file="pelota.png")
canvas.create_image(30,10,ancho =NW,image= my_image)
my_image1 =PhotoImage(file="arco.png")
canvas.create_image(0,0,ancho =NW,image= my_image1)
tk.mainloop()


tk = Tk()





