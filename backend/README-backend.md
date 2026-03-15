# Backend - Sistema de Asistencias UBBJ
## Descripción del Backend

>Se usó **Anaconda** como entorno de desarrollo para gestionar las dependencias y facilitar la instalación de paquetes necesarios para el desarrollo del backend. Pero también se puede usar un entorno virtual tradicional con `venv` o `virtualenv` si se prefiere, siempre y cuando la versión de Python que se use sea compatible o sea la misma que la utilizada en el proyecto.

* **Base de Datos:** PostgreSQL
* **Framework:** FastAPI
* **Versión de Python:** `3.*` con Anaconda

## Instrucciones para el Backend
### Desarrollo
#### Para Anaconda

1. Clonar el repositorio

```bash
git clone https://github.com/<usuario>/Sistema-De-Asistencias-UBBJ.git
```

2. Crear un entorno virtual con Anaconda

```bash
conda create -n asistencias-ubbj python=3.10
```

3. Activar el entorno virtual

```bash
conda activate asistencias-ubbj
```

4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

5. Configurar la base de datos PostgreSQL y actualizar las variables de entorno en el archivo `.env` con las credenciales correspondientes.
6. Ejecutar el servidor de desarrollo

```bash
uvicorn main:app --reload
```

#### Para Python

1. Clonar el repositorio

```bash
git clone https://github.com/<usuario>/Sistema-De-Asistencias-UBBJ.git
```

2. Crear un entorno virtual

```bash
python -m venv asistencias-ubbj
```

3. Activar el entorno virtual

* **En Windows:**

```bash
asistencias-ubbj\Scripts\activate
```

* **En macOS/Linux:**

```bash
source asistencias-ubbj/bin/activate
```

4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

5. Configurar la base de datos PostgreSQL y actualizar las variables de entorno en el archivo `.env` con las credenciales correspondientes.

6. Ejecutar el servidor de desarrollo

```bash
uvicorn main:app --reload
```

## Librerías de Python para el análisis de datos

* `pandas`: para la manipulación y análisis de datos, especialmente útil para manejar los datos de asistencias y generar reportes.
* `numpy`: para operaciones numéricas y manejo de arrays, que pueden ser útiles para cálculos relacionados con la puntualidad y los retardos.
* `openpyxl`: para leer y escribir archivos Excel, lo que facilita la importación de datos de asistencias desde archivos `.xlsx` y la generación de reportes en formato Excel.