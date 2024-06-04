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

// Array para almacenar los ángulos de la posición base
float basePosition[6] = {90, 0, 0, 0, 90, 90};

void setup() {
  Serial.begin(9600);
  Serial.println("Iniciando PCA9685...");

  // Inicia la placa PCA9685 en la dirección I2C por defecto (0x40)
  pwm.begin();

  // Establece la frecuencia de PWM a 60 Hz, adecuada para servos
  pwm.setPWMFreq(60);

  delay(10);

  // Mover los servos a la posición base suavemente
  for (int i = 1; i <= 6; i++) {
    float current = currentAngle[i - 1];
    float target = basePosition[i - 1];
    float step = 1; // Paso de incremento de ángulo

    if (current < target) {
      for (float angle = current; angle <= target; angle += step) {
        setServoAngle(i, angle);
        delay(DELAY_TIME);
      }
    } else {
      for (float angle = current; angle >= target; angle -= step) {
        setServoAngle(i, angle);
        delay(DELAY_TIME);
      }
    }

    currentAngle[i - 1] = target; // Actualiza el ángulo actual
  }
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
    // Leer la cadena de entrada
    String input = Serial.readStringUntil('\n');

    // Array para almacenar los ángulos de los servos
    float targetAngles[6];

    // Separar la cadena por comas y convertir a float
    int i = 0;
    int startIndex = 0;
    while (i < 6) {
      int commaIndex = input.indexOf(',', startIndex);
      if (commaIndex == -1) {
        commaIndex = input.length();
      }

      if (commaIndex == startIndex) {
        Serial.println("Entrada no válida. Asegúrate de que todos los ángulos estén presentes y separados por comas.");
        return;
      }

      targetAngles[i] = input.substring(startIndex, commaIndex).toFloat();
      if (targetAngles[i] < 0 || targetAngles[i] > 180) {
        Serial.println("Entrada no válida. Asegúrate de que todos los ángulos estén en el rango de 0 a 180 grados.");
        return;
      }

      startIndex = commaIndex + 1;
      i++;
    }

    // Mover cada servo al ángulo especificado
    for (int j = 0; j < 6; j++) {
      Serial.print("Moviendo el servo ");
      Serial.print(j + 1); // Se suma 1 para que los servos se muestren del 1 al 6
      Serial.print(" a ");
      Serial.print(targetAngles[j]);
      Serial.println(" grados.");
      smoothMove(j + 1, currentAngle[j], targetAngles[j], DELAY_TIME); // Se suma 1 para que los servos se muevan del 1 al 6
      currentAngle[j] = targetAngles[j]; // Actualiza el ángulo actual
    }
  }
}

