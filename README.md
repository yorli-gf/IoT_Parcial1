# Sistema de Monitoreo de Temperatura con Raspberry Pi Pico W y Sensor LM35

Este proyecto consiste en un sistema de monitoreo de temperatura basado en Internet de las Cosas (IoT) utilizando una Raspberry Pi Pico W y un sensor LM35. Los datos de temperatura se envían a la plataforma ThingSpeak para su visualización y análisis en tiempo real. Además, se utiliza MathWorks para calcular el promedio de temperatura y generar alertas si se supera un umbral predefinido.

## Tecnologías Utilizadas
- **Raspberry Pi Pico W**: Placa de desarrollo utilizada para la captura y procesamiento de datos.
- **Sensor LM35**: Sensor de temperatura que mide la temperatura ambiente en grados Celsius.
- **ThingSpeak**: Plataforma en la nube para almacenar y visualizar datos en tiempo real.
- **MathWorks**: Herramienta utilizada en ThingSpeak para análisis de datos y generación de alertas.
- **MicroPython**: Lenguaje de programación utilizado para desarrollar el código en la Raspberry Pi Pico W.

## Configuración del Hardware
Para conectar el sensor LM35 a la Raspberry Pi Pico W, sigue estos pasos:
1. **VCC**: Conecta el pin VCC del LM35 al pin VBUS (5V) de la Raspberry Pi Pico W (pin 40).
2. **GND**: Conecta el pin GND del LM35 al pin GND de la Raspberry Pi Pico W.
3. **Salida (Vout)**: Conecta el pin de salida del LM35 al pin GP26 (ADC0) de la Raspberry Pi Pico W.

## Instalación y Configuración

### Requisitos Previos
- Raspberry Pi Pico W.
- Sensor LM35.
- Conexión a Internet Wi-Fi.
- Cuenta en ThingSpeak (gratuita).
- Entorno de desarrollo para MicroPython (como Thonny IDE).

### Pasos para la Instalación
1. **Configura ThingSpeak**:
   - Crea un nuevo canal en ThingSpeak.
   - Anota la **API Key** del canal, ya que la necesitarás para enviar datos desde la Raspberry Pi Pico W.

2. **Carga el Código en la Raspberry Pi Pico W**:
   - Descarga o copia el código en MicroPython proporcionado en este repositorio.
   - Abre el código en un entorno de desarrollo como Thonny IDE.
   - Modifica las siguientes variables en el código con tus datos:
     - `SSID`: Nombre de tu red Wi-Fi.
     - `PASSWORD`: Contraseña de tu red Wi-Fi.
     - `API_KEY`: API Key de tu canal en ThingSpeak.
   - Carga el código en la Raspberry Pi Pico W.

3. **Ejecuta el Código**:
   - Una vez cargado el código, la Raspberry Pi Pico W se conectará a la red Wi-Fi y comenzará a enviar datos de temperatura a ThingSpeak cada 180 segundos.

### Uso
- **Visualización de Datos**:
  - Accede a tu canal en ThingSpeak para ver los datos de temperatura en tiempo real.
  - Configura gráficas y alertas según tus necesidades.

- **Análisis de Datos**:
  - Utiliza MathWorks en ThingSpeak para calcular el promedio de temperatura en los últimos 10 datos recibidos.
  - Configura alertas para recibir notificaciones si la temperatura supera un umbral predefinido (por ejemplo, 35°C).

## Estructura del Repositorio
- **/src**: Contiene el código en MicroPython para la Raspberry Pi Pico W.
- **/docs**: Documentación adicional, imágenes y diagramas del proyecto.
- **README.md**: Este archivo, con la descripción del proyecto, instrucciones de instalación y uso.

