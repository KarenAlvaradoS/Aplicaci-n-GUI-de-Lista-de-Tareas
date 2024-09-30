import tkinter as tk
from tkinter import messagebox

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Crear el campo de entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(self.root, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botón para añadir tarea
        self.boton_añadir = tk.Button(self.root, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_añadir.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas (Listbox)
        self.lista_tareas = tk.Listbox(self.root, height=10, width=50, selectmode=tk.SINGLE)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar tarea como completada
        self.boton_completar = tk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

        # Vincular la tecla Enter para añadir tareas
        self.root.bind('<Return>', self.añadir_tarea_evento)

    # Función para añadir una nueva tarea
    def añadir_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea != "":
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

    # Permitir añadir tarea al presionar Enter
    def añadir_tarea_evento(self, event):
        self.añadir_tarea()

    # Función para marcar una tarea como completada
    def marcar_completada(self):
        try:
            tarea_seleccionada = self.lista_tareas.curselection()
            tarea = self.lista_tareas.get(tarea_seleccionada)
            # Marcar la tarea con un ✔ para indicar que está completada
            self.lista_tareas.delete(tarea_seleccionada)
            self.lista_tareas.insert(tarea_seleccionada, f"{tarea} ✔")
        except:
            messagebox.showwarning("Seleccionar tarea", "Por favor, seleccione una tarea para marcar como completada.")

    # Función para eliminar una tarea
    def eliminar_tarea(self):
        try:
            tarea_seleccionada = self.lista_tareas.curselection()
            self.lista_tareas.delete(tarea_seleccionada)
        except:
            messagebox.showwarning("Seleccionar tarea", "Por favor, seleccione una tarea para eliminar.")

# Configuración de la ventana principal de Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareasApp(root)
    root.mainloop()
