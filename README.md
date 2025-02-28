# ProyectoP1_Lot
Este proyecto utiliza una  Raspberry Pi Pico W  para medir la temperatura usando su sensor interno
1. Configuración del Hardware (sin LM35)
Raspberry Pi Pico W: No necesitas conectar ningún sensor externo. Usarás el sensor de temperatura interno de la Pico W.
Conéctate a la red Wi-Fi para enviar los datos de temperatura.

2. Programación en MicroPython
Conectar a Wi-Fi: Utiliza las librerías de MicroPython para conectarte a la red Wi-Fi.
Leer la temperatura interna: Usa el ADC de la Raspberry Pi Pico W para acceder al sensor de temperatura interno. y colaca tu codigo.

3. Visualización en ThingSpeak
Configurar ThingSpeak: Crea un canal en ThingSpeak y configúralo para recibir datos en el "Field 1".
Crear Gráficas: En ThingSpeak, habilita los gráficos para visualizar la temperatura en tiempo real.
Configurar MathWorks: Configura la aplicación MathWorks para realizar análisis, como el cálculo del promedio de los últimos 10 datos y alertas de temperatura.
Promedio de temperatura: Usa el bloque de análisis en ThingSpeak para calcular el promedio.
Alerta de temperatura: Configura un "Trigger" para enviar alertas cuando la temperatura exceda 35°C.

5. Documentación y GitHub
