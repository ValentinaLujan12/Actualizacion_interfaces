import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo Text con ttk")

def obtenerText():
    print(texto.get(1.0, 'end')) 
    texto.delete(1.0, 'end') 
    texto.insert(1.0, "Clicked!") 

texto = tk.Text(ventana, width=40, height=10)
texto.pack()

boton = ttk.Button(ventana, text="Click to get text", command=obtenerText)
boton.pack(side="bottom", anchor="w")

ventana.mainloop()
