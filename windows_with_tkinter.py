import tkinter as tk
from tkinter import ttk

desplegable = ["hola", "Amigo", "Como", "Estas"]
etiqueta = ()

def show_selection():
    """ obtener el valor seleccionado y lo muestra en la etiqueta """
    etiqueta.confing (text=f"Selection: {desplegable.get()}")

# 1. crear la ventana principal

window_principal = tk.Tk()
window_title = ("Ejemplo de BYU-Pathway")

window = ()

window.mainloop()


"""Aun falta mucho por aprender a mejorar este codigo pero bueno aja alli se aprende"""