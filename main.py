import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
import serial

# Crear la ventana principal
root = tk.Tk()
root.title("Control brazo robotico")
root.configure(bg='#051333')
root.geometry("1350x680")

button_font = tkfont.Font(family="Arial", size=10, weight="bold")
text_font = tkfont.Font(family="Arial", size=12, weight="bold")

# Estado del puerto serial
SerialPort1 = serial.Serial()

# Funciones de conexión y desconexión
def click_conectar():
    if not SerialPort1.isOpen():
        try:
            SerialPort1.baudrate = 9600
            SerialPort1.bytesize = 8
            SerialPort1.parity = "N"
            SerialPort1.stopbits = serial.STOPBITS_ONE
            SerialPort1.port = combo_com.get()
            SerialPort1.open()
            label_estado.config(text="Conectado", bg="#1cb360")
            messagebox.showinfo(message="Puerto Conectado")
        except Exception as e:
            messagebox.showerror(message=f"Error al conectar: {e}")
    else:
        messagebox.showinfo(message="El puerto ya está conectado")

def click_desconectar():
    if SerialPort1.isOpen():
        SerialPort1.close()
        label_estado.config(text="Desconectado", bg="#932727")
        messagebox.showinfo(message="Puerto Desconectado")
    else:
        messagebox.showinfo(message="El puerto ya está desconectado")

# Sección 1: Conexión
label_conexion = tk.Label(root, text="Conexión", bg='#051333', fg='white', font=text_font)
label_conexion.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

frame_conexion = tk.Frame(root, bg='#051333')
frame_conexion.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

# Label para mostrar el estado de la conexión
label_estado = tk.Label(frame_conexion, text="Desconectado", font=text_font, bg="#932727", fg="white", width=20)
label_estado.grid(row=1, column=0, padx=5, pady=5)

combo_com = ttk.Combobox(frame_conexion, values=["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8"])
combo_com.grid(row=2, column=0, padx=5, pady=5)
combo_com.set("COM1")

btn_establecer = tk.Button(frame_conexion, text="Conectar", font=button_font, command=click_conectar)
btn_establecer.grid(row=3, column=0, padx=5, pady=5)

btn_cerrar = tk.Button(frame_conexion, text="Desconectar", font=button_font, command=click_desconectar)
btn_cerrar.grid(row=4, column=0, padx=5, pady=5)

# Sección 2: Cinemática Directa
label_cinematica_directa = tk.Label(root, text="Seccion 2", bg='#051333', fg='white', font=text_font)
label_cinematica_directa.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

frame_cinematica_directa = tk.Frame(root, bg='#051333')
frame_cinematica_directa.grid(row=1, column=1, padx=10, pady=5, sticky="nw")

# Sección 3: Entradas Numéricas
label_entradas = tk.Label(root, text="Entradas Numéricas", bg='#051333', fg='white', font=text_font)
label_entradas.grid(row=0, column=2, padx=10, pady=5, sticky="nw")

frame_entradas = tk.Frame(root, bg='#051333')
frame_entradas.grid(row=1, column=2, padx=10, pady=5, sticky="nw")

tk.Label(frame_entradas, text="Ángulos Servomotor 1", bg='#051333', fg='white', font=text_font).grid(row=0, column=0, padx=5, pady=5)
spinbox1 = tk.Spinbox(frame_entradas, from_=0, to=180)
spinbox1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="Ángulos Servomotor 2", bg='#051333', fg='white', font=text_font).grid(row=1, column=0, padx=5, pady=5)
spinbox2 = tk.Spinbox(frame_entradas, from_=0, to=180)
spinbox2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="Ángulos Servomotor 3", bg='#051333', fg='white', font=text_font).grid(row=2, column=0, padx=5, pady=5)
spinbox3 = tk.Spinbox(frame_entradas, from_=0, to=180)
spinbox3.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="Ángulos Servomotor 4", bg='#051333', fg='white', font=text_font).grid(row=3, column=0, padx=5, pady=5)
spinbox4 = tk.Spinbox(frame_entradas, from_=0, to=180)
spinbox4.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="Ángulos Servomotor 5", bg='#051333', fg='white', font=text_font).grid(row=4, column=0, padx=5, pady=5)
spinbox5 = tk.Spinbox(frame_entradas, from_=0, to=180)
spinbox5.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="Ángulos Servomotor 6", bg='#051333', fg='white', font=text_font).grid(row=5, column=0, padx=5, pady=5)
spinbox6 = tk.Spinbox(frame_entradas, from_=0, to=180)
spinbox6.grid(row=5, column=1, padx=5, pady=5)

# Sección 4: Cinemática Inversa
label_cinematica_inversa = tk.Label(root, text="Seccion 5", bg='#051333', fg='white', font=text_font)
label_cinematica_inversa.grid(row=2, column=1, padx=10, pady=5, sticky="nw")

# Sección 5: Panel
label_panel = tk.Label(root, text="Panel", bg='#051333', fg='white', font=text_font)
label_panel.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

frame_panel = tk.Frame(root, bg='#051333')
frame_panel.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

# Registros de estados
btn_r1 = tk.Button(frame_panel, text=f"Registro 1", font=button_font).grid(row=1, column=1, padx=5, pady=5)
btn_r2 = tk.Button(frame_panel, text=f"Registro 2", font=button_font).grid(row=2, column=1, padx=5, pady=5)
btn_r3 = tk.Button(frame_panel, text=f"Registro 3", font=button_font).grid(row=3, column=1, padx=5, pady=5)
btn_r4 = tk.Button(frame_panel, text=f"Registro 4", font=button_font).grid(row=4, column=1, padx=5, pady=5)
btn_r5 = tk.Button(frame_panel, text=f"Registro 5", font=button_font).grid(row=5, column=1, padx=5, pady=5)

btn_home = tk.Button(frame_panel, text="  Home  ", font=button_font).grid(row=1, column=0, padx=5, pady=5)
btn_ejecutar = tk.Button(frame_panel, text="Ejecutar", font=button_font).grid(row=2, column=0, padx=5, pady=5)
btn_limpiar = tk.Button(frame_panel, text="Limpiar ", font=button_font).grid(row=3, column=0, padx=5, pady=5)

# Sección de gráficos (Incluir imagen)
label_graficos = tk.Label(root, text="", bg='#051333', fg='white', font=text_font)
label_graficos.grid(row=2, column=2, padx=10, pady=5, sticky="nw")

frame_graficos = tk.Frame(root, bg='#051333')
frame_graficos.grid(row=3, column=2, padx=10, pady=5, sticky="nw")

# Cargar la imagen y colocarla en el label
try:
    image = Image.open("LogoUBB.png")
    image = image.resize((230, 200), Image.LANCZOS)  # Ajustar tamaño a 100x100
    photo = ImageTk.PhotoImage(image)

    label_image = tk.Label(frame_graficos, image=photo)
    label_image.image = photo  # Necesario para mantener una referencia de la imagen
    label_image.pack(padx=50, pady=5)
except Exception as e:
    print(f"Error loading image: {e}")

btn_salir = tk.Button(frame_graficos, text="Salir", command=root.quit, font=button_font)
btn_salir.pack(padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
