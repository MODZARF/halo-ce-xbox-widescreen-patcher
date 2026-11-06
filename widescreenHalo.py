print("""

            ________      ________      ________      ________ 
---------- |\_____  \    |\   __  \    |\   __  \    |\  _____\----------------
----------  \|___/  /|   \ \  \|\  \   \ \  \|\  \   \ \  \__/ ---------------
--------------  /  / /    \ \   __  \   \ \   _  _\   \ \   __\--------------
-------------- /  /_/__    \ \  \ \  \   \ \  \\  \|    \ \  \_|----------------
------------- |\________\   \ \__\ \__\   \ \__\\ _\     \ \__\ ----------------
-------------- \|_______|    \|__|\|__|    \|__|\|__|    \|__| -----------------

""")

print("Parche Wide Screen para Halo Combat Evolved Xbox Clásico")
def reemplazar_bytes():
    archivo = "default.xbe"

    try:
        with open(archivo, "rb") as f:
            datos = f.read()
        # Comprobación
        if datos[:11] == b'XBEH@\x7E\x00\xC7\x2A\xFE\xBE':
            # Reemplazar los bytes para NTSC
            datos = datos.replace(b'\xD8\x25\x00\xE7\x1E\x00', b'\xD8\x25\xA0\xA0\x1F\x00')
            datos = datos.replace(b'\x00\x00\x00\x3F\x90\x04\x11\x00\xF0\x04\x11\x00\xB0\xEC\x10\x00', b'\xAA\xAA\x2A\x3F\x90\x04\x11\x00\xF0\x04\x11\x00\xB0\xEC\x10\x00')
            datos = datos.replace(b'\xD8\x0D\xA0\x0A\x1F\x00\xD9\x46\x0C\xD8\x66\x08\xD8\x0D\xA0\x0A', b'\xD8\x0D\x00\xE7\x1E\x00\xD9\x46\x0C\xD8\x66\x08\xD8\x0D\xA0\x0A')
            datos = datos.replace(b'\x00\xD8\x0D\x20\x0C\x1F\x00\x0F\xBF\x05\xC0\xEB\x2F\x00\x0F\xBF', b'\x00\xD8\x0D\x54\x0D\x1F\x00\x0F\xBF\x05\xC0\xEB\x2F\x00\x0F\xBF')
            # Guardar
            archivo_modificado = f"{archivo[:-4]}_widescreen.xbe"
            with open(archivo_modificado, "wb") as f_modificado:
                f_modificado.write(datos)
            print("Aplicado con éxito en la versión NTSC")
            print("Agradecimientos a Nemesis2000")
            input("Presiona enter para cerrar la ventana")
        elif datos[:11] == b'XBEH\x91\x9C\x8D\x35\x65\x9A\xE1':
            # Reemplazar los bytes para PAL
            datos = datos.replace(b'\xD8\x3D\x98\x2B\x1F\x00\xD9\x5C\x24\x18\xD9\xC9\xD8\xC9\xD8\x3D\x98\x2B\x1F\x00\xD9\x5C\x24\x1C\xDD\xD8\xD9\x47\x20\xD8\x4F\x10\xD9\x47\x1C\xD8\x4F\x14\xDE\xE9\xD9\x5C\x24\x38\xD9\x47\x14\xD8', b'\xD8\x3D\x80\x0A\x1F\x00\xD9\x5C\x24\x18\xD9\xC9\xD8\xC9\xD8\x3D\x98\x2B\x1F\x00\xD9\x5C\x24\x1C\xDD\xD8\xD9\x47\x20\xD8\x4F\x10\xD9\x47\x1C\xD8\x4F\x14\xDE\xE9\xD9\x5C\x24\x38\xD9\x47\x14\xD8')
            # Guardar
            archivo_modificado = f"{archivo[:-4]}_widescreen.xbe"
            with open(archivo_modificado, "wb") as f_modificado:
                f_modificado.write(datos)
            print("Aplicado con éxito en la versión PAL")
            print("Agradecimientos a MrNova")
            input("Presiona enter para cerrar la ventana")
        else:
            print("¡ERROR! el default.xbe no pertenece a Halo Combat Evolved")
            input("Presiona enter para cerrar la ventana")
    except FileNotFoundError:
        print("ERROR... default.xbe no encontrado")
        input("Presiona enter para cerrar la ventana")

reemplazar_bytes()