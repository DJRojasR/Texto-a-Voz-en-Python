"""
Lector de archivos de texto
El programa lee un archivo .txt completo y lo convierte en voz.
Ejemplo: “Leer libro.txt en voz alta”.
"""
import pyttsx3

def lector_texto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


def menu_opciones():
    while True:
        print("\n=== MENU DE OPCIONES ===")
        print("1. Leer archivo 1")
        print("2. Leer archivo 2")
        print("3. Salir")

        option = input("Escoja una opciones ")

        if option == "1":
            with open("texto.txt","r",encoding="utf-8") as archivo:
                contenido = archivo.read()
            lector_texto(contenido)
        elif option == "2": 
            with open("texto/texto2.txt", "r", encoding="utf-8") as archivo2:
                contenido2 = archivo2.read()
            lector_texto(contenido2)
        elif option == "3":
            break
        else:
            print("Escoja una opcion correcta ")   

menu_opciones()

