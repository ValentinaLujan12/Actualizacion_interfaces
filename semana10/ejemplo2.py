import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo pack")
ventana.geometry("400x200")

entryTop = ttk.Entry(ventana)
botonLeft = ttk.Button(ventana, text="Left")
entryRight = ttk.Entry(ventana)
botonBottom = ttk.Button(ventana, text="Bottom")
botonCenter = ttk.Button(ventana, text="Center")

entryTop.pack(side="top", fill="x")
botonLeft.pack(side="left", anchor="n", padx=10, pady=10)
entryRight.pack(side="right", anchor="n")
botonBottom.pack(side="bottom", anchor="w")
botonCenter.pack(expand=True, anchor="se")

ventana.mainloop()
