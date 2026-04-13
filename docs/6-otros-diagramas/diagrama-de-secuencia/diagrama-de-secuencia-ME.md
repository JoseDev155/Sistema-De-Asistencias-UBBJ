# Diagrama de Secuencia

Hecho en [Eraser](https://eraser.io/):

![Diagrama de Secuencia](./Diagrama%20de%20Secuencia%20-%20UBBJ.png)

```eraser
// 1. Definicion de Actores
User [label: "Usuario / Admin", shape: person]
Frontend [label: "Frontend (React)", icon: react]
Backend [label: "Backend (FastAPI)", icon: fastapi]
DB [label: "PostgreSQL", icon: postgresql]

// FLUJO 1: LOGIN
User > Frontend: Ingresa credenciales
Frontend > Backend: POST /login
Backend > Backend: Validar credenciales y generar JWT
Backend > DB: Consultar usuario
DB > Backend: Retorna datos de perfil
Backend > Frontend: Retorna Token JWT
Frontend > User: Redirige al Dashboard

// FLUJO 2: ASISTENCIA
User > Frontend: Confirma su entrada
Frontend > Backend: POST /asistencia (JWT)
Backend > Backend: Calcular puntualidad y lógica
Backend > DB: Guardar registro de asistencia
DB > Backend: Confirmacion de guardado
Backend > Frontend: JSON status puntualidad
Frontend > User: Muestra mensaje de exito

// FLUJO 3: REPORTES
User > Frontend: Accede a modulo reportes
Frontend > Backend: GET /reportes (Filtros JWT)
Backend > DB: SELECT registros filtrados
DB > Backend: Retorna lista de asistencias
Backend > Backend: Procesar metricas y estadisticas
Backend > Frontend: Datos procesados JSON
Frontend > User: Renderiza graficas y metricas
```
