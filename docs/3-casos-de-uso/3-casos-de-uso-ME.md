# Casos de Uso

>Usaré el primer diagrama, ya que es el que yo ya he entregado en proyectos anteriores, pero pueden usar cualquiera

## Documento

En el documento `Casos de uso - UBBJ.docx` se encuentran descritos los casos de uso del sistema, con sus respectivos actores. El formato es de una plantilla de un proyecto anterior,
mientras que la redacción se hizo con **Claude**.

Este se unirá posteriormente al **Manual del Analista**.

## Diagrama de Casos de Uso v1

Hecho en [Lucidchart](https://www.lucidchart.com/pages):

![Diagrama de Casos de Uso](./diagramas/Diagrama%20de%20casos%20de%20uso%20General%20-%20UBBJ.png)

## Diagrama de Casos de Uso v2

Hecho en [Eraser](https://eraser.io/):

![Diagrama de Casos de Uso](./diagramas/Diagrama%20de%20casos%20de%20uso%20General%20-%20UBBJ%20-%20Eraser.png)

```eraser
// --- ACTORES DE ENTRADA (IZQUIERDA) ---
Profesor_In [shape: person, label: "Profesor"]
Admin_In [shape: person, label: "Administrador"]

// --- ACTORES DE SALIDA (DERECHA) ---
Profesor_Out [shape: person, label: "Profesor"]
Admin_Out [shape: person, label: "Administrador"]
Estudiante [shape: person, label: "Estudiante (Sujeto Pasivo)"]

// --- SISTEMA (CENTRO) ---
group "Sistema de Asistencia UBBJ" {
  
  // Bloque 1: Acceso
  UC1 [label: "Ingresa al panel del sistema", shape: oval]
  UC_Res1 [label: "Consulta grupos y horarios", shape: oval]
  
  // Bloque 2: Operación de Asistencia
  UC2 [label: "Registra la asistencia (Manual/Excel)", shape: oval]
  UC_Res2 [label: "Recibe estatus de puntualidad", shape: oval]
  UC_Res3 [label: "Confirma guardado en DB", shape: oval]
  
  // Bloque 3: Administración y Reportes
  UC3 [label: "Accede a la sección de métricas", shape: oval]
  UC_Res4 [label: "Consulta estadísticas globales", shape: oval]
  UC_Res5 [label: "Recibe reporte (PDF/Excel)", shape: oval]
  
  // Bloque 4: Gestión
  UC4 [label: "Actualiza datos de docentes", shape: oval]
  UC_Res6 [label: "Confirma cambios de usuario", shape: oval]
}

// --- RELACIONES DE ENTRADA (IZQUIERDA -> SISTEMA) ---
Profesor_In > UC1
Profesor_In > UC2

Admin_In > UC1
Admin_In > UC3
Admin_In > UC4

// --- RELACIONES DE SALIDA (SISTEMA -> DERECHA) ---
UC_Res1 > Profesor_Out
UC_Res2 > Profesor_Out
UC_Res3 > Profesor_Out

UC_Res4 > Admin_Out
UC_Res5 > Admin_Out
UC_Res6 > Admin_Out

// --- RELACIÓN CON EL ALUMNO ---
UC_Res2 > Estudiante: "Efecto de registro sobre"
UC_Res5 > Estudiante: "Incluye historial de"
```