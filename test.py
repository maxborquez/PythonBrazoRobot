import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Antropomórfico CrisGo 6GDL")
root.geometry("800x600")

# Sección 1: Conexión
frame_conexion = ttk.LabelFrame(root, text="Conexión", padding="10")
frame_conexion.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

combo_com = ttk.Combobox(frame_conexion, values=["COM1", "COM2", "COM3", "COM4"])
combo_com.grid(row=0, column=0, padx=5, pady=5)
combo_com.set("COM3")

btn_establecer = tk.Button(frame_conexion, text="Establecer Comunicación", bg="green", fg="white")
btn_establecer.grid(row=1, column=0, padx=5, pady=5)

btn_cerrar = tk.Button(frame_conexion, text="Cerrar Comunicación", bg="red", fg="white")
btn_cerrar.grid(row=2, column=0, padx=5, pady=5)

# Sección 2: Cinemática Directa
frame_cinematica_directa = ttk.LabelFrame(root, text="Cinemática Directa", padding="10")
frame_cinematica_directa.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Tabla para los valores
columns = ("#", "θ(grados)", "d(centimetros)", "α(grados)")
tree = ttk.Treeview(frame_cinematica_directa, columns=columns, show="headings", height=7)
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=0, column=0, padx=5, pady=5)

# Agregar algunos datos de ejemplo
data = [
    (0, 0, 3, 0),
    (1, -90, 0, 0),
    (2, 90, 5, 90),
    (3, 0, 16.5, 0),
    (4, 0, 0, -90),
    (5, 0, 4.5, 0)
]
for row in data:
    tree.insert("", "end", values=row)

btn_calcular_directa = tk.Button(frame_cinematica_directa, text="Calcular Directa")
btn_calcular_directa.grid(row=1, column=0, padx=5, pady=5)

# Sección 3: Sliders
frame_sliders = ttk.LabelFrame(root, text="Sliders", padding="10")
frame_sliders.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

for i in range(6):
    tk.Label(frame_sliders, text=f"Ángulos Servomotor {i+1}").grid(row=i, column=0, padx=5, pady=5)
    tk.Scale(frame_sliders, from_=-180, to=180, orient=tk.HORIZONTAL).grid(row=i, column=1, padx=5, pady=5)

# Sección 4: Cinemática Inversa
frame_cinematica_inversa = ttk.LabelFrame(root, text="Cinemática Inversa", padding="10")
frame_cinematica_inversa.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(frame_cinematica_inversa, text="Posición").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame_cinematica_inversa).grid(row=0, column=1, padx=5, pady=5)
tk.Entry(frame_cinematica_inversa).grid(row=0, column=2, padx=5, pady=5)
tk.Entry(frame_cinematica_inversa).grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_cinematica_inversa, text="Orientación").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame_cinematica_inversa).grid(row=1, column=1, padx=5, pady=5)
tk.Entry(frame_cinematica_inversa).grid(row=1, column=2, padx=5, pady=5)
tk.Entry(frame_cinematica_inversa).grid(row=1, column=3, padx=5, pady=5)

btn_calcular_inversa = tk.Button(frame_cinematica_inversa, text="Calcular Inversa", bg="blue", fg="white")
btn_calcular_inversa.grid(row=2, column=1, padx=5, pady=5)

btn_posicionar = tk.Button(frame_cinematica_inversa, text="Posicionar", bg="green", fg="white")
btn_posicionar.grid(row=2, column=2, padx=5, pady=5)

# Sección 5: Panel
frame_panel = ttk.LabelFrame(root, text="Panel", padding="10")
frame_panel.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

for i in range(1, 6):
    tk.Button(frame_panel, text=f"Registro{i}").grid(row=i-1, column=0, padx=5, pady=5)

tk.Button(frame_panel, text="Ejecutar").grid(row=5, column=0, padx=5, pady=5)
tk.Button(frame_panel, text="Limpiar").grid(row=6, column=0, padx=5, pady=5)

# Sección de gráficos (No funcional en este ejemplo)
frame_graficos = ttk.LabelFrame(root, text="Gráficos", padding="10")
frame_graficos.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Agregar espacio para gráficos (puedes usar matplotlib o algún otro método para gráficos reales)
tk.Label(frame_graficos, text="Gráfico 1 (Placeholder)").pack(padx=5, pady=5)
tk.Label(frame_graficos, text="Gráfico 2 (Placeholder)").pack(padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
