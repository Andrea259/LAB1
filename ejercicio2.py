import tkinter as tk

def leer_clave():
    def obtener_clave():
        clave = entry.get()
        print(f"Clave ingresada: {clave}")
        window.destroy()

    window = tk.Tk()
    window.title("Clave Secreta")
    window.geometry("300x200")

    label = tk.Label(window, text="Ingrese su clave:")
    label.pack()

    entry = tk.Entry(window, show="*")
    entry.pack()

    boton = tk.Button(window, text="Aceptar", command=obtener_clave)
    boton.pack()

    window.mainloop()

leer_clave()
