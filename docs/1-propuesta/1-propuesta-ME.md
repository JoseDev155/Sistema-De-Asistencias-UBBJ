# Detalles de la Propuesta
## Sobre la propuesta

* Los apartados entre corchetes `[]` son, información que no conozco aun. Por lo que si se quiere usar este documento, se debe leer y completar la información faltante.
* Se uso ChatGPT para:
  * Mejorar la redacción de la propuesta, aunque se puede adaptar a su propio estilo de redacción.
  * Investigar tecnologías y herramientas de gestión de asistencias en el contexto educativo mexicano, por lo que si se tiene mayor conocimiento sobre el tema, se pueden agregar o modificar las tecnologías y herramientas mencionadas.
* Se agregaron las IAs que usé en la propuesta del proyecto, si les puede afectar en su calificación, pueden eliminar las referencias si lo desean.

## Stack tecnológico propuesto
### Backend - FastAPI (Python)

Se utilizó FastAPI ya que se sabe que la autora del repositorio original utiliza mucho Python, y FastAPI es un framework moderno y eficiente para construir APIs RESTful.

Se valoraron otras opciones aun más fáciles como:
* **Next.js (JavaScript):** Pero se descartó por:
  * La falta de experiencia en JavaScript y la preferencia por Python.
  * Aunque este framework reduce la cantidad de código para las rutas y controladores (literlamente un archivo en una carpeta es una ruta), depende mucho de RSC (React Server Components)
  * Los RSC, para no entrar en mucho detalle, como su nombre lo indica, son componentes de React que se ejecutan en el servidor, y en los últimos meses han tenido muchos problemas de seguridad, por lo que se habría tenido que implementar soluciones como los CDNs de Cloudflare y otras cosas, que aunque son gratuitos, hay que investigar mas sobre como funcionan y como implementarlos, lo que habría complicado más el desarrollo del proyecto.
* **Laravel o PHP "crudo:"** Un framework y lenguaje de programación rey en el desarrollo web, pero se descartó por:
  * La falta de experiencia en PHP y la preferencia por Python.
  * Aunque Laravel es un framework muy popular y tiene una gran comunidad, se consideró que FastAPI sería más adecuado para el proyecto debido a su simplicidad y eficiencia.

Además, FastAPI tiene una excelente documentación y una comunidad activa, lo que facilita el desarrollo y la resolución de problemas.

### Base de Datos - PostgreSQL
Aunque habría sido más fácil usar MySQL, que es el mas popular, se optó PostgreSQL por su compatibilidad con Python y que no depende de Oracle.

Oracle es dueña de MySQL, y no le ha agregado muchas funcionalidades en los últimos años. Se podría haber usado MariaDB, pero al final PostgreSQL era la opción más segura y además, ya lo tenía instalado :p

### Frontend - React.js y Bootstrap
Se eligió React.js por su popularidad y facilidad de uso para construir interfaces de usuario interactivas.

También, es el framework en el ya tengo experiencia, por lo que era más rápido de desarrollar para mí.

Aunque se tendrá que aprender React para los miembros del equipo que no lo conocen, es más fácil que implementar el Frontend vanilla (HTML, CSS y JavaScript puro), ya que React ofrece una estructura y herramientas que facilitan el desarrollo de aplicaciones web modernas.

Además, React tiene una gran comunidad y una amplia gama de bibliotecas y herramientas que facilitan el desarrollo frontend.

También se eligió Bootstrap para el diseño y la maquetación, ya que es un framework CSS que proporciona estilos predefinidos y componentes reutilizables, lo que acelera el proceso de diseño y garantiza una apariencia consistente en toda la aplicación.
Se podría utilizar Tailwind CSS, ya que muchas plataformas de IA orientadas al diseño lo usan, pero se hizo está decisión asumiendo que los miembros del equipo no querían aprender CSS a profundiad.

### Otras herramientas y tecnologías

* **VS Code**: Como editor de código, gratuito
* **GitHub Copilot (Pro)**: Tengo la versión Pro, por el carnet de estudiante :p
* **Cartero**: Cliente HTTP como sustituto a **Postman**, ya que es gratuito y de código abierto. Aunque se puede usar Postman si se prefiere, también es gratis pero requiere crear una cuenta