# Diagramas MER-MR y de Clases

>Este documento son mis notas, no es entregable, solo los diagramas ER y de clases son entregables
>Sólo es para una breve explicación si es que les sirve :p

>[!IMPORTANT]
>El diagrama MER no se hizo, ya que el MER es un diagrama que muestra las tablas con sus atributos de forma mas gráfica, se hacía muy grande y muy engorroso hacerlo.
>Es como los bosquejos inciales que anexe pero más detallado, por lo que no lo haré. Lo siento :(

## MR y MER
El MR (**Modelo Relacinal**) es una representación gráfica de la estructura de una base de datos, mostrando las entidades, sus atributos y las relaciones entre ellas.

En el contexto del **Sistema de Asistencias de la UBBJ**, el MER incluiría entidades como "Estudiante", "Profesor", "Asignatura", "Grupo",
"Ciclo Académico", entre otras, y las relaciones entre ellas, como "Un estudiante se inscribe en un grupo" o "Un profesor imparte una asignatura".

>Se hizo en inglés por convención :P

### Bosquejos iniciales

Fue un bosquejo rápido para tener una idea de cómo se relacionan las entidades, ya que si no me salía bien, no quería estar corrigiendo a cada rato.

Además, en el caso que saliera bien, luego tenía que hacer un proceso llamado **Normalización**, que en resumen, es un proceso para eliminar la redundancia de datos y duplicidades en las tablas de la base de datos.

Pero al final si salió bien, Gemini únicamente me dio correción de tipos de datos y agregar 2 tablas intermedias para eliminar las duplicidades.
>A que si soy bueno programando ¿no? :p

Únicamente use llaves primarias (**PK**s), llaves foráneas (**FK**s) y 1 que 2 atributos, como dije, solo era un bosquejo rápido para tener una idea de cómo se relacionan las entidades, no me preocupé por los otros atributos ni nada:

![Bosquejo - Diagrama de BD](./diagrama-mer-mr/bosquejo-ER-workflow-light.png)

>Se hizo en **Excalidraw**

### Modelo Relacional (MR)

![Modelo Relacional](./diagrama-mer-mr/Modelo%20Relacional%20MR%20-%20UBBJ.png)

## Diagrama de Clases

El diagrama de clases es una representación gráfica de las clases, sus atributos, métodos y las relaciones entre ellas en un sistema orientado a objetos (POO).

![Diagrama de Clases](./diagrama-de-clases/plantuml_export_ubbj.png)

>Digrama hecho en **PlantText**, un editor UML en línea

El diagrama lo hizo Gemini, ya que sólo le pasé el diagrama MR, algunas de las funciones que tendrá el sistema y me dió el código para pegarlo en
PlantText.

El código esta aquí en [diagrama de clases UML](./diagrama-de-clases/plantuml_export_ubbj.puml), obvio que conforme avanza el desarrollo puede cambiar, pero de forma rápida, el código se ve así:

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam packageStyle rectangle

package "User Management" {
    class Role {
        - id: Integer
        - name: String
        - description: String
        - is_active: Boolean
        + getPermissions(): List
    }

    class User {
        - id: String
        - first_name: String
        - last_name: String
        - email: String
        - password: Hash
        - is_active: Boolean
        + authenticate(password: String): Boolean
        + getFullName(): String
    }
}

package "Academic Structure" {
    class Signature {
        - id: String
        - name: String
        - description: String
        - is_active: Boolean
    }

    class Career {
        - id: Integer
        - name: String
        - description: String
        - is_active: Boolean
    }

    class SignatureCareer {
        - id: String
        ' Relación N:N entre Carrera y Materia
    }

    class AcademicCycle {
        - id: Integer
        - cycle_name: String
        - cycle_year: Date
    }

    class Group {
        - id: String
        - name: String
        + getScheduleForDay(day: Integer): Schedule
        + getAttendanceReport(): DataFrame
    }
}

package "Attendance Engine" {
    class Schedule {
        - id: String
        - day_of_week: SmallInt
        - start_time: Time
        - end_time: Time
        - max_entry_minutes: Integer
        - minutes_to_be_late: Integer
        + isValidTime(check_time: Time): Boolean
    }

    class Student {
        - id: String
        - first_name: String
        - last_name: String
        - email: String
        - enrollment_date: Date
        - is_active: Boolean
        + getGlobalAttendance(): Float
    }

    class Enrollment {
        - id: Integer
        - enrollment_date: Date
        + getStudentAttendanceInGroup(): Float
    }

    class Attendance {
        - id: Integer
        - attendance_date: Date
        - status: Enum
        - notes: String
        + calculateStatus(arrivalTime: DateTime, schedule: Schedule): Enum
    }
}

' Relaciones de Asociación
Role "1" -- "0..*" User : assigned_to >
Signature "1" -- "0..*" SignatureCareer
Career "1" -- "0..*" SignatureCareer

SignatureCareer "1" -- "0..*" Group : belongs_to >
User "1" -- "0..*" Group : teaches >
AcademicCycle "1" -- "0..*" Group : active_in >

Group "1" *-- "1..*" Schedule : contains >
Group "1" -- "0..*" Enrollment : has >
Student "1" -- "0..*" Enrollment : owns >

Enrollment "1" *-- "0..*" Attendance : records >

@enduml
```