# Halo CE - Widescreen Patcher for Xbox Clásico

Herramienta en Python para aplicar el mod de **Widescreen** al `default.xbe` de **Halo: Combat Evolved** de Xbox Clásico, con un solo clic.

Sin complicaciones, sin editores hexadecimales, sin buscar offsets a mano. El programa detecta automáticamente si tu `default.xbe` es **NTSC** o **PAL** y aplica la edición correspondiente.

> Proyecto fan sin ánimo de lucro con fines de preservación y accesibilidad. No incluye ni distribuye archivos del juego. Necesitas tu propia copia original.

## ¿Qué hace?

Modifica los valores hexadecimales dentro del `default.xbe` para forzar la relación de aspecto panorámica (16:9) en Halo: Combat Evolved, eliminando la imagen estirada o con barras negras en pantallas modernas y en Xbox con salida por componentes.

- ✅ Detección automática de versión **NTSC** / **PAL**
- ✅ Aplicación automática del parche correcto
- ✅ No sobreescribe tu archivo original
- ✅ Funciona con el script `.py` o con el `.exe` compilado

## Requisitos

- Tu copia original de `default.xbe` de Halo: Combat Evolved para Xbox Clásico
- Windows (para el `.exe`) o Python 3.10+ (para el `.py`)

## Cómo usarlo

Es muy simple:

1. Descarga el `Halo_Widescreen_Patcher.exe` desde la pestaña **Releases**, o descarga el script `patcher.py` de este repositorio.
2. Coloca tu `default.xbe` **original** en la misma carpeta que el `.exe` o el `.py`.
3. Ejecuta el `.exe` o el `.py`.
4. Listo. Se creará un nuevo archivo en la misma ruta con el nombre:

   `default_widescreen.xbe`

5. Renómbralo a `default.xbe` y reemplázalo en tu carpeta del juego en tu Xbox.

Tu archivo original queda intacto, por si quieres volver a la versión 4:3.

## Créditos y Agradecimientos

Este proyecto no sería posible sin la comunidad:

- **PS2Wide** - Por los valores hex para la versión **NTSC**
- **MrNova** - Por los valores hex para la versión **PAL**

Gracias por documentar y compartir estos valores para la comunidad.

## Aviso Legal

Esta herramienta solo modifica un archivo que el usuario ya posee legalmente. No contiene código del juego, ni archivos de Halo, ni material con copyright de Bungie / Microsoft / 343 Industries.

Se distribuye como una herramienta de preservación para que un juego fuera del mercado actual siga siendo jugable de la mejor forma posible en hardware original y moderno.

## ¿Quieres ayudar?

Si encuentras algún error con alguna versión del `default.xbe`, abre un Issue con la región de tu juego y el hash del archivo. Con gusto lo revisaré.
