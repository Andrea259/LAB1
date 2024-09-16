import tkinter as tk

def leer_cedula():
    def obtener_datos():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        print(f"Cédula: {cedula}, Nombre: {nombre}")
        window.destroy()

    window = tk.Tk()
    window.title("Cédula y Nombre")
    window.geometry("300x200")

    label_cedula = tk.Label(window, text="Ingrese su número de cédula:")
    label_cedula.pack()

    entry_cedula = tk.Entry(window)
    entry_cedula.pack()

    label_nombre = tk.Label(window, text="Ingrese su nombre completo:")
    label_nombre.pack()

    entry_nombre = tk.Entry(window)
    entry_nombre.pack()

    boton = tk.Button(window, text="Aceptar", command=obtener_datos)
    boton.pack()

    window.mainloop()

leer_cedula()