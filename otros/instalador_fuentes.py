import os
import shutil
import platform

def install_font(font_path):
    """
    Instala una fuente en el sistema operativo actual (Windows o macOS).

    Parámetros:
    font_path (str): Ruta completa al archivo de la fuente que se va a instalar.

    Nota:
    - Para que la instalación tenga éxito en Windows, el script debe ejecutarse con permisos elevados (administrador).
    - En macOS, es posible que debas instalar la biblioteca `fontTools` previamente usando `pip install fonttools`.
    """
    font_name = os.path.splitext(os.path.basename(font_path))[0]

    if platform.system() == "Windows":
        import win32api
        import win32con
        import win32gui

        dst_path = os.path.join(os.environ['SystemRoot'], 'Fonts', font_name)

        if not os.path.exists(dst_path):  # Verificar si la fuente ya existe
            shutil.copy(font_path, dst_path)

            # Agregar la fuente al registro de Windows
            key = win32api.RegOpenKey(
                win32con.HKEY_LOCAL_MACHINE, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts', 0, win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(
                key, font_name, 0, win32con.REG_SZ, dst_path)
            win32api.RegCloseKey(key)

            # Actualizar las fuentes del sistema en tiempo real
            win32gui.SendMessage(win32con.HWND_BROADCAST,
                                 win32con.WM_FONTCHANGE, 0, 0)
        else:
            print(f"La fuente '{font_name}' ya está instalada en Windows.")

    elif platform.system() == "Darwin":
        from fontTools.ttLib import TTFont

        dst_path = os.path.expanduser("~/Library/Fonts/" + font_name)

        if not os.path.exists(dst_path):  # Verificar si la fuente ya existe
            shutil.copy(font_path, dst_path)

            # Recargar la fuente en macOS
            font = TTFont(dst_path)
            font.save(dst_path)
        else:
            print(f"La fuente '{font_name}' ya está instalada en macOS.")

    else:
        raise NotImplementedError(
            "Lo siento, no se puede instalar una fuente en este sistema operativo.")

"""
nota: para windows
si no quieres reiniciar el equipo puedes intentar forzar una actualización de las 
fuentes sin reiniciar ejecutando los siguientes comandos en la línea de comandos 
con privilegios de administrador:

taskkill /F /IM explorer.exe
start explorer.exe
"""