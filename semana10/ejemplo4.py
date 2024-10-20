import tkinter as tk
from tkinter import ttk

vent = tk.Tk()
vent.title("Ejemplo place")
vent.geometry("400x200")

# Configurar el estilo para los Entry
style = ttk.Style()
style.theme_use('clam')  # Cambiar a un tema que permite personalización
style.configure("Pink.TEntry", fieldbackground="pink")

lblNum1 = ttk.Label(vent, text="Primer Número:", background="yellow", anchor="center")
lblNum1.place(x=10, y=10, width=100, height=30)
txtNum1 = ttk.Entry(vent, style="Pink.TEntry") 
txtNum1.place(x=120, y=10, width=100, height=30)

lblNum2 = ttk.Label(vent, text="Segundo Número:", background="yellow", anchor="center")
lblNum2.place(x=10, y=50, width=100, height=30)
txtNum2 = ttk.Entry(vent, style="Pink.TEntry") 
txtNum2.place(x=120, y=50, width=100, height=30)

btn1 = ttk.Button(vent, text="Sumar")
btn1.place(x=230, y=50, width=80, height=30)

vent.mainloop()
