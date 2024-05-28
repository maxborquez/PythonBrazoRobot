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

void moverServo(Servo &servo, int &posActual, int posFinal) {
  int paso = posFinal > posActual ? 1 : -1; // Definir el paso (1 o -1) según la dirección del movimiento
  for (int pos = posActual; pos != posFinal; pos += paso) {
    servo.write(pos); // Mover el servo a la posición actual
    delay(15); // Esperar un poco para crear un movimiento suave
  }
  posActual = posFinal; // Actualizar la posición actual del servo
}

void loop() {
  if (Serial.available() > 0) {
    // Leer la posición del primer servo
    Serial.println("Ingrese la posicion del servo 1 (0-180):");
    while (Serial.available() == 0) {}
    pos1 = Serial.parseInt();
    pos1 = constrain(pos1, 0, 180); // Asegurarse de que la posición esté entre 0 y 180
    moverServo(servo1, pos1, pos1);
    Serial.println("posicion del servo 1: " + String(pos1));

    // Leer la posición del segundo servo
    Serial.println("Ingrese la posicion del servo 2 (0-180):");
    while (Serial.available() == 0) {}
    pos2 = Serial.parseInt();
    pos2 = constrain(pos2, 0, 180);
    moverServo(servo2, pos2, pos2);
    Serial.println("posicion del servo 2: " + String(pos2));

    // Leer la posición del tercer servo
    Serial.println("Ingrese la posicion del servo 3 (0-180):");
    while (Serial.available() == 0) {}
    pos3 = Serial.parseInt();
    pos3 = constrain(pos3, 0, 180);
    moverServo(servo3, pos3, pos3);
    Serial.println("posicion del servo 3: " + String(pos3));

    // Leer la posición del cuarto servo
    Serial.println("Ingrese la posicion del servo 4 (0-180):");
    while (Serial.available() == 0) {}
    pos4 = Serial.parseInt();
    pos4 = constrain(pos4, 0, 180);
    moverServo(servo4, pos4, pos4);
    Serial.println("posicion del servo 4: " + String(pos4));

    // Leer la posición del quinto servo
    Serial.println("Ingrese la posicion del servo 5 (0-180):");
    while (Serial.available() == 0) {}
    pos5 = Serial.parseInt();
    pos5 = constrain(pos5, 0, 180);
    moverServo(servo5, pos5, pos5);
    Serial.println("posicion del servo 5: " + String(pos5));

    // Leer la posición del sexto servo
    Serial.println("Ingrese la posicion del servo 6 (0-180):");
    while (Serial.available() == 0) {}
    pos6 = Serial.parseInt();
    pos6 = constrain(pos6, 0, 180);
    moverServo(servo6, pos6, pos6);
    Serial.println("posicion del servo 6: " + String(pos6));
  }
}
