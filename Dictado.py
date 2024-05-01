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
archivo_txt = "Palabras.txt"
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
archivo_ruta = os.path.join(desktop_path, archivo_txt)

borar = "no"

print("")
print("Tiene que crear un archivo llamado 'Palabras.txt' que adentro debe contener las palabras que va a practicar")

crash = "no"

for i in range(1):
    if os.path.exists(archivo_ruta):
        print(f"El archivo  existe.")
    else:
        print(f"El archivo no existe.")
        crash = "si"
        time.sleep(4)
        break

def detener_musica(idx_actual):
    pygame.mixer.music.stop()
    print("La música se detuvo.")

if crash == "si":
    print("Crashed... No existe el archivo 'Palabras.txt'")
    time.sleep(2)
else:
    for i in range(1):

        # Función para leer el archivo de texto y enumerar las palabras
        def enumerar_palabras(archivo):
            with open(archivo_ruta, 'r', encoding='utf-8') as file: # Py/traduccion/Lista.txt', 'r'
                #print(archivo_ruta)
                palabras = file.read().split()
                for i, palabra in enumerate(palabras, 1):
                    print(f"{i}. {palabra}")
            return palabras

        # Función para descargar el audio de la palabra en chino y renombrar el archivo con el nombre de la palabra
        def descargar_audio(palabras):
            if not os.path.exists("Audios"):
                os.makedirs("Audios")
            for palabra in palabras:
                tts = gTTS(text=palabra, lang='zh')
                tts.save(f"Audios/{palabra}.mp3")

        # Función para reproducir el audio de una palabra
        def reproducir_audio(palabra):
            archivo_audio = f"Audios/{palabra}.mp3"
            if os.path.exists(archivo_audio):
                pygame.mixer.init()
                pygame.mixer.music.load(archivo_audio)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                    time.sleep(1)
                    pygame.mixer.music.stop()

        def desdesoedir(palabra):
            time_test=0.08
            for i in palabra :
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(time_test)
            print()

        def pista(actual):
            print(actual)
        
        # Función para leer la entrada del usuario y manejar las opciones
        def manejar_opciones(palabras, orden_aleatorio, idx_actual):
            print("\nOpciones:")
            print("S = Siguiente")            # R = Replay
            print("A = Anterior ")            # E = Exit
            print("R = Replay")               # S = Siguiente
            print("E = Exit")                 # A = Anterior 
            print("M = Mostrar")              # M = Mostrar


            while True:
            
                opcion = input("Elige una opción: ")
                if opcion == 'e':
                    print("")
                    desdesoedir("Hasta la proxima!!!")
                    print("")
                    pygame.mixer.quit()
                    try:
                        carpeta = "Audios"
                        shutil.rmtree(carpeta)
                        #print("Misión Cumplida...")
                        return True, 0
                    except:
                        print("Misión Fallida... No se pudo borrar la carpeta")
                        return True, 0
                    
                elif opcion == 'r':
                    reproducir_audio(orden_aleatorio[idx_actual])
                elif opcion == 's':
                    idx_actual = (idx_actual + 1) % len(orden_aleatorio)
                    reproducir_audio(orden_aleatorio[idx_actual])
                elif opcion == 'm':
                    pista(orden_aleatorio[idx_actual])
                    reproducir_audio(orden_aleatorio[idx_actual])
                elif opcion == 'a':
                    idx_actual = (idx_actual - 1) % len(orden_aleatorio)
                    reproducir_audio(orden_aleatorio[idx_actual])
                else:
                    print("Opción inválida. Inténtalo de nuevo.")
            
            return False, idx_actual  # Añadir esta línea para retornar el índice actual

        sisss = os.getcwd()
        #print("La ruta actual es:", sisss)

        # Enumerar las palabras del archivo
        palabras = enumerar_palabras(archivo_txt)
        # Pedir al usuario cuántas palabras desea reproducir


        while True:
            try:
                cantidad_palabras = int(input("¿Cuántas palabras deseas escuchar?: "))
                if 1 <= cantidad_palabras <= len(palabras):
                    break
                else:
                    print("Número fuera de rango. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Introduce un número entero.")


        # Descargar los audios de las palabras en chino y renombrar los archivos con el nombre de la palabra
        descargar_audio(palabras)

        # Obtener un orden aleatorio de las palabras
        orden_aleatorio = random.sample(palabras, cantidad_palabras)

        # Elegir un índice aleatorio para iniciar la reproducción
        idx_actual = random.randint(0, len(orden_aleatorio) - 1)

        # Reproducir las palabras en el orden aleatorio
        while True:
            reproducir_audio(orden_aleatorio[idx_actual])
            reiniciar_programa, idx_actual = manejar_opciones(palabras, orden_aleatorio, idx_actual)
            if reiniciar_programa:         
                break
            
