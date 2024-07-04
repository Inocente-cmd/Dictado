import random
import os
from gtts import gTTS
import pygame
import time
import sys
import shutil
import pyttsx3


# Este codigo a sido escrito porque el creador habia fracasado un dictado de chino de 8 palabras.
# No sabia como pronunicar las palabras y por eso no escribio la palabra correcta.
# El ejercicio era de 8 palabras y solo pudo escribir 5.


archivo_txt = "Palabras.txt"
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
archivo_ruta = os.path.join(desktop_path, archivo_txt)

print("")

crash = "no"

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

for i in range(1):
    if os.path.exists(archivo_ruta):
        pass
        #print(f"El archivo existe.")
    else:
        print(f"El archivo no existe.")
        print("Tiene que crear un archivo llamado 'Palabras.txt' que adentro debe contener las palabras que va a practicar")
        crash = "si"
        time.sleep(4)
        break

if crash == "si":
    print("Crashed... No existe el archivo 'Palabras.txt'")
    time.sleep(2)
else:
    for i in range(1):

        def enumerar_palabras(archivo):
            with open(archivo_ruta, 'r', encoding='utf-8') as file:
                palabras = file.read().split()
                for i, palabra in enumerate(palabras, 1):
                    print(f"{i}. {palabra}")
            return palabras

        def descargar_audio(palabras):
            if not os.path.exists("Audios"):
                os.makedirs("Audios")
            for palabra in palabras:
                tts = gTTS(text=palabra, lang='zh')
                tts.save(f"Audios/{palabra}.mp3")

        def reproducir_audio(palabra):
            if lan == "zh":
                archivo_audio = f"Audios/{palabra}.mp3"
                if os.path.exists(archivo_audio):
                    pygame.mixer.init()
                    pygame.mixer.music.load(archivo_audio)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                        time.sleep(1)
                    pygame.mixer.music.stop()
            else:
                texto_a_voz(palabra)

        def desdesoedir(palabra):
            time_test = 0.08
            for i in palabra:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(time_test)
            print()

        def pista(actual):
            print(actual)

        def manejar_opciones(palabras, orden_aleatorio, idx_actual):
            print("\nOpciones:")
            print("1 = Siguiente")
            print("2 = Anterior")
            print("3 = Replay")
            print("4 = Mostrar")
            print("5 = Exit")

            while True:
                opcion = input("Elige una opción: ")
                if opcion == '5':
                    print("")
                    desdesoedir("¡Hasta la próxima!")
                    print("")
                    desdesoedir("By inocente")
                    time.sleep(3)
                    pygame.mixer.quit()
                    try:
                        carpeta = "Audios"
                        shutil.rmtree(carpeta)
                        return True, 0
                    except:
                        return True, 0

                elif opcion == '3':
                    reproducir_audio(orden_aleatorio[idx_actual])
                elif opcion == '1':
                    idx_actual = (idx_actual + 1) % len(orden_aleatorio)
                    reproducir_audio(orden_aleatorio[idx_actual])
                elif opcion == '4':
                    pista(orden_aleatorio[idx_actual])
                    reproducir_audio(orden_aleatorio[idx_actual])
                elif opcion == '2':
                    idx_actual = (idx_actual - 1) % len(orden_aleatorio)
                    reproducir_audio(orden_aleatorio[idx_actual])
                else:
                    print("Opción inválida. Inténtalo de nuevo.")

            return False, idx_actual
        print("\n" * 300000)

        lan = str(input("¿Cuál es el idioma de las palabras Zh/En?: ")).strip().lower()
        palabras = enumerar_palabras(archivo_txt)

        total_palabras = len(palabras)

        while True:
            try:
                cantidad_palabras = int(input(f"¿Cuántas palabras (1-{total_palabras}) deseas practicar?: "))
                if 1 <= cantidad_palabras <= total_palabras:
                    break
                else:
                    print(f"Valor inválido. Introduce un número entre 1 y {total_palabras}.")
            except ValueError:
                print("Entrada inválida. Introduce un número entero.")

        palabras_a_practicar = palabras[:cantidad_palabras]

        if lan == "zh":
            descargar_audio(palabras_a_practicar)

        orden_aleatorio = random.sample(palabras_a_practicar, cantidad_palabras)
        idx_actual = random.randint(0, len(orden_aleatorio) - 1)

        while True:
            reproducir_audio(orden_aleatorio[idx_actual])
            reiniciar_programa, idx_actual = manejar_opciones(palabras_a_practicar, orden_aleatorio, idx_actual)
            if reiniciar_programa:
                break
