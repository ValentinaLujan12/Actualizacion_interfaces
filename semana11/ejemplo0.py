import tkinter as tk

def evento():
    pass

ventana = tk.Tk()
ventana.title("Tkinter APP")

menuBar = tk.Menu(ventana)
ventana.config(menu=menuBar)

menu1 = tk.Menu(menuBar)
menuBar.add_cascade(label="Menu 1", menu=menu1, command=evento)

menu1.add_command(label="Item 1", command=evento)
menu1.add_separator()
menu1.add_command(label="Item 2", command=evento)

ventana.mainloop()