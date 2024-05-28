#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// Crea un objeto para controlar la placa PCA9685
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Definir los límites del pulso en microsegundos para el servo
#define SERVOMIN  150 // Pulso de 1ms
#define SERVOMAX  600 // Pulso de 2ms
#define DELAY_TIME 20 // Tiempo de retraso entre movimientos en milisegundos

// Array para almacenar el ángulo actual de cada servo
float currentAngle[6] = {90, 0, 0, 0, 90, 90}; // Iniciar todos los servos a 90 grados

void setup() {
  Serial.begin(9600);
  Serial.println("Iniciando PCA9685...");

  // Inicia la placa PCA9685 en la dirección I2C por defecto (0x40)
  pwm.begin();

  // Establece la frecuencia de PWM a 60 Hz, adecuada para servos
  pwm.setPWMFreq(60);

  delay(10);
}

// Función para convertir grados a pulsos
uint16_t degreesToPulse(float degrees) {
  // Limita los grados entre 0 y 180
  degrees = constrain(degrees, 0, 180);
  // Convierte grados a ancho de pulso
  uint16_t pulse = map(degrees, 0, 180, SERVOMIN, SERVOMAX);
  return pulse;
}

// Función para mover un servo a una posición específica en grados
void setServoAngle(uint8_t n, float angle) {
  uint16_t pulse = degreesToPulse(angle);
  pwm.setPWM(n, 0, pulse);
}

// Función para mover un servo suavemente de una posición a otra
void smoothMove(uint8_t servo, float startAngle, float endAngle, int stepDelay) {
  if (startAngle < endAngle) {
    for (float angle = startAngle; angle <= endAngle; angle++) {
      setServoAngle(servo, angle);
      delay(stepDelay);
    }
  } else {
    for (float angle = startAngle; angle >= endAngle; angle--) {
      setServoAngle(servo, angle);
      delay(stepDelay);
    }
  }
}

void loop() {
  // Verifica si hay datos disponibles en el puerto serial
  if (Serial.available()) {
    // Lee el número del servo (0-5)
    int servo = Serial.parseInt();
    // Lee el ángulo al que se debe mover el servo (0-180)
    int angle = Serial.parseInt();

    // Asegúrate de que el número del servo y el ángulo sean válidos
    if (servo >= 1 && servo <= 6 && angle >= 0 && angle <= 180) {
      Serial.print("Moviendo el servo ");
      Serial.print(servo);
      Serial.print(" a ");
      Serial.print(angle);
      Serial.println(" grados.");

      // Mueve el servo suavemente al ángulo especificado desde su ángulo actual
      smoothMove(servo, currentAngle[servo], angle, DELAY_TIME);
      currentAngle[servo] = angle; // Actualiza el ángulo actual
    } else {
      Serial.println("Entrada no válida. Por favor ingrese un número de servo (0-5) seguido por un ángulo (0-180).");
    }

    // Limpiar el buffer serial
    while (Serial.available()) {
      Serial.read();
    }
  }
}
