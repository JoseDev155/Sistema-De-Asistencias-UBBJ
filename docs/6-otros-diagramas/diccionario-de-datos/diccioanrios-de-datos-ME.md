# Diccionarios de datos

El documento `Diccionario de Datos - UBBJ.docx` contiene el diccionario de datos completo, con cada tabla, sus atributos, tipos de datos, claves primarias, claves foráneas y restricciones.

El documento se hizo usando el script de la Base de Datos y con **Claude** para redactar el documento.

Esto se unirá en el **Manual del Analista** más adelante.

## Notas sobre claves únicas compuestas

* Tabla `career_signatures`: `UNIQUE(signature_id, career_id)` evita duplicar la misma firma dentro de la misma carrera. Un par firma-carrera sólo puede existir una vez.
* Tabla `enrollments`: `UNIQUE(student_id, group_id)` evita que un estudiante se inscriba dos veces en el mismo grupo. Un estudiante sólo puede tener una inscripción por grupo.
* Tabla `attendances`: `UNIQUE(enrollment_id, attendance_date)` evita registros de asistencia duplicados para la misma inscripción en un mismo día.