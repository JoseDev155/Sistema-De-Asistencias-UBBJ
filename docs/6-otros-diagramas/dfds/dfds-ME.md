# DFDs

Hechos en [Eraser](https://eraser.io/).

## DFD Nivel 0: Diagrama de Contexto

![DFD Nivel 0](./DFD%20Nivel%200%20-%20UBBJ.png)

```eraser
// Entidades Externas
Usuario [shape: rectangle]
Administrador [shape: rectangle]
SistemaAsistencia [label: "Sistema de Asistencia - UBBJ (Proceso 0)", shape: oval]

// Flujos de Datos
Usuario > SistemaAsistencia: Credenciales, Registro de Asistencia
SistemaAsistencia > Usuario: Confirmación, Estatus de puntualidad

Administrador > SistemaAsistencia: Solicitud de Reportes, Filtros
SistemaAsistencia > Administrador: Reportes PDF/Excel, Métricas
```

## DFD Nivel 1: Diagrama de Nivel 1 con Módulos Principales

![DFD Nivel 1](./DFD%20Nivel%201%20-%20UBBJ.png)

```eraser
// --- ENTIDADES EXTERNAS ---
Usuario [shape: rectangle]
Administrador [shape: rectangle]

// --- ALMACENES DE DATOS (DATASTORES) ---
D1_Usuarios [label: "D1: Tabla Usuarios (Credenciales/Roles)", shape: storage]
D2_Asistencias [label: "D2: Tabla Asistencias (Registros/Métricas)", shape: storage]
D3_Archivos [label: "D3: Sistema de Archivos (Uploads/Exports)", shape: storage]
D4_Logs [label: "D4: Logs del Sistema (Monitoreo)", shape: storage]

// --- PROCESOS DETALLADOS (BURBUJAS) ---

// Módulo de Acceso
P1_1 [label: "2.1 Validar JWT & Permisos", shape: oval]
P1_2 [label: "2.2 Verificar Credenciales", shape: oval]

// Módulo de Lógica de Asistencia
P2_1 [label: "2.3 Saneamiento de Datos Entrada", shape: oval]
P2_2 [label: "2.4 Motor de Cálculo de Puntualidad", shape: oval]
P2_3 [label: "2.5 Registro de Evento en DB", shape: oval]

// Módulo de Archivos y Reportes
P3_1 [label: "2.6 Procesador de Carga Excel", shape: oval]
P3_2 [label: "2.7 Generador de Reportes y Exportación", shape: oval]
P3_3 [label: "2.8 Analizador de Métricas", shape: oval]

// --- FLUJOS DE DATOS (EL VIAJE DE LA INFORMACIÓN) ---

// Flujo de Autenticación
Usuario > P1_2: Formulario Login (JSON)
P1_2 <> D1_Usuarios: Hash de Password / Rol
P1_2 > Usuario: Token JWT Firmado
P1_2 > D4_Logs: Registro de Intento de Acceso

// Flujo de Registro de Asistencia
Usuario > P1_1: Petición Asistencia + JWT
P1_1 > P2_1: ID_Usuario Validado
P2_1 > P2_2: Datos Limpios + Timestamp
P2_2 <> D2_Asistencias: Horarios Configurables
P2_2 > P2_3: Resultado (Puntual/Retardo)
P2_3 > D2_Asistencias: Insert Registro
P2_3 > Usuario: Respuesta JSON de confirmación

// Flujo de Carga Masiva (Excel)
Administrador > P3_1: Archivo .xlsx (Uploads)
P3_1 > D3_Archivos: Guardar Archivo Físico
P3_1 > P2_3: Datos Extraídos para Inserción Masiva

// Flujo de Reportes y Estadísticas
Administrador > P1_1: Solicitud de Reporte + JWT
P1_1 > P3_3: Permiso Admin Validado
P3_3 <> D2_Asistencias: Datos Históricos
P3_3 > P3_2: Datos Agregados (Cómputo)
P3_2 > D3_Archivos: Crear PDF/Excel Temporal
P3_2 > Administrador: Descarga de Reporte / Dashboard
```

## DFD Nivel 2: Detalle de Procesos Internos

![DFD Nivel 2](./DFD%20Nivel%202%20-%20UBBJ.png)

```eraser
// --- ENTIDADES EXTERNAS ---
Usuario [shape: rectangle]
Administrador [shape: rectangle]

// --- ALMACENES DE DATOS (DATASTORES) ---
D1_Usuarios [label: "D1: Tabla Usuarios (Credenciales/Roles)", shape: storage]
D2_Asistencias [label: "D2: Tabla Asistencias (Registros/Métricas)", shape: storage]
D3_Archivos [label: "D3: Sistema de Archivos (Uploads/Exports)", shape: storage]
D4_Logs [label: "D4: Logs del Sistema (Monitoreo)", shape: storage]

// --- PROCESOS DETALLADOS (BURBUJAS) ---

// Módulo de Acceso
P1_1 [label: "2.1 Validar JWT & Permisos", shape: oval]
P1_2 [label: "2.2 Verificar Credenciales", shape: oval]

// Módulo de Lógica de Asistencia
P2_1 [label: "2.3 Saneamiento de Datos Entrada", shape: oval]
P2_2 [label: "2.4 Motor de Cálculo de Puntualidad", shape: oval]
P2_3 [label: "2.5 Registro de Evento en DB", shape: oval]

// Módulo de Archivos y Reportes
P3_1 [label: "2.6 Procesador de Carga Excel", shape: oval]
P3_2 [label: "2.7 Generador de Reportes y Exportación", shape: oval]
P3_3 [label: "2.8 Analizador de Métricas", shape: oval]

// --- FLUJOS DE DATOS (EL VIAJE DE LA INFORMACIÓN) ---

// Flujo de Autenticación
Usuario > P1_2: Formulario Login (JSON)
P1_2 <> D1_Usuarios: Hash de Password / Rol
P1_2 > Usuario: Token JWT Firmado
P1_2 > D4_Logs: Registro de Intento de Acceso

// Flujo de Registro de Asistencia
Usuario > P1_1: Petición Asistencia + JWT
P1_1 > P2_1: ID_Usuario Validado
P2_1 > P2_2: Datos Limpios + Timestamp
P2_2 <> D2_Asistencias: Horarios Configurables
P2_2 > P2_3: Resultado (Puntual/Retardo)
P2_3 > D2_Asistencias: Insert Registro
P2_3 > Usuario: Respuesta JSON de confirmación

// Flujo de Carga Masiva (Excel)
Administrador > P3_1: Archivo .xlsx (Uploads)
P3_1 > D3_Archivos: Guardar Archivo Físico
P3_1 > P2_3: Datos Extraídos para Inserción Masiva

// Flujo de Reportes y Estadísticas
Administrador > P1_1: Solicitud de Reporte + JWT
P1_1 > P3_3: Permiso Admin Validado
P3_3 <> D2_Asistencias: Datos Históricos
P3_3 > P3_2: Datos Agregados (Cómputo)
P3_2 > D3_Archivos: Crear PDF/Excel Temporal
P3_2 > Administrador: Descarga de Reporte / Dashboard
```
