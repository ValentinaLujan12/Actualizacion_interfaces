import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo grid")
ventana.geometry("400x200")

frame = ttk.Frame(ventana, width=200, height=100)
frame.pack(expand=True)

label1 = ttk.Label(frame, text="Email")
entry1 = ttk.Entry(frame)
label2 = ttk.Label(frame, text="Password")
entry2 = ttk.Entry(frame)
boton1 = ttk.Button(frame, text="Submit")
boton2 = ttk.Button(frame, text="Clear")

label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
boton1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
boton2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

ventana.mainloop()
