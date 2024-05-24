import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
import serial

class ControlBrazoRobot:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Control brazo robotico")
        self.ventana.configure(bg='#051333')
        self.ventana.geometry("800x600")

        self.button_font = tkfont.Font(family="Arial", size=10, weight="bold")
        self.text_font = tkfont.Font(family="Arial", size=12, weight="bold")

        self.SerialPort1 = serial.Serial()
        self.create_widgets()

    def create_widgets(self):
        self.seccion_conexion()
        self.seccion_2()
        self.seccion_servos()
        self.seccion_panel()
        self.seccion_6()

    def seccion_conexion(self):
        label_conexion = tk.Label(self.ventana, text="Conexión", bg='#051333', fg='white', font=self.text_font)
        label_conexion.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

        frame_conexion = tk.Frame(self.ventana, bg='#051333')
        frame_conexion.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

        self.label_estado = tk.Label(frame_conexion, text="Desconectado", font=self.text_font, bg="#932727", fg="white", width=20)
        self.label_estado.grid(row=1, column=0, padx=5, pady=5)

        self.combo_com = ttk.Combobox(frame_conexion, values=["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8"])
        self.combo_com.grid(row=2, column=0, padx=5, pady=5)
        self.combo_com.set("COM1")

        btn_establecer = tk.Button(frame_conexion, text="Conectar", font=self.button_font, command=self.click_conectar)
        btn_establecer.grid(row=3, column=0, padx=5, pady=5)

        btn_cerrar = tk.Button(frame_conexion, text="Desconectar", font=self.button_font, command=self.click_desconectar)
        btn_cerrar.grid(row=4, column=0, padx=5, pady=5)

    def seccion_2(self):
        label_cinematica_directa = tk.Label(self.ventana, text="Seccion 2", bg='#051333', fg='white', font=self.text_font)
        label_cinematica_directa.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

        frame_cinematica_directa = tk.Frame(self.ventana, bg='#051333')
        frame_cinematica_directa.grid(row=1, column=1, padx=10, pady=5, sticky="nw")

    def seccion_servos(self):
        label_entradas = tk.Label(self.ventana, text="Servomotores", bg='#051333', fg='white', font=self.text_font)
        label_entradas.grid(row=0, column=2, padx=10, pady=5, sticky="nw")

        frame_entradas = tk.Frame(self.ventana, bg='#051333')
        frame_entradas.grid(row=1, column=2, padx=10, pady=5, sticky="nw")

        for i in range(6):
            tk.Label(frame_entradas, text=f"Ángulos Servomotor {i + 1}", bg='#051333', fg='white', font=self.text_font).grid(row=i, column=0, padx=5, pady=5)
            tk.Spinbox(frame_entradas, from_=0, to=180).grid(row=i, column=1, padx=5, pady=5)

    def seccion_panel(self):
        label_panel = tk.Label(self.ventana, text="Panel", bg='#051333', fg='white', font=self.text_font)
        label_panel.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

        frame_panel = tk.Frame(self.ventana, bg='#051333')
        frame_panel.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

        buttons = ["Registro 1", "Registro 2", "Registro 3", "Registro 4", "Registro 5", "Home", "Ejecutar", "Limpiar"]
        for i, text in enumerate(buttons):
            row = i % 5 + 1
            column = 0 if i < 5 else 1
            tk.Button(frame_panel, text=text, font=self.button_font).grid(row=row, column=column, padx=5, pady=5)

    def seccion_6(self):
        label_graficos = tk.Label(self.ventana, text="Seccion 6", bg='#051333', fg='white', font=self.text_font)
        label_graficos.grid(row=2, column=2, padx=10, pady=5, sticky="nw")

        frame_graficos = tk.Frame(self.ventana, bg='#051333')
        frame_graficos.grid(row=3, column=2, padx=10, pady=5, sticky="nw")

        try:
            image = Image.open("LogoUBB.png")
            image = image.resize((230, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            label_image = tk.Label(frame_graficos, image=photo)
            label_image.image = photo
            label_image.pack(padx=50, pady=5)
        except Exception as e:
            print(f"Error loading image: {e}")

        btn_salir = tk.Button(frame_graficos, text="Salir", command=self.ventana.quit, font=self.button_font)
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
                self.label_estado.config(text="Conectado", bg="#1cb360")
                messagebox.showinfo(message="Puerto Conectado")
            except Exception as e:
                messagebox.showerror(message=f"Error al conectar: {e}")
        else:
            messagebox.showinfo(message="El puerto ya está conectado")

    def click_desconectar(self):
        if self.SerialPort1.isOpen():
            self.SerialPort1.close()
            self.label_estado.config(text="Desconectado", bg="#932727")
            messagebox.showinfo(message="Puerto Desconectado")
        else:
            messagebox.showinfo(message="El puerto ya está desconectado")


def main():
    ventana = tk.Tk()
    app = ControlBrazoRobot(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
