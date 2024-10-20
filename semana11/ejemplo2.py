import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo de Etiqueta")
ventana.geometry("400x200")

label1 = ttk.Label(ventana, text="label1 long long long long\nlong long long long long", 
                   font=("Arial", 10), foreground="#0076a3")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="n")

label2 = ttk.Label(ventana, text="label2", font=("Arial", 30), foreground="black")
imagen = tk.PhotoImage(file="semana11/imagenes/carta.png")
label2.config(image=imagen, compound="bottom")
label2.grid(row=0, column=1, padx=10, pady=10, sticky="n")

ventana.mainloop()