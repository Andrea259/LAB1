
import tkinter as tk

def most_datos():
    ventana = tk.Tk()
    ventana.title("Datos Personales")
    ventana.geometry("300x200")

    nombre = "Andrea Ramos"
    edad = "19 años"

    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    label_nombre = tk.Label(frame, text=nombre, font=("Arial Black", 14))
    label_nombre.pack()

    label_edad = tk.Label(frame, text=edad, font=("Arial Black", 14))
    label_edad.pack()

    ventana.mainloop()

most_datos()