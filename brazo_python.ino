#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

int pos1 = 0;
int pos2 = 0;
int pos3 = 0;
int pos4 = 0;
int pos5 = 0;
int pos6 = 0;

void moverServo(Servo &servo, int &posActual, int posFinal) {
  int paso = posFinal > posActual ? 1 : -1; // Definir el paso (1 o -1) según la dirección del movimiento
  for (int pos = posActual; pos != posFinal; pos += paso) {
    servo.write(pos); // Mover el servo a la posición actual
    delay(15); // Esperar un poco para crear un movimiento suave
  }
  posActual = posFinal; // Actualizar la posición actual del servo
}

void setup() {
  // Asignar los pines de control para cada servo
  servo1.attach(2);
  servo2.attach(3);
  servo3.attach(4);
  servo4.attach(5);
  servo5.attach(6);
  servo6.attach(7);

  // Iniciar la comunicación serie
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Leer la cadena completa desde el puerto serie
    String posiciones = Serial.readStringUntil('\n');
    // Separar la cadena en las posiciones individuales
    int index1 = posiciones.indexOf(',');
    int newPos1 = posiciones.substring(0, index1).toInt();
    newPos1 = constrain(newPos1, 0, 180);
    moverServo(servo1, pos1, newPos1);

    int index2 = posiciones.indexOf(',', index1 + 1);
    int newPos2 = posiciones.substring(index1 + 1, index2).toInt();
    newPos2 = constrain(newPos2, 0, 180);
    moverServo(servo2, pos2, newPos2);

    int index3 = posiciones.indexOf(',', index2 + 1);
    int newPos3 = posiciones.substring(index2 + 1, index3).toInt();
    newPos3 = constrain(newPos3, 0, 180);
    moverServo(servo3, pos3, newPos3);

    int index4 = posiciones.indexOf(',', index3 + 1);
    int newPos4 = posiciones.substring(index3 + 1, index4).toInt();
    newPos4 = constrain(newPos4, 0, 180);
    moverServo(servo4, pos4, newPos4);

    int index5 = posiciones.indexOf(',', index4 + 1);
    int newPos5 = posiciones.substring(index4 + 1, index5).toInt();
    newPos5 = constrain(newPos5, 0, 180);
    moverServo(servo5, pos5, newPos5);

    int newPos6 = posiciones.substring(index5 + 1).toInt();
    newPos6 = constrain(newPos6, 0, 180);
    moverServo(servo6, pos6, newPos6);

    // Enviar las posiciones a través de Serial para verificación
    Serial.println("Posiciones recibidas:");
    Serial.println("Servo 1: " + String(pos1));
    Serial.println("Servo 2: " + String(pos2));
    Serial.println("Servo 3: " + String(pos3));
    Serial.println("Servo 4: " + String(pos4));
    Serial.println("Servo 5: " + String(pos5));
    Serial.println("Servo 6: " + String(pos6));
  }
}
