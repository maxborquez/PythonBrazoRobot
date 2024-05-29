import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
import serial
import csv

class ControlBrazoRobot:
    def __init__(self, ventana):
        self.azul = "#051333"
        self.rojo = "#932727"
        self.verde = "#1cb360"
        self.ventana = ventana
        self.ventana.title("Control brazo robotico")
        self.ventana.configure(bg=self.azul)
        self.ventana.geometry("1150x680")

        self.button_font = tkfont.Font(family="Arial", size=10, weight="bold")
        self.text_font = tkfont.Font(family="Arial", size=12, weight="bold")

        self.SerialPort1 = serial.Serial()
        self.registro_seleccionado = None  # Variable para almacenar el registro seleccionado
        self.create_widgets()

    def create_widgets(self):
        self.seccion_conexion()
        self.seccion_2()
        self.seccion_servos()
        self.seccion_panel()
        self.tabla_registros()
        self.seccion_6()

    def seccion_conexion(self):
        label_conexion = tk.Label(self.ventana, text="Conexión", bg=self.azul, fg='white', font=self.text_font)
        label_conexion.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

        frame_conexion = tk.Frame(self.ventana, bg=self.azul)
        frame_conexion.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

        self.label_estado = tk.Label(frame_conexion, text="Desconectado", font=self.text_font, bg=self.rojo, fg="white", width=12)
        self.label_estado.grid(row=1, column=0, padx=5, pady=5)

        self.combo_com = ttk.Combobox(frame_conexion, values=["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8"])
        self.combo_com.grid(row=2, column=0, padx=5, pady=5)
        self.combo_com.set("COM1")

        btn_establecer = tk.Button(frame_conexion, text="Conectar", font=self.button_font, command=self.click_conectar)
        btn_establecer.grid(row=3, column=0, padx=5, pady=5)

        btn_cerrar = tk.Button(frame_conexion, text="Desconectar", font=self.button_font, command=self.click_desconectar)
        btn_cerrar.grid(row=4, column=0, padx=5, pady=5)

    def seccion_2(self):
        label_seccion_2 = tk.Label(self.ventana, text="Sección 2", bg=self.azul, fg='white', font=self.text_font)
        label_seccion_2.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

        frame_seccion_2 = tk.Frame(self.ventana, bg=self.azul)
        frame_seccion_2.grid(row=1, column=1, padx=10, pady=5, sticky="nw")

    def seccion_servos(self):
        label_servos = tk.Label(self.ventana, text="Servomotores", bg=self.azul, fg='white', font=self.text_font)
        label_servos.grid(row=0, column=2, padx=10, pady=5, sticky="nw")

        frame_servos = tk.Frame(self.ventana, bg=self.azul)
        frame_servos.grid(row=1, column=2, padx=10, pady=5, sticky="nw")

        self.spinbox_servos = []
        for i in range(6):
            tk.Label(frame_servos, text=f"Posición servo {i+1}", bg=self.azul, fg='white', font=self.text_font).grid(row=i, column=0, padx=5, pady=5)
            spinbox = tk.Spinbox(frame_servos, from_=0, to=180, width=5, font=15)
            spinbox.grid(row=i, column=1, padx=5, pady=5)
            self.spinbox_servos.append(spinbox)

        btn_reset = tk.Button(frame_servos, text="  Reset  ", font=self.button_font, command=self.resetear_posiciones)
        btn_reset.grid(row=6, column=0, padx=5, pady=5)

        btn_mover = tk.Button(frame_servos, text="  Mover  ", font=self.button_font, command=self.enviar_posiciones)
        btn_mover.grid(row=6, column=1, padx=5, pady=5)

    def seccion_panel(self):
        label_panel = tk.Label(self.ventana, text="Panel", bg=self.azul, fg='white', font=self.text_font)
        label_panel.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

        frame_panel = tk.Frame(self.ventana, bg=self.azul)
        frame_panel.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

        btn_registro1 = tk.Button(frame_panel, text="Registro 1", font=self.button_font, command=lambda: self.seleccionar_registro("r1"))
        btn_registro1.grid(row=1, column=0, padx=5, pady=5)

        btn_registro2 = tk.Button(frame_panel, text="Registro 2", font=self.button_font, command=lambda: self.seleccionar_registro("r2"))
        btn_registro2.grid(row=2, column=0, padx=5, pady=5)

        btn_registro3 = tk.Button(frame_panel, text="Registro 3", font=self.button_font, command=lambda: self.seleccionar_registro("r3"))
        btn_registro3.grid(row=3, column=0, padx=5, pady=5)

        btn_registro4 = tk.Button(frame_panel, text="Registro 4", font=self.button_font, command=lambda: self.seleccionar_registro("r4"))
        btn_registro4.grid(row=4, column=0, padx=5, pady=5)

        btn_registro5 = tk.Button(frame_panel, text="Registro 5", font=self.button_font, command=lambda: self.seleccionar_registro("r5"))
        btn_registro5.grid(row=5, column=0, padx=5, pady=5)

        btn_home = tk.Button(frame_panel, text="  Home  ", font=self.button_font, command=self.enviar_home)
        btn_home.grid(row=1, column=1, padx=5, pady=5)

        btn_ejecutar = tk.Button(frame_panel, text="Ejecutar", font=self.button_font)
        btn_ejecutar.grid(row=2, column=1, padx=5, pady=5)

        btn_limpiar = tk.Button(frame_panel, text="Limpiar ", font=self.button_font, command=self.limpiar_registro)
        btn_limpiar.grid(row=3, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(frame_panel, text="Agregar ", font=self.button_font, command=self.agregar_fila)
        btn_agregar.grid(row=4, column=1, padx=5, pady=5)

        btn_quitar = tk.Button(frame_panel, text="  Quitar  ", font=self.button_font, command=self.quitar_ultima_fila)
        btn_quitar.grid(row=5, column=1, padx=5, pady=5)

    def enviar_home(self):
        if self.SerialPort1.isOpen():
            cadena_home = "90,0,0,0,90,90"
            self.SerialPort1.write(cadena_home.encode())
            messagebox.showinfo(message=f"Posiciones home enviadas: {cadena_home}")
        else:
            messagebox.showwarning(message="El puerto no está conectado")

    def tabla_registros(self):
        label_tabla_registros = tk.Label(self.ventana, text="Registros", bg=self.azul, fg='white', font=self.text_font)
        label_tabla_registros.grid(row=2, column=1, padx=10, pady=5, sticky="nw")

        self.frame_tabla_registros = tk.Frame(self.ventana, bg=self.azul)
        self.frame_tabla_registros.grid(row=3, column=1, padx=10, pady=5, sticky="nw")

        self.tree = ttk.Treeview(self.frame_tabla_registros, columns=[f"#{i}" for i in range(1, 7)], show='headings')

        for i in range(1, 7):
            self.tree.heading(f"#{i}", text=f"Servo {i}")
            self.tree.column(f"#{i}", width=100)

        self.tree.pack(expand=True, fill='both')

        tk.Label(self.frame_tabla_registros, text="Tabla de registros", bg=self.azul, fg='white', font=self.text_font).pack(padx=5, pady=5)

    def seccion_6(self):
        label_seccion_6 = tk.Label(self.ventana, text="Sección 6", bg=self.azul, fg='white', font=self.text_font)
        label_seccion_6.grid(row=2, column=2, padx=10, pady=5, sticky="nw")

        frame_seccion_6 = tk.Frame(self.ventana, bg=self.azul)
        frame_seccion_6.grid(row=3, column=2, padx=10, pady=5, sticky="nw")

        image = Image.open("./LogoUBB.png")
        image = image.resize((230, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        label_image = tk.Label(frame_seccion_6, image=self.photo)
        label_image.pack(padx=5, pady=5)

        btn_salir = tk.Button(frame_seccion_6, text=" Salir ", font=self.button_font, command=self.ventana.quit)
        btn_salir.pack(padx=5, pady=5)

    def click_conectar(self):
        try:
            self.SerialPort1.port = self.combo_com.get()
            self.SerialPort1.baudrate = 9600
            self.SerialPort1.open()
            self.label_estado.configure(text="Conectado", bg=self.verde)
        except:
            messagebox.showerror("Error", "No se pudo conectar al puerto")

    def click_desconectar(self):
        if self.SerialPort1.isOpen():
            self.SerialPort1.close()
            self.label_estado.configure(text="Desconectado", bg=self.rojo)

    def enviar_posiciones(self):
        if self.SerialPort1.isOpen():
            posiciones = ",".join(spinbox.get() for spinbox in self.spinbox_servos)
            self.SerialPort1.write(posiciones.encode())
            messagebox.showinfo(message=f"Posiciones enviadas: {posiciones}")
        else:
            messagebox.showwarning(message="El puerto no está conectado")

    def resetear_posiciones(self):
        for spinbox in self.spinbox_servos:
            spinbox.delete(0, 'end')
            spinbox.insert(0, 0)

    def cargar_registros(self):
        registros = {}
        with open('registros.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[0]
                if key not in registros:
                    registros[key] = []
                registros[key].append(row[1:])
        return registros

    def mostrar_registros(self, registro_id):
        registros = self.cargar_registros()
        if registro_id in registros and registros[registro_id]:
            self.tree.delete(*self.tree.get_children())
            for fila in registros[registro_id]:
                self.tree.insert("", "end", values=fila)
        else:
            self.tree.delete(*self.tree.get_children())  # Limpiar la tabla si no hay registros
            messagebox.showinfo("Información", f"Registro seleccionado vacío")

    def seleccionar_registro(self, registro_id):
        self.registro_seleccionado = registro_id
        self.mostrar_registros(registro_id)

    def limpiar_registro(self):
        if self.registro_seleccionado:
            registros = self.cargar_registros()
            if self.registro_seleccionado in registros:
                registros[self.registro_seleccionado] = []  # Limpiar todas las filas del registro seleccionado
                with open('registros.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    for key, values in registros.items():
                        for fila in values:
                            writer.writerow([key] + fila)
                self.mostrar_registros(self.registro_seleccionado)
            else:
                messagebox.showwarning("Advertencia", "No se encontraron registros para limpiar en el registro seleccionado")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro primero")

    def agregar_fila(self):
        if self.registro_seleccionado:
            valores_spinbox = [spinbox.get() for spinbox in self.spinbox_servos]
            if all(self.es_entero_valido(valor) for valor in valores_spinbox):
                nueva_fila = [self.registro_seleccionado] + valores_spinbox
                with open('registros.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(nueva_fila)
                self.mostrar_registros(self.registro_seleccionado)
            else:
                messagebox.showwarning("Advertencia", "Los valores de las posiciones deben ser enteros entre 0 y 180")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro primero")

    def es_entero_valido(self, valor):
        try:
            entero = int(valor)
            return 0 <= entero <= 180
        except ValueError:
            return False

    def quitar_ultima_fila(self):
        if self.registro_seleccionado:
            registros = self.cargar_registros()
            if self.registro_seleccionado in registros:
                registros[self.registro_seleccionado] = registros[self.registro_seleccionado][:-1]
                with open('registros.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    for key, values in registros.items():
                        for fila in values:
                            writer.writerow([key] + fila)
                self.mostrar_registros(self.registro_seleccionado)
            else:
                messagebox.showwarning("Advertencia", "Registro seleccionado vacío")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro primero")

def main():
    ventana = tk.Tk()
    app = ControlBrazoRobot(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
