#Este programa permite al usuario seleccionar su género usando Radiobuttons y elegir su país usando un Combobox.
# Luego, al presionar un botón, el programa mostrará los datos seleccionados.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear una clase para manejar la ventana
class FormularioUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Usuario")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("400x300")
        
        # Crear un frame para organizar los widgets
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Etiqueta para el nombre
        self.nombre_label = tk.Label(frame, text="Nombre Completo:")
        self.nombre_label.grid(row=0, column=0, padx=10, pady=10)

        # Entrada para el nombre
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta para el género
        self.genero_label = tk.Label(frame, text="Género:")
        self.genero_label.grid(row=1, column=0, padx=10, pady=10)

        # Variable para almacenar el género seleccionado
        self.genero = tk.StringVar(value="Masculino")

        # Radiobuttons para elegir el género
        self.genero_masculino = tk.Radiobutton(frame, text="Masculino", variable=self.genero, value="Masculino")
        self.genero_masculino.grid(row=1, column=1, padx=10, pady=5)

        self.genero_femenino = tk.Radiobutton(frame, text="Femenino", variable=self.genero, value="Femenino")
        self.genero_femenino.grid(row=1, column=2, padx=10, pady=5)

        # Etiqueta para el país
        self.pais_label = tk.Label(frame, text="País:")
        self.pais_label.grid(row=2, column=0, padx=10, pady=10)

        # Combobox para seleccionar el país
        self.pais = ttk.Combobox(frame, values=["Argentina", "México", "España", "Colombia", "Chile"])
        self.pais.grid(row=2, column=1, padx=10, pady=10)
        self.pais.set("Selecciona un país")

        # Botón para enviar los datos
        self.enviar_button = tk.Button(self.root, text="Enviar", command=self.mostrar_datos)
        self.enviar_button.pack(pady=20)

    # Función que se ejecuta al hacer clic en el botón "Enviar"
    def mostrar_datos(self):
        nombre = self.nombre_entry.get()
        genero = self.genero.get()
        pais = self.pais.get()

        # Mostrar los datos en un mensaje
        messagebox.showinfo("Datos del Usuario", f"Nombre: {nombre}\nGénero: {genero}\nPaís: {pais}")

# Inicializar la ventana
root = tk.Tk()
app = FormularioUsuario(root)
root.mainloop()

#explicacion 
#Este programa resuelve el problema de recolectar información básica de un usuario (nombre, género y país) mediante una interfaz gráfica amigable y accesible. 
# Permite al usuario interactuar con diferentes widgets como campos de texto, botones de selección y menús desplegables para ingresar sus datos.
# El uso de Radiobuttons es útil cuando se desea que el usuario seleccione solo una opción entre varias (como el género), mientras que el Combobox permite seleccionar de una lista predefinida de opciones, facilitando la entrada de datos estructurados.
# Este enfoque es útil en aplicaciones que necesitan recopilar datos de usuarios de forma visual, como formularios de registro, encuestas o sistemas de gestión.






