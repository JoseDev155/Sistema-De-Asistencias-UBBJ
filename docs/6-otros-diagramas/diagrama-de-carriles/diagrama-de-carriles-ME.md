# Diagrama de Carriles - Swimlane

Hecho en [Eraser](https://eraser.io/):

![Diagrama de Carriles](./diagramas/Diagrama%20de%20Carriles%20Swimlane%20-%20UBBJ.png)

```eraser
// 1. Definición de la estructura de carriles
pool sistema-Asistencia {
  lane "Usuario o Admin" {
    U1 [label: "Ingresa Credenciales"]
    U2 [label: "Confirma Asistencia"]
    U3 [label: "Solicita Reportes"]
  }
  lane "Frontend (React)" {
    F1 [label: "Petición Login"]
    F2 [label: "Petición Asistencia"]
    F3 [label: "Renderiza Interfaz"]
  }
  lane "Backend (FastAPI)" {
    B1 [label: "Valida JWT y Negocio"]
    B2 [label: "Procesa Métricas"]
  }
  lane "Base de Datos (Postgres)" {
    D1 [label: "Consulta y Guardado"]
  }
}

// 2. Definición de los flujos de flechas
U1 -> F1
F1 -> B1
B1 -> D1
D1 -> B1: Datos usuario
B1 -> F1: Token JWT
F1 -> U1: Dashboard

U2 -> F2
F2 -> B1: Datos + JWT
B1 -> D1: Insert Registro
D1 -> B1: OK
B1 -> F2: Estatus
F2 -> U2: Éxito

U3 -> F3
F3 -> B2
B2 -> D1: Select
D1 -> B2: Registros
B2 -> F3: JSON Procesado
F3 -> U3: Gráficos
```
