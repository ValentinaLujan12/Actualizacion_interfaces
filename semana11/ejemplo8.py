import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Mouse Events")
ventana.geometry("400x200")

def informacionEvento(event):
    print("Tipo de evento:",event.type,"\n","X : Y - ",event.x,":",event.y,"\n",
    "XVentana : YVentana -",event.x_root,":",event.y_root,"\n","num:",event.num,
    "\nWidget:",event.widget,"\n")

etiqueta = ttk.Label(ventana, text="Eventos del ratón")
etiqueta.grid(row=0, column=0)

bandera = ttk.Label(ventana)
imagen = tk.PhotoImage(file="semana11/imagenes/Colombia.png")
bandera.config(image=imagen)
bandera.bind("<Button-1>", informacionEvento)
bandera.bind("<Enter>", informacionEvento)
bandera.bind("<Leave>", informacionEvento)
bandera.bind("<B1-Motion>", informacionEvento)
bandera.bind("<ButtonRelease-1>", informacionEvento)

bandera.grid(row=0, column=1)

ventana.mainloop()