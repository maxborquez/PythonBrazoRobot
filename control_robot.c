#include <stdio.h>
#include <windows.h>
#include <string.h>

// Declaración de funciones
void moverUnServo(HANDLE hSerial);
void moverSeisServos(HANDLE hSerial);
HANDLE conectarPuertoSerial(char *puerto);

int main()
{
    HANDLE hSerial;
    char puerto[10];
    int numeroPuerto;
    int opcion;

    // Solicitar al usuario el número del puerto COM
    printf("Ingrese el número del puerto COM (1-8): ");
    scanf("%d", &numeroPuerto);

    // Validar el número del puerto
    if (numeroPuerto < 1 || numeroPuerto > 8)
    {
        printf("Número de puerto COM no válido. Debe estar entre 1 y 8.\n");
        return 1;
    }

    // Construir la cadena del puerto COM
    snprintf(puerto, sizeof(puerto), "\\\\.\\COM%d", numeroPuerto);

    // Conectar al puerto serial
    hSerial = conectarPuertoSerial(puerto);

    if (hSerial == INVALID_HANDLE_VALUE)
    {
        printf("Error al conectar con el puerto %s\n", puerto);
        return 1;
    }
    else
    {
        printf("Conectado exitosamente al puerto %s\n", puerto);
    }

    // Menú de opciones
    do
    {
        printf("Seleccione una opción:\n");
        printf("1. Mover un solo servo\n");
        printf("2. Mover los 6 servos\n");
        printf("3. Salir\n");
        printf("Opción: ");

        // Leer la opción del usuario
        do
        {
            scanf("%d", &opcion);
            if (opcion < 1 || opcion > 3)
            {
                printf("Opción no válida. Inténtelo de nuevo: ");
            }

        } while (opcion < 1 || opcion > 3);

        // Ejecutar la opción seleccionada
        switch (opcion)
        {
        case 1:
            moverUnServo(hSerial);
            break;
        case 2:
            moverSeisServos(hSerial);
            break;
        case 3:
            printf("Saliendo...\n");
            break;
        default:
            printf("Opción no válida. Inténtelo de nuevo.\n");
        }
    } while (opcion != 3);

    // Cerrar el puerto serial antes de salir
    CloseHandle(hSerial);

    return 0;
}

HANDLE conectarPuertoSerial(char *puerto)
{
    HANDLE hSerial;
    DCB dcbSerialParams = {0};
    COMMTIMEOUTS timeouts = {0};

    hSerial = CreateFile(
        puerto,
        GENERIC_READ | GENERIC_WRITE,
        0,
        NULL,
        OPEN_EXISTING,
        0,
        NULL);

    if (hSerial == INVALID_HANDLE_VALUE)
    {
        return INVALID_HANDLE_VALUE;
    }

    dcbSerialParams.DCBlength = sizeof(dcbSerialParams);

    if (!GetCommState(hSerial, &dcbSerialParams))
    {
        CloseHandle(hSerial);
        return INVALID_HANDLE_VALUE;
    }

    dcbSerialParams.BaudRate = CBR_115200;
    dcbSerialParams.ByteSize = 8;
    dcbSerialParams.StopBits = ONESTOPBIT;
    dcbSerialParams.Parity = NOPARITY;

    if (!SetCommState(hSerial, &dcbSerialParams))
    {
        CloseHandle(hSerial);
        return INVALID_HANDLE_VALUE;
    }

    timeouts.ReadIntervalTimeout = 50;
    timeouts.ReadTotalTimeoutConstant = 50;
    timeouts.ReadTotalTimeoutMultiplier = 10;
    timeouts.WriteTotalTimeoutConstant = 50;
    timeouts.WriteTotalTimeoutMultiplier = 10;

    if (!SetCommTimeouts(hSerial, &timeouts))
    {
        CloseHandle(hSerial);
        return INVALID_HANDLE_VALUE;
    }

    return hSerial;
}

void moverUnServo(HANDLE hSerial)
{
    int servo;
    int posicion;
    char comando[20];
    DWORD bytesEscritos;

    do
    {
        printf("Ingrese el número del servo que desea mover (1-6): ");
        scanf("%d", &servo);
        if (servo < 1 || servo > 6)
        {
            printf("Número de servo no válido. Inténtelo de nuevo.\n");
        }

    } while (servo < 1 || servo > 6);

    do
    {
        printf("Ingrese la posición deseada para el servo %d (0-180 grados): ", servo);
        scanf("%d", &posicion);
        if (posicion < 0 || posicion > 180)
        {
            printf("Angulo de posicion no válido. Inténtelo de nuevo.\n");
        }

    } while (posicion < 0 || posicion > 180);

    // Construir la cadena de comando
    snprintf(comando, sizeof(comando), "s%d,%d", servo, posicion);

    // Enviar la cadena al puerto serial
    if (!WriteFile(hSerial, comando, strlen(comando), &bytesEscritos, NULL))
    {
        printf("Error al enviar datos al puerto serial.\n");
    }
    else
    {
        printf("\n\n\n///////////Comando enviado: %s///////////\n\n\n", comando);
    }
}

void moverSeisServos(HANDLE hSerial)
{
    int posiciones[6];
    char comando[50] = "";
    char buffer[10];
    DWORD bytesEscritos;

    for (int i = 0; i < 6; i++)
    {
        do
        {
            printf("Ingrese la posición deseada para el servo %d (0-180 grados): ", i + 1);
            scanf("%d", &posiciones[i]);
            if (posiciones[i] < 0 || posiciones[i] > 180)
            {
                printf("Posición no válida para el servo %d. Inténtelo de nuevo.\n", i + 1);
            }

        } while (posiciones[i] < 0 || posiciones[i] > 180);
    }

    // Construir la cadena de comando
    for (int i = 0; i < 6; i++)
    {
        snprintf(buffer, sizeof(buffer), "%d", posiciones[i]);
        strcat(comando, buffer);
        if (i < 5)
        {
            strcat(comando, ",");
        }
    }

    // Enviar la cadena al puerto serial
    if (!WriteFile(hSerial, comando, strlen(comando), &bytesEscritos, NULL))
    {
        printf("Error al enviar datos al puerto serial.\n");
    }
    else
    {
        printf("\n\n\n///////////Comando enviado: %s///////////\n\n\n", comando);
    }
}
