import tkinter as tk

def datos_mascotas():
    def obtener_datos():
        mascota1 = entry_mascota1.get()
        mascota2 = entry_mascota2.get()
        mascota3 = entry_mascota3.get()
        print(f"Mascota 1: {mascota1}, Mascota 2: {mascota2}, Mascota 3: {mascota3}")
        window.destroy()

    window = tk.Tk()
    window.title("Datos de Mascotas")
    window.geometry("300x300")

    label_mascota1 = tk.Label(window, text="Ingrese los datos de la Mascota 1:")
    label_mascota1.pack()
    entry_mascota1 = tk.Entry(window)
    entry_mascota1.pack()

    label_mascota2 = tk.Label(window, text="Ingrese los datos de la Mascota 2:")
    label_mascota2.pack()
    entry_mascota2 = tk.Entry(window)
    entry_mascota2.pack()

    label_mascota3 = tk.Label(window, text="Ingrese los datos de la Mascota 3:")
    label_mascota3.pack()
    entry_mascota3 = tk.Entry(window)
    entry_mascota3.pack()

    boton = tk.Button(window, text="Aceptar", command=obtener_datos)
    boton.pack()

    window.mainloop()

datos_mascotas()