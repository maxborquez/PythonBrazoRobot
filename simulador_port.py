import serial
import threading

# Puerto COM virtual a simular
COM_PORT = 'COM1'

def simulate_device():
    with serial.Serial(COM_PORT, baudrate=9600, timeout=1) as ser:
        print(f"Simulated device connected to {COM_PORT}")
        while True:
            # Simular la recepción de datos
            data = ser.readline().decode().strip()
            if data:
                print(f"Received: {data}")

if __name__ == "__main__":
    # Crear un hilo para simular el dispositivo
    t = threading.Thread(target=simulate_device)
    t.daemon = True
    t.start()

    # Esperar a que el usuario presione Enter para salir
    input("Press Enter to exit\n")
