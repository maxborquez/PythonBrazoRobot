// Librerias
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <LiquidCrystal.h>

Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver(0x40);
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // Inicializa la pantalla LCD

// Variables
int pos0_S1 = 95;
int pos180_S1 = 500;
int pos0_S2 = 110;
int pos180_S2 = 500;
int pos0_S3 = 130;
int pos180_S3 = 500;
int pos0_S4 = 100;
int pos180_S4 = 500;
int pos0_S5 = 100;
int pos180_S5 = 500;
int pos0_S6 = 106;
int pos180_S6 = 488;
int servoPos[7] = {0, 0, 0, 0, 0, 0, 0};
int lastSetPos[7] = {0, 0, 0, 0, 0, 0, 0};

// Funciones
void moveAllServosToZero()
{
    for (int i = 1; i < 7; i++)
    {
        setServo(i, 0); // Mover el servo 'i' a la posición 0
    }
}

void moveAllServosToHome()
{
    for (int i = 1; i < 7; i++)
    {
        if (i == 2)
        {
            setServo(i, 60); // Mover el servo 2 a 60
        }
        else if (i == 3)
        {
            setServo(i, 20); // Mover el servo 3 a 20
        }
        else
        {
            setServo(i, 0); // Mover los otros servos a 0
        }
    }
}

void setServo(uint8_t n_servo, int angulo)
{
    int duty;
    int delayTime = 50; // Tiempo de retardo en milisegundos
    int stepDelay = 50; // Tiempo de retardo entre cada paso en milisegundos
    int steps = 30;     // Número de pasos para la transición
    int currentAngle = lastSetPos[n_servo];
    int targetAngle = angulo;
    int stepSize = (targetAngle - currentAngle) / steps;

    // Limitar los ángulos servos 2 y 3
    if (n_servo == 2)
    {
        if (lastSetPos[3] >= 95 && lastSetPos[3] <= 100 && angulo > 10)
        {                                  // Si el servo 2 está en 100 grados, limitar el servo 3 a 20 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 10 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 10;
        }
        else if (lastSetPos[3] >= 85 && lastSetPos[3] <= 95 && angulo > 20)
        {                                  // Si el servo 2 está en 90 grados, limitar el servo 3 a 30 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 20 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 20;
        }
        else if (lastSetPos[3] >= 75 && lastSetPos[3] <= 85 && angulo > 30)
        {                                  // Si el servo 2 está en 80 grados, limitar el servo 3 a 40 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 30 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 30;
        }
        else if (lastSetPos[3] >= 65 && lastSetPos[3] <= 75 && angulo > 40)
        {                                  // Si el servo 2 está en 70 grados, limitar el servo 3 a 50 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 40 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 40;
        }
        else if (lastSetPos[3] >= 55 && lastSetPos[3] <= 65 && angulo > 60)
        {                                  // Si el servo 2 está en 60 grados, limitar el servo 3 a 60 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 60 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 60;
        }
        else if (lastSetPos[3] >= 45 && lastSetPos[3] <= 55 && angulo > 80)
        {                                  // Si el servo 2 está en 50 grados, limitar el servo 3 a 80 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 80 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 80;
        }
        else if (lastSetPos[3] >= 35 && lastSetPos[3] <= 45 && angulo > 90)
        {                                  // Si el servo 2 está en 40 grados, limitar el servo 3 a 100 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 90 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 90;
        }
        else if (lastSetPos[3] >= 25 && lastSetPos[3] <= 35 && angulo > 100)
        {                                   // Si el servo 2 está en 30 grados, limitar el servo 3 a 110 grados
            lcd.clear();                    // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);            // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");    // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);            // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 100 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 100;
        }
        else if (lastSetPos[3] >= 15 && lastSetPos[3] <= 25 && angulo > 110)
        {                                   // Si el servo 2 está en 20 grados, limitar el servo 3 a 120 grados
            lcd.clear();                    // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);            // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");    // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);            // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 110 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 110;
        }
        else if (n_servo == 2 && angulo > 120)
        {                                  // Limitar el servo 2 a maximo 120
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Limite Alcanzado"); // Mostrar el mensaje de límite alcanzado
            angulo = 120;
        }
    }
    else if (n_servo == 3 && angulo > 100)
    {                                  // Limitar el servo 3 a maximo 100
        lcd.clear();                   // Limpiar la pantalla LCD
        lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
        lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
        lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
        lcd.print("Limite Alcanzado"); // Mostrar el mensaje de límite alcanzado
        angulo = 100;
    }
    else if (n_servo == 5 && angulo > 140)
    {                                  // Limitar el servo 5 a maximo 100
        lcd.clear();                   // Limpiar la pantalla LCD
        lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
        lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
        lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
        lcd.print("Limite Alcanzado"); // Mostrar el mensaje de límite alcanzado
        angulo = 140;
    }

    if (n_servo == 3)
    {
        if (lastSetPos[2] >= 115 && lastSetPos[2] <= 120 && angulo > 10)
        {                                  // Si el servo 2 está en 100 grados, limitar el servo 3 a 20 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 10 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 10;
        }
        else if (lastSetPos[2] >= 105 && lastSetPos[2] <= 115 && angulo > 10)
        {                                  // Si el servo 2 está en 90 grados, limitar el servo 3 a 30 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 10 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 10;
        }
        else if (lastSetPos[2] >= 95 && lastSetPos[2] <= 105 && angulo > 20)
        {                                  // Si el servo 2 está en 80 grados, limitar el servo 3 a 40 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 20 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 20;
        }
        else if (lastSetPos[2] >= 85 && lastSetPos[2] <= 95 && angulo > 30)
        {                                  // Si el servo 2 está en 70 grados, limitar el servo 3 a 50 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 30 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 30;
        }
        else if (lastSetPos[2] >= 75 && lastSetPos[2] <= 85 && angulo > 40)
        {                                  // Si el servo 2 está en 60 grados, limitar el servo 3 a 60 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 40 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 40;
        }
        else if (lastSetPos[2] >= 65 && lastSetPos[2] <= 75 && angulo > 50)
        {                                  // Si el servo 2 está en 50 grados, limitar el servo 3 a 80 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 50 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 50;
        }
        else if (lastSetPos[2] >= 55 && lastSetPos[2] <= 65 && angulo > 60)
        {                                  // Si el servo 2 está en 40 grados, limitar el servo 3 a 100 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 60 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 60;
        }
        else if (lastSetPos[2] >= 45 && lastSetPos[2] <= 55 && angulo > 60)
        {                                  // Si el servo 2 está en 30 grados, limitar el servo 3 a 110 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 60 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 60;
        }
        else if (lastSetPos[2] >= 35 && lastSetPos[2] <= 45 && angulo > 70)
        {                                  // Si el servo 2 está en 20 grados, limitar el servo 3 a 120 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 70 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 70;
        }
        else if (lastSetPos[2] >= 25 && lastSetPos[2] <= 35 && angulo > 80)
        {                                  // Si el servo 2 está en 20 grados, limitar el servo 3 a 120 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 80 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 80;
        }
        else if (lastSetPos[2] >= 15 && lastSetPos[2] <= 25 && angulo > 90)
        {                                  // Si el servo 2 está en 20 grados, limitar el servo 3 a 120 grados
            lcd.clear();                   // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);           // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");   // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);           // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 90 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 90;
        }
        else if (lastSetPos[2] >= 5 && lastSetPos[2] <= 15 && angulo > 100)
        {                                   // Si el servo 2 está en 20 grados, limitar el servo 3 a 120 grados
            lcd.clear();                    // Limpiar la pantalla LCD
            lcd.setCursor(0, 0);            // Posicionar el cursor en la fila 1, columna 1
            lcd.print("Dato Recibido:");    // Mostrar un mensaje de confirmación
            lcd.setCursor(0, 1);            // Posicionar el cursor en la fila 2, columna 1
            lcd.print("Maximo 100 Grados"); // Mostrar el mensaje de límite alcanzado
            angulo = 100;
        }
    }

    // Ajustar Servos
    if (n_servo == 1)
    {
        duty = map(currentAngle, 0, 180, pos0_S1, pos180_S1);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Servo: ");
        lcd.print(n_servo);
        lcd.setCursor(0, 1);
        lcd.print("Angulo:");
        lcd.print(currentAngle);
    }
    else if (n_servo == 2)
    {
        duty = map(currentAngle, 0, 180, pos0_S2, pos180_S2);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Servo: ");
        lcd.print(n_servo);
        lcd.setCursor(0, 1);
        lcd.print("Angulo:");
        lcd.print(currentAngle);
    }
    else if (n_servo == 3)
    {
        duty = map(currentAngle, 0, 180, pos0_S3, pos180_S3);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Servo: ");
        lcd.print(n_servo);
        lcd.setCursor(0, 1);
        lcd.print("Angulo:");
        lcd.print(currentAngle);
    }
    else if (n_servo == 4)
    {
        duty = map(currentAngle, 0, 180, pos0_S4, pos180_S4);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Servo: ");
        lcd.print(n_servo);
        lcd.setCursor(0, 1);
        lcd.print("Angulo:");
        lcd.print(currentAngle);
    }
    else if (n_servo == 5)
    {
        duty = map(currentAngle, 0, 180, pos0_S5, pos180_S5);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Servo: ");
        lcd.print(n_servo);
        lcd.setCursor(0, 1);
        lcd.print("Angulo:");
        lcd.print(currentAngle);
    }
    else if (n_servo == 6)
    {
        duty = map(currentAngle, 0, 180, pos0_S6, pos180_S6);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Servo: ");
        lcd.print(n_servo);
        lcd.setCursor(0, 1);
        lcd.print("Angulo:");
        lcd.print(currentAngle);
    }
    else
    {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("ERROR");
        return;
    }

    // Mover el servo en pasos graduales
    for (int i = 0; i < steps; i++)
    {
        // Actualizar la posición actual en cada paso
        currentAngle += stepSize;
        if ((stepSize > 0 && currentAngle > targetAngle) || (stepSize < 0 && currentAngle < targetAngle))
        {
            currentAngle = targetAngle;
        }
        duty = map(currentAngle, 0, 180, (n_servo == 1) ? pos0_S1 : (n_servo == 2) ? pos0_S2
                                                                : (n_servo == 3)   ? pos0_S3
                                                                : (n_servo == 4)   ? pos0_S4
                                                                : (n_servo == 5)   ? pos0_S5
                                                                                   : pos0_S6,
                   (n_servo == 1) ? pos180_S1 : (n_servo == 2) ? pos180_S2
                                            : (n_servo == 3)   ? pos180_S3
                                            : (n_servo == 4)   ? pos180_S4
                                            : (n_servo == 5)   ? pos180_S5
                                                               : pos180_S6);
        servos.setPWM(n_servo, 0, duty);
        delay(stepDelay); // Esperar antes del siguiente paso
    }

    // Actualizar el arreglo de posiciones establecidas
    lastSetPos[n_servo] = angulo;
}

void setup()
{
    servos.begin();
    servos.setPWMFreq(50);
    Serial.begin(115200);
    moveAllServosToHome();
    lcd.begin(16, 2); // Configurar la pantalla LCD como 16x2

    // Mostrar un mensaje de bienvenida en la pantalla LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("   Brazo robot ");
    lcd.setCursor(0, 1);
    lcd.print("6 Grad. Libertad");
}

void loop()
{
    String data;

    if (Serial.available() > 0)
    {
        data = Serial.readStringUntil('\n');

        Serial.print("Data: ");
        Serial.println(data);

        // Verificar si se recibieron seis valores de ángulo separados por espacios
        int pos[6];
        int num_pos = sscanf(data.c_str(), "%d,%d,%d,%d,%d,%d", &pos[0], &pos[1], &pos[2], &pos[3], &pos[4], &pos[5]);

        if (num_pos == 6)
        {
            // Mover todos los servos a las posiciones deseadas
            for (int i = 0; i < 6; i++)
            {

                setServo(i + 1, pos[i]); // Sumar 1 al índice del servo para que vaya de 1 a 6
                delay(2000);
            }
        }

        if (data.startsWith("s"))
        {
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Dato Recibido:");
            lcd.setCursor(0, 1);

            // Extraer los números del comando
            int n1, n2;
            if (sscanf(data.c_str(), "s%d,%d", &n1, &n2) == 2)
            {
                lcd.print("Mover servo");
                lcd.print(n1);
                lcd.print(" a ");
                lcd.print(n2);
                setServo(n1, n2);
            }
        }

        // Verificar si el comando es "Home"
        if (data == "Home")
        {
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Dato Recibido:");
            lcd.setCursor(0, 1);
            lcd.print("Posicion Home");
            moveAllServosToHome();
        }
    }
}
