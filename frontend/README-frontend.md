# Frontend - Sistema de Asistencias UBBJ
# Índice
- [Frontend - Sistema de Asistencias UBBJ](#frontend---sistema-de-asistencias-ubbj)
- [Índice](#índice)
  - [Arquitectura del Frontend](#arquitectura-del-frontend)
  - [Tecnologías del Frontend](#tecnologías-del-frontend)
  - [Instrucciones para el Frontend](#instrucciones-para-el-frontend)
    - [Desarrollo](#desarrollo)
      - [**Configurar Node.js con FNM**](#configurar-nodejs-con-fnm)
      - [**Para npm**](#para-npm)
      - [**Para pnpm**](#para-pnpm)
  - [Variables de Entorno](#variables-de-entorno)
  - [Librerías de JavaScript para el proyecto](#librerías-de-javascript-para-el-proyecto)

## Arquitectura del Frontend

El frontend es una **SPA (Single Page Application)** construida con **React** y **Vite**. Su estructura está organizada para separar la lógica de negocio, las vistas y los componentes reutilizables.

```plaintext
frontend/
├───public/          # Iconos, favicon y recursos estáticos públicos
├───src/             # Código fuente principal de la aplicación
│   ├───api/         # Cliente y funciones para consumir la API del backend
│   ├───assets/      # Imágenes, logos e iconografía local
│   ├───components/  # Componentes reutilizables de UI
│   ├───context/     # Contextos globales, como autenticación
│   ├───layouts/     # Layouts compartidos para la aplicación
│   ├───pages/       # Vistas o pantallas principales
│   ├───App.jsx      # Componente raíz con las rutas principales
│   ├───config.js    # Configuración centralizada de variables de entorno
│   ├───index.css    # Estilos globales de la aplicación
│   └───main.jsx     # Punto de entrada del frontend
├───base.env         # Plantilla de variables de entorno
├───eslint.config.js # Configuración de ESLint
├───index.html       # HTML base de Vite
├───jsconfig.json    # Configuración de alias para importaciones
├───package.json     # Dependencias y scripts del proyecto
├───vite.config.js   # Configuración de Vite y alias de rutas
└───README-frontend.md
```

La aplicación se apoya en estos bloques principales:

* `pages/`: Contienen las vistas completas del sistema, como login, dashboard, estudiantes, grupos, asistencias y reportes.
* `components/`: Encapsulan piezas reutilizables de interfaz, por ejemplo tarjetas, formularios, paneles y campos personalizados.
* `context/`: Administra el estado compartido, especialmente la autenticación y la sesión del usuario.
* `api/`: Centraliza la comunicación con el backend FastAPI.
* `layouts/`: Definen la estructura general de navegación y contenido de la aplicación.

## Tecnologías del Frontend

> El frontend se desarrolla con **Vite** y **React**. Para ejecutarlo, se recomienda usar **Node.js** administrado con **FNM (Fast Node Manager)** en una versión LTS compatible con Vite.

* **Framework de UI:** [React](https://react.dev/)
* **Renderizado:** [React DOM](https://react.dev/reference/react-dom)
* **Ruteo:** [React Router DOM](https://reactrouter.com/)
* **Componentes UI:** [React Bootstrap](https://react-bootstrap.github.io/)
* **Estilos base:** [Bootstrap](https://getbootstrap.com/)
* **Bundler / servidor de desarrollo:** [Vite](https://vite.dev/)
* **Linter:** [ESLint](https://eslint.org/)
* **Alias de rutas:** `@` apunta a `src/` mediante `vite.config.js` y `jsconfig.json`
* **Gestor de paquetes:** [pnpm](https://pnpm.io/)
* **Node.js:** [v24.14.1 LTS](https://nodejs.org/es)
* **Node.js Version Manager:** [FNM](https://github.com/Schniz/fnm)

## Instrucciones para el Frontend

### Desarrollo

> **Renombrar el archivo `base.env` a `.env`** o crear un archivo `.env` nuevo con las variables del proyecto.

La aplicación necesita la variable `VITE_API_BASE_URL` para conectarse con el backend. Si esa variable no existe, el frontend no arranca correctamente.

#### **Configurar Node.js con FNM**

1. Instalar FNM siguiendo la guía oficial

[Schniz/fnm](https://github.com/Schniz/fnm)

2. Instalar una versión LTS de Node.js

```bash
fnm install --lts
```

3. Activar la versión LTS instalada

```bash
fnm use --lts
```

4. Verificar la instalación

```bash
node -v
npm -v
```

#### **Para npm**

1. Clonar el repositorio

```bash
git clone https://github.com/<usuario-del-repositorio>/Sistema-De-Asistencias-UBBJ.git
```

2. Entrar a la carpeta del frontend

```bash
cd frontend
```

3. Configurar las variables de entorno

```bash
copy base.env .env
```

* En Windows, puedes usar `copy base.env .env`
* En macOS/Linux, puedes usar `cp base.env .env`

4. Editar el archivo `.env` y definir la URL base de la API

```bash
VITE_API_BASE_URL=http://127.0.0.1:8000
```

5. Instalar las dependencias

```bash
npm install
```

6. Ejecutar el servidor de desarrollo

```bash
npm run dev
```

7. Generar la versión de producción

```bash
npm run build
```

8. Previsualizar el build

```bash
npm run preview
```

9. Validar el código con ESLint

```bash
npm run lint
```

#### **Para pnpm**

1. Clonar el repositorio

```bash
git clone https://github.com/<usuario-del-repositorio>/Sistema-De-Asistencias-UBBJ.git
```

2. Entrar a la carpeta del frontend

```bash
cd frontend
```

3. Configurar las variables de entorno

```bash
copy base.env .env
```

4. Editar el archivo `.env` y definir la URL base de la API

```bash
VITE_API_BASE_URL=http://127.0.0.1:8000
```

5. Instalar las dependencias

```bash
pnpm install
```

6. Ejecutar el servidor de desarrollo

```bash
pnpm dev
```

7. Generar la versión de producción

```bash
pnpm build
```

8. Previsualizar el build

```bash
pnpm preview
```

9. Validar el código con ESLint

```bash
pnpm lint
```

## Variables de Entorno

El frontend usa la siguiente variable principal:

* `VITE_API_BASE_URL`: URL base del backend FastAPI, por ejemplo `http://127.0.0.1:8000`

## Librerías de JavaScript para el proyecto

* `react`: base de la interfaz de usuario.
* `react-dom`: integración de React con el DOM del navegador.
* `react-router-dom`: navegación entre vistas y rutas protegidas.
* `react-bootstrap`: componentes visuales listos para usar con Bootstrap.
* `bootstrap`: estilos y utilidades CSS base.
* `vite`: desarrollo local, empaquetado y build de producción.
* `eslint`: análisis estático y validación del código JavaScript.
