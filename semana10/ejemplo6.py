import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo Frames")
ventana.geometry("300x200")

# Crear un estilo para los frames
style = ttk.Style()

# Definir estilos para los frames
style.configure("Red.TFrame", background="red")
style.configure("Blue.TFrame", background="blue")
style.configure("Green.TFrame", background="green")
style.configure("Orange.TFrame", background="orange")

frame1 = ttk.Frame(ventana, height=40, style="Red.TFrame")
frame1.pack(fill='x')

frame11 = ttk.Frame(frame1, style="Blue.TFrame")
frame11.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="center")

frame2 = ttk.Frame(ventana, width=50, style="Green.TFrame")
frame2.pack(side='right', fill='y')

frame12 = ttk.Frame(frame2, style="Orange.TFrame")
frame12.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.5, anchor="s")

cinco = ttk.Button(frame11, text="Cinco")
cinco.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="e")

uno = ttk.Button(frame11, text="1")
uno.place(relx=0.6, rely=0.5, relwidth=0.4, relheight=1, anchor="w")

dos = ttk.Button(frame12, text="Dos")
dos.pack(padx=1, pady=1)

tres = ttk.Button(frame12, text="Tres")
tres.pack(padx=1, pady=1)

cuatro = ttk.Button(frame12, text="Cuatro")
cuatro.pack(padx=1, pady=1)

ventana.mainloop()

