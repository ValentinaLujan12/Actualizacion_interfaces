import tkinter as tk
from tkinter import ttk

vent = tk.Tk()
vent.title("Ejemplo de place")
vent.geometry("400x200")

# Configurar el estilo para los Entry
style = ttk.Style()
style.theme_use('clam')  # Cambiar a un tema que permite personalización
style.configure("Pink.TEntry", fieldbackground="pink")

lbl1 = ttk.Label(vent, text="Primer número", background="yellow", anchor="center")
lbl1.place(relx=0.03, rely=0.04, relwidth=0.23, relheight=0.1)
txt1 = ttk.Entry(vent, style="Pink.TEntry")  # Aplicar el estilo personalizado
txt1.place(relx=0.3, rely=0.04, relwidth=0.22, relheight=0.1)

lbl2 = ttk.Label(vent, text="Segundo número", background="yellow", anchor="center")
lbl2.place(relx=0.03, rely=0.17, relwidth=0.23, relheight=0.1)
txt2 = ttk.Entry(vent, style="Pink.TEntry")  # Aplicar el estilo personalizado
txt2.place(relx=0.3, rely=0.17, relwidth=0.22, relheight=0.1)

btn1 = ttk.Button(vent, text="Sumar")
btn1.place(relx=0.55, rely=0.17, relwidth=0.25, relheight=0.1)
btn1.configure(padding=(5, 0.5))  # Padding (horizontal, vertical) para ubicar el texto del botón

vent.mainloop()
