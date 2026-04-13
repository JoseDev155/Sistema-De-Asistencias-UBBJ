# Diagrama de Estado

Hecho en [Eraser](https://eraser.io/):

![Diagrama de Estado](./Diagrama%20de%20Estado%20-%20UBBJ.png)

```eraser
// --- CONFIGURACIÓN VISUAL (ESTILO CIAN) ---
direction: right

// Nodos de inicio y fin
Inicio [shape: circle, fill: "#5ed3c4", label: "Inicio"]
Fin [shape: circle, stroke: "#5ed3c4", stroke-width: 6, label: "Fin"]

// Estados del Proceso
Apertura [label: "Sesión de Clase", shape: rounded-rectangle, fill: "#5ed3c4"]
Registro [label: "Registro de Alumno", shape: rounded-rectangle, fill: "#5ed3c4"]
Analisis [label: "Análisis de Horario", shape: rounded-rectangle, fill: "#5ed3c4"]
Estatus [label: "Asignación de Estatus", shape: rounded-rectangle, fill: "#5ed3c4"]

// Estados Finales (Basados en el ENUM de tu BD)
Presente [label: "Presente", shape: rounded-rectangle, fill: "#5ed3c4"]
Tardio [label: "Tardío", shape: rounded-rectangle, fill: "#5ed3c4"]
Ausente [label: "Ausente", shape: rounded-rectangle, fill: "#5ed3c4"]
Justificado [label: "Justificado", shape: rounded-rectangle, fill: "#5ed3c4"]
Salida [label: "Salida Temprana", shape: rounded-rectangle, fill: "#5ed3c4"]

// --- TRANSICIONES Y LÓGICA ---
Inicio > Apertura
Apertura > Registro: "Captura datos"
Registro > Analisis: "Valida llegada"
Analisis > Estatus: "Compara start_time"

// Ramificaciones del Estatus
Estatus > Presente: "En tiempo"
Estatus > Tardio: "Fuera de tolerancia"
Estatus > Ausente: "Sin registro"

// Transiciones Secundarias (Como el 'Dormitorio' de tu ejemplo)
Ausente > Justificado: "Presenta nota"
Presente > Salida: "Retiro previo"
Tardio > Salida: "Retiro previo"

// Cierre de flujo hacia el nodo final
Presente > Fin
Tardio > Fin
Justificado > Fin
Salida > Fin
Ausente > Fin
```
