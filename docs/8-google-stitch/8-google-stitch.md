# Google Stitch

>Esta sección es opcional, ya que es sobre las herramientas de IA que usé para generar el frontend del proyecto

## Prompt

Usé [Google Stitch](https://stitch.withgoogle.com/) para generar las interfaces del frontend de la aplicación.

Eso si, ya que no le especifiqué en el primer prompt que el idioma de la aplicación era español, me generó las interfaces en inglés.

Intenté pedirle que me las tradujera al español, pero las tradujo un poco mal. Por lo que hay algunas partes que quedaron en inglés.

Igual dejo el prompt que le di para generar las interfaces pero corregido, por si alguien quiere probarlo y ver si les da mejores resultados. Esta en la carpeta `prompt/`.

## Google Antigravity

También, anexo la carpeta `.antigravity/` que es la que contiene el proyecto generado por Google Stitch, por si alguien quiere usarlo como base para su proyecto.

Además, contiene algunas configuraciones que usé para el agente de Antigravity, por si alguien quiere probarlo y ver si les da mejores resultados.

>[!NOTE]
>Aquí estará duplicada la plantilla XLSM de asistencias del proyecto, pero es porque aquí es donde debe leer (o leyó mas bien) el agente de Antigravity para generar la plantilla XLSM para la parte de asistencias y el módulo de asistencias (uploads) e incluirla en el backend del proyecto.

>[!IMPORTANT]
>Si se desea usar la carpeta `.antigravity/` para el proyecto, en todo proyecto de IA debe, las carpetas `.antigravity/`, `.agents/`, entre otras, debe estas en la raíz del proyecto. Tal que así:

```plaintext
.antigravity/
backend/
frontend/
```