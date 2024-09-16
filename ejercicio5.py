import tkinter as tk

def datos_personales():
    def obtener_datos():
        datos = [entry.get() for entry in entradas]
        print(f"Datos personales: {datos}")
        window.destroy()

    window = tk.Tk()
    window.title("Datos de una Persona")
    window.geometry("400x500")

    etiquetas = [
        "Nombre", "Apellido", "Edad", "Género", "Dirección", 
        "Teléfono", "Email", "Ocupación", "Nacionalidad", "Estado civil"
    ]

    entradas = []
    for etiqueta in etiquetas:
        label = tk.Label(window, text=f"Ingrese {etiqueta}:")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()
        entradas.append(entry)

    boton = tk.Button(window, text="Aceptar", command=obtener_datos)
    boton.pack()

    window.mainloop()

datos_personales()