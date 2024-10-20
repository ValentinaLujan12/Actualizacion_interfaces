import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Mi primer Tkinter")

# Crear un estilo personalizado para el botón
style = ttk.Style()

# Configurar ancho y alto en términos de caracteres
style.configure("TButton", padding=(300, 200))  # padding (ancho, alto)

# Crear el botón usando ttk.Button con el estilo personalizado
button = ttk.Button(
    window,
    text="OK",
    style="TButton"
)

button.pack()
window.mainloop()
