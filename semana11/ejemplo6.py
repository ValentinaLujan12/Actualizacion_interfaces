import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Creación de alertas")
ventana.geometry("400x200")

def confirmacion():
    opcion = messagebox.askokcancel("Diálogo de confirmación", "Ventana de diálogo de confirmación")
    if opcion:
        messagebox.showinfo("Diálogo de confirmación", "Has pulsado Aceptar")

def error():
    messagebox.showerror("Error", "Ventana de diálogo de error")

boton = ttk.Button(ventana, text="Alerta de confirmación", command=confirmacion)
boton.pack(anchor="w", padx=10, pady=10)

boton2 = ttk.Button(ventana, text="Alerta de error", command=error)
boton2.pack(anchor="w", padx=10, pady=10)

ventana.mainloop()
