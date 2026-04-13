# Diagrama de Actividades

Hecho en [Eraser](https://eraser.io/):

![Diagrama de Actividades](./Diagrama%20de%20Actividades%20-%20UBBJ.png)

```eraser
// Nodos de inicio y fin
Start [shape: circle, fill: black, label: "Inicio"]
End [shape: circle, fill: black, label: "Fin"]

// Actividades iniciales
Login [label: "Ingresar Credenciales"]
Auth [label: "Validar en Backend (FastAPI)"]
Decision_Auth [shape: diamond, label: "¿Datos válidos?"]
Error_Login [label: "Mostrar Error de Acceso"]
Dashboard [label: "Cargar Dashboard (React)"]
Decision_Rol [shape: diamond, label: "¿Rol de Usuario?"]

// Flujo Profesor
Prof_Menu [label: "Seleccionar Materia y Grupo"]
Decision_Metodo [shape: diamond, label: "¿Método de Registro?"]
Manual [label: "Marcar Alumnos en Lista UI"]
Upload_Excel [label: "Subir Archivo .xlsx"]
Process_Asist [label: "Calcular Puntualidad y Guardar"]

// Flujo Administrador
Admin_Menu [label: "Acceder a Métricas y Reportes"]
Filters [label: "Aplicar Filtros (Fecha/Carrera)"]
Generate_Report [label: "Generar Reporte (PDF/Excel)"]

// Conexiones de flujo
Start > Login
Login > Auth
Auth > Decision_Auth

// Lógica de decisión Login
Decision_Auth > Error_Login: No
Error_Login > Login
Decision_Auth > Dashboard: Sí

// Lógica de Rol
Dashboard > Decision_Rol
Decision_Rol > Prof_Menu: Profesor
Decision_Rol > Admin_Menu: Administrador

// Lógica de Registro (Profesor)
Prof_Menu > Decision_Metodo
Decision_Metodo > Manual: Manual
Decision_Metodo > Upload_Excel: Excel
Manual > Process_Asist
Upload_Excel > Process_Asist
Process_Asist > End

// Lógica de Reportes (Admin)
Admin_Menu > Filters
Filters > Generate_Report
Generate_Report > End
```
