# Haciendo un pequeño proyecto para hacer que python puede leer texto
# pip install pytsx3

import pyttsx3

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def menu_opciones():
    while True:
        print("\n=== MENU DE OPCIONES ===")
        print("1. Convertir texto a voz")
        print("2. Como si fuera un chat boot xd")
        print("3. Salir")
        
        opcion = input("Elige una opcion ")
        
        if opcion == "1":
            texto = input("Escribe un texto ")
            texto_a_voz(texto)
        elif opcion =="2":
            texto_a_voz("Hola como estas en que te puedo ayudar")
            texto2 = input("Responde al chatboot ") #Es un ejemplo
            texto_a_voz(texto2)
        elif opcion == "3":
            break
        else:
            print("Esriba una opcion correcta ")

# LLamamos al menu de opciones
menu_opciones()    
        
    


