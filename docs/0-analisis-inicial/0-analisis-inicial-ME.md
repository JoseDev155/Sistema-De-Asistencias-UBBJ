# Análisis Inicial
## Descripción del proyecto de GitHub (original)

>Sistema de asistencias para una institución educativa. Registra entradas, calcula puntualidad y retardos, genera reportes y estadísticas para supervisión administrativa. (En pagina web con login)

Por lo que entiendo, el sistema debe:
* Permitir a los usuarios registrarse e iniciar sesión.
  * Usuarios con diferentes roles (administradores, profesores, estudiantes) con permisos específicos.
  * Al ser un sistema de asistencias, se entiende que es para uso exclusivo de profesores y administradores, por lo que los estudiantes no tendrían acceso al sistema.
* Registrar las asistencias de los estudiantes, calculando la puntualidad y los retardos.
* Permitir gestionar estudiantes por sección, grupos o carreras.
* Generar reportes y estadísticas para supervisión administrativa.
* Tener una interfaz web intuitiva y fácil de usar.
* Garantizar la seguridad de los datos y la privacidad de los usuarios.
* **No hay datos aproximados del volumen de estudiantes que maneja la institución**

## NOTAS
### Consideraciones para los desarrolladores
* Se realizó pensando en que los "desarrolladores" del proyecto saben programar (por la carrera universitaria que cursan), pero no tienen conociemientos de desarrollo web.
* Desconozco la **documentación técnica** que se requiere para el proyecto, por lo que se hizo una documentación básica para cada sección, pero en base a la información que proporcioné pueden usarla para agregarla a su propia documentación.
* Desconozco el **formato de los reportes y estadísticas** que se requieren, por lo que se hizo un formato básico para cada uno, pero pueden agregar más detalles o formatos específicos según las necesidades del proyecto.
* Desconozco si se requiere un reporte de inter-ciclo (en mi país un semestre se divide en 3 ciclos, y cada ciclo tiene su propio reporte), por lo que se hizo un formato de **reporte semestral general**, pero pueden agregar un formato específico para cada ciclo si es necesario.
* Sólo hay instrucciones para **Desarrollo** (entorno local, nuestra propia computadora), no para **Producción** (servidor real), ya que no he realizado dicha tarea (en entornos serios), pero se pueden agregar posteriormente si es necesario.
* Se usó *Inglés* para los **nombres de las carpetas y archivos**, ya que es una práctica común en el desarrollo de software y facilita la colaboración con desarrolladores de diferentes regiones. Sin embargo, la documentación, los comentarios y mensajes de respuesta están en español para asegurar que sean accesibles para todos los miembros del equipo.

### Metodología de desarrollo
* Se usó la *metodología ágil* **Kanban** para el desarrollo del proyecto por la facilidad que ofrece.
* No se agregó información específica como **ruta crítica (CPM)**, historias de usuario y etc. Que son parte de la documentación requerida en proyectos de software, porque se asumió que por su carrera, no se los pidieron.
* Se usó la herramienta de gestión de proyectos **Asana** para organizar las tareas y el progreso del proyecto, aunque también se pueden usar otras herramientas similares como Jira, Asana, etc.
* Igualmente se dejó un [**Template** de *Excel*](./2-cronograma/) para la gestión de tareas, por si se prefiere una herramienta más tradicional, nunca han usado una metodología ágil o no quieren usar una herramienta de gestión de proyectos.

### Git/GitHub
* Se usó la plataforma de control de versiones **GitHub** para alojar el código fuente del proyecto, gestionar las ramas y realizar revisiones de código.
* Los **commits** se escribieron en español para mantener la coherencia con el idioma de la documentación y facilitar la comprensión de los cambios realizados.
* Las conveciones de nombres para los mensajes de commit siguen mi propio estilo, pero pueden adaptarlos a su propio estilo:
  * `Agregar`: para agregar nuevos archivos
  * `Nuevo/a`: para nuevas funcionalidades
  * `Corregir`: para corrección de errores
  * `Docs`: para cambios en la documentación
  * `Actualizar`: para actualizaciones generales sin nuevas funcionalidades
* Las ramas se nombraron de la siguiente manera:
  * `main`: rama principal, estable y lista para producción
    * `develop`: rama de desarrollo, donde se integran las nuevas funcionalidades antes de pasar a `main`
      * `<rama-específica>`: ramas para el desarrollo de nuevas funcionalidades específicas