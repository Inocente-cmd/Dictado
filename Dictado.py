import random
import os
from gtts import gTTS
import pygame
import time
import sys
import shutil


# Este codigo a sido escrito porque el creador habia fracasado un dictado de chino de 8 palabras.
# No sabia como pronunicar las palabras y poreso no escribio la palabra correcta.
# El ejercicio era de 8 palabras y solo pudo escribir 5.

#ruta_actual = os.getcwd()
#print("La ruta actual es:", ruta_actual)
# Nombre del archivo de texto

# Función para descargar el audio de la palabra en un idioma específico y renombrar el archivo
def descargar_audio(palabras, lang):
    if not os.path.exists("Audios"):
        os.makedirs("Audios")
    for palabra in palabras:
        tts = gTTS(text=palabra, lang=lang)
        tts.save(f"Audios/{palabra}_{lang}.mp3")

# Función para reproducir el audio de una palabra
def reproducir_audio(palabra, lang):
    archivo_audio = f"Audios/{palabra}_{lang}.mp3"
    if os.path.exists(archivo_audio):
        pygame.mixer.init()
        pygame.mixer.music.load(archivo_audio)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            time.sleep(1)

# Función para leer la entrada del usuario y manejar las opciones
def manejar_opciones(palabras, orden_aleatorio, idx_actual, lang):
    print("\nOpciones:")
    print("S = Siguiente")
    print("A = Anterior")
    print("R = Replay")
    print("E = Exit")
    print("M = Mostrar")

    while True:
        opcion = input("Elige una opción: ").strip().lower()
        if opcion == 'e':
            print("\n¡Hasta la próxima!")
            pygame.mixer.quit()
            try:
                carpeta = "Audios"
                shutil.rmtree(carpeta)
                print("Se borró la carpeta 'Audios'.")
            except Exception as e:
                print(f"No se pudo borrar la carpeta 'Audios': {e}")
            return True, 0
        elif opcion == 'r':
            reproducir_audio(orden_aleatorio[idx_actual], lang)
        elif opcion == 's':
            idx_actual = (idx_actual + 1) % len(orden_aleatorio)
            reproducir_audio(orden_aleatorio[idx_actual], lang)
        elif opcion == 'm':
            print(orden_aleatorio[idx_actual])
            reproducir_audio(orden_aleatorio[idx_actual], lang)
        elif opcion == 'a':
            idx_actual = (idx_actual - 1) % len(orden_aleatorio)
            reproducir_audio(orden_aleatorio[idx_actual], lang)
        else:
            print("Opción inválida. Inténtalo de nuevo.")

    return False, idx_actual

# Función principal del programa
def main():
    archivo_txt = "Palabras.txt"
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    archivo_ruta = os.path.join(desktop_path, archivo_txt)

    if not os.path.exists(archivo_ruta):
        print(f"No se encontró el archivo '{archivo_txt}' en el escritorio.")
        return

    # Leer las palabras del archivo
    with open(archivo_ruta, 'r', encoding='utf-8') as file:
        palabras = file.read().split()

    # Mostrar cuántas palabras hay disponibles

    print("""

















""")
    #print(f"Hay {len(palabras)} palabras disponibles para practicar.")

    # Preguntar cuántas palabras desea escuchar
    while True:
        try:
            cantidad_palabras = int(input(f"""Tienes {len(palabras)} palabras.
¿Hasta que palabra Usted quiere practicar? Del 1 hasta : """))
            if 1 <= cantidad_palabras <= len(palabras):
                break
            else:
                print("Número fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

    # Descargar audios en ambos idiomas
    descargar_audio(palabras, 'zh')  # Chino
    descargar_audio(palabras, 'en')  # Inglés

    # Obtener un orden aleatorio de las palabras
    orden_aleatorio = random.sample(palabras, cantidad_palabras)

    # Elegir un índice aleatorio para comenzar la reproducción
    idx_actual = random.randint(0, len(orden_aleatorio) - 1)

    # Reproducir las palabras en el orden aleatorio
    while True:
        lang = input("¿En qué idioma esta el texto? (Zh/En): ").strip().lower()
        if lang not in ['zh', 'en']:
            print("Idioma no válido.")
            continue

        reproducir_audio(orden_aleatorio[idx_actual], lang)

        # Manejar opciones del usuario
        reiniciar_programa, idx_actual = manejar_opciones(palabras, orden_aleatorio, idx_actual, lang)
        if reiniciar_programa:
            break

if __name__ == "__main__":
    main()
