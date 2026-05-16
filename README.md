# FieldSense: Sistema de Monitoreo IoT de Extremo a Extremo

**FieldSense** es una solución integral diseñada para la captura, procesamiento y visualización de datos ambientales en tiempo real. Este proyecto resuelve la desconexión común entre el hardware de bajo nivel y las aplicaciones web modernas, estableciendo un flujo de datos seguro, bidireccional y persistente.

## 🛠️ Arquitectura Técnica

El sistema se divide en tres capas fundamentales que garantizan una operatividad robusta:

### 1. Capa de Hardware (Firmware)
* **Microcontrolador:** ESP32.
* **Sensor:** DHT22 (Humedad y Temperatura).
* **Protocolo de Comunicación:** HTTP/HTTPS con empaquetado de datos en formato **JSON** mediante la librería `ArduinoJson`.
* **Características Especiales:** * Implementación de `WiFiClientSecure` para conexiones seguras.
    * Uso de cabeceras personalizadas (`Bypass-Tunnel-Reminder`) para el bypass de túneles remotos como LocalTunnel.
    * Lógica de transmisión eficiente con reintentos automáticos en caso de pérdida de conexión.
    * <img width="439" height="629" alt="image" src="https://github.com/user-attachments/assets/8ea82376-3b27-4e7b-aae7-bf1c6345f35a" />


### 2. Capa de Servidor (Backend)
* **Entorno:** Python 3.10+ / Flask.
* **Persistencia:** Base de datos **MySQL** gestionada a través de **SQLAlchemy**.
* **Seguridad:** Configuración de políticas **CORS** para habilitar la comunicación segura con el frontend alojado en dominios externos.
* **API REST:** Endpoints optimizados para la recepción de lecturas (`POST`) y la entrega de históricos formateados para visualización dinámica (`GET`).

### 3. Capa de Usuario (Frontend)
* **Tecnologías:** HTML5, **Tailwind CSS** para un diseño responsivo y JavaScript Vanilla.
* **Visualización de Datos:** Implementación de gráficas dinámicas mediante **Chart.js**.
* **Interactividad:** El dashboard se actualiza automáticamente cada 5 segundos consumiendo la API, permitiendo un monitoreo en tiempo real sin recargar el sitio.

## 🚀 Proyecto
* **Integración Full-Stack:** Conexión exitosa y estable desde el sensor físico hasta la interfaz en la nube.
* **Simulación de Entorno:** Desarrollo de un script de simulación en Python que emula el comportamiento de un ESP32, permitiendo realizar pruebas de carga y debugging del backend sin necesidad de hardware físico.
* **Seguridad Fail-Safe:** Arquitectura diseñada para manejar excepciones de red y asegurar la integridad de la base de datos ante peticiones malformadas.
* **Escalabilidad:** Sistema preparado para la integración de múltiples nodos de sensores simultáneos.

## 📂 Estructura de Archivos
* `/embedded`: Código fuente para el ESP32 (C++/Arduino).
* `/backend`: API REST desarrollada en Flask (`Cerebro.py`).
* `/database`: Esquema relacional y scripts de creación de tablas (`Datos.sql`).
* `/frontend`: Dashboard web con integración de gráficas.
* `/tools`: Script de simulación virtual de hardware (`Simulador.py`).

## ⚙️ Configuración y Uso

### Base de Datos
Ejecutar el script SQL para generar la estructura necesaria: mysql

#Backend
Instalar dependencias y ejecutar el servidor:

Bash
pip install flask flask-sqlalchemy flask-cors pymysql requests
python backend/Cerebro.py
Simulación
Para probar el sistema sin un ESP32 físico:

Bash
python tools/Simulador.py
🌐 Despliegue Actual
El frontend se encuentra disponible y operativo en:

🔗 https://hadwareysoftwarefullstack.netlify.app/

Nota: Este proyecto ha sido desarrollado con un enfoque estricto en resultados funcionales, eficiencia de código y arquitectura de sistemas distribuidos.
