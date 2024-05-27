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
        self.ventana.geometry("800x600")

        self.button_font = tkfont.Font(family="Arial", size=10, weight="bold")
        self.text_font = tkfont.Font(family="Arial", size=12, weight="bold")

        self.SerialPort1 = serial.Serial()
        self.registros = self.leer_registros_csv("registros.csv")
        self.create_widgets()

    def create_widgets(self):
        self.seccion_conexion()
        self.seccion_2()
        self.seccion_servos()
        self.seccion_panel()
        self.seccion_5()
        self.seccion_6()

    def leer_registros_csv(self, filename):
        registros = {}
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            current_r = None
            for row in reader:
                if len(row) > 0 and row[0].startswith('r'):
                    current_r = row[0]
                    registros[current_r] = []
                elif current_r:
                    registros[current_r].append(row)
        return registros

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

        btn_mover = tk.Button(frame_servos, text="  Mover  ", font=self.button_font, command=self.enviar_posiciones)
        btn_mover.grid(row=6, column=1, padx=5, pady=5)

    def seccion_panel(self):
        label_panel = tk.Label(self.ventana, text="Panel", bg=self.azul, fg='white', font=self.text_font)
        label_panel.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

        frame_panel = tk.Frame(self.ventana, bg=self.azul)
        frame_panel.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

        btn_registro1 = tk.Button(frame_panel, text="Registro 1", font=self.button_font, command=lambda: self.mostrar_registro('r1'))
        btn_registro1.grid(row=1, column=0, padx=5, pady=5)

        btn_registro2 = tk.Button(frame_panel, text="Registro 2", font=self.button_font, command=lambda: self.mostrar_registro('r2'))
        btn_registro2.grid(row=2, column=0, padx=5, pady=5)

        btn_registro3 = tk.Button(frame_panel, text="Registro 3", font=self.button_font, command=lambda: self.mostrar_registro('r3'))
        btn_registro3.grid(row=3, column=0, padx=5, pady=5)

        btn_registro4 = tk.Button(frame_panel, text="Registro 4", font=self.button_font, command=lambda: self.mostrar_registro('r4'))
        btn_registro4.grid(row=4, column=0, padx=5, pady=5)

        btn_registro5 = tk.Button(frame_panel, text="Registro 5", font=self.button_font, command=lambda: self.mostrar_registro('r5'))
        btn_registro5.grid(row=5, column=0, padx=5, pady=5)

        btn_home = tk.Button(frame_panel, text="  Home  ", font=self.button_font)
        btn_home.grid(row=1, column=1, padx=5, pady=5)

        btn_ejecutar = tk.Button(frame_panel, text="Ejecutar", font=self.button_font)
        btn_ejecutar.grid(row=2, column=1, padx=5, pady=5)

        btn_limpiar = tk.Button(frame_panel, text="Limpiar ", font=self.button_font)
        btn_limpiar.grid(row=3, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(frame_panel, text="Agregar ", font=self.button_font)
        btn_agregar.grid(row=4, column=1, padx=5, pady=5)

        btn_quitar = tk.Button(frame_panel, text="  Quitar  ", font=self.button_font)
        btn_quitar.grid(row=5, column=1, padx=5, pady=5)

    def seccion_5(self):
        label_seccion_5 = tk.Label(self.ventana, text="Sección 5", bg=self.azul, fg='white', font=self.text_font)
        label_seccion_5.grid(row=2, column=1, padx=10, pady=5, sticky="nw")

        self.frame_seccion_5 = tk.Frame(self.ventana, bg=self.azul)
        self.frame_seccion_5.grid(row=3, column=1, padx=10, pady=5, sticky="nw")

        for widget in self.frame_seccion_5.winfo_children():
            widget.destroy()

        self.tree = ttk.Treeview(self.frame_seccion_5, columns=[f"#{i}" for i in range(1, 7)], show='headings')

        for i in range(1, 7):
            self.tree.heading(f"#{i}", text=f"Col {i}")
            self.tree.column(f"#{i}", width=100)

        self.tree.pack(expand=True, fill='both')

    def seccion_6(self):
        label_seccion_6 = tk.Label(self.ventana, text="Sección 6", bg=self.azul, fg='white', font=self.text_font)
        label_seccion_6.grid(row=2, column=2, padx=10, pady=5, sticky="nw")

        frame_seccion_6 = tk.Frame(self.ventana, bg=self.azul)
        frame_seccion_6.grid(row=3, column=2, padx=10, pady=5, sticky="nw")

        try:
            image = Image.open("LogoUBB.png")
            image = image.resize((230, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            label_image = tk.Label(frame_seccion_6, image=photo)
            label_image.image = photo
            label_image.pack(padx=50, pady=5)
        except Exception as e:
            print(f"Error loading image: {e}")

        btn_salir = tk.Button(frame_seccion_6, text="Salir", command=self.ventana.quit, font=self.button_font)
        btn_salir.pack(padx=5, pady=5)

    def click_conectar(self):
        if not self.SerialPort1.isOpen():
            try:
                self.SerialPort1.baudrate = 9600
                self.SerialPort1.bytesize = 8
                self.SerialPort1.parity = "N"
                self.SerialPort1.stopbits = serial.STOPBITS_ONE
                self.SerialPort1.port = self.combo_com.get()
                self.SerialPort1.open()
                self.label_estado.config(text="Conectado", bg=self.verde)
                messagebox.showinfo(message="Puerto Conectado")
            except Exception as e:
                messagebox.showerror(message=f"Error al conectar: {e}")
        else:
            messagebox.showinfo(message="El puerto ya está conectado")

    def click_desconectar(self):
        if self.SerialPort1.isOpen():
            self.SerialPort1.close()
            self.label_estado.config(text="Desconectado", bg=self.rojo)
            messagebox.showinfo(message="Puerto Desconectado")
        else:
            messagebox.showinfo(message="El puerto ya está desconectado")

    def enviar_posiciones(self):
        if self.SerialPort1.isOpen():
            posiciones = [spinbox.get() for spinbox in self.spinbox_servos]
            cadena = ",".join(posiciones)
            self.SerialPort1.write(cadena.encode())
            messagebox.showinfo(message=f"Posiciones enviadas: {cadena}")
        else:
            messagebox.showwarning(message="El puerto no está conectado")

    def mostrar_registro(self, registro):
        for widget in self.frame_seccion_5.winfo_children():
            widget.destroy()

        self.tree = ttk.Treeview(self.frame_seccion_5, columns=[f"#{i}" for i in range(1, 7)], show='headings')

        for i in range(1, 7):
            self.tree.heading(f"#{i}", text=f"Servo {i}")
            self.tree.column(f"#{i}", width=100)

        self.tree.pack(expand=True, fill='both')

        if registro in self.registros:
            if len(self.registros[registro]) == 0:
                tk.Label(self.frame_seccion_5, text="No hay datos", bg=self.azul, fg='white', font=self.text_font).pack(padx=5, pady=5)
            else:
                for row in self.registros[registro]:
                    self.tree.insert("", "end", values=row)

def main():
    ventana = tk.Tk()
    app = ControlBrazoRobot(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
