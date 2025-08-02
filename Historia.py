import random

def generar_historia():
   nombres = ["Lucía", "Carlos", "Paula", "Tomás"]
   lugares = ["una cueva", "el bosque encantado", "una ciudad perdida"]
   acciones = ["descubrió", "encontró", "vio", "tocó"]

   nombre = random.choice(nombres)
   lugar = random.choice(lugares)
   accion = random.choice(acciones)

   return f"{nombre} fue a {lugar} y {accion} algo increíble."

print("Generador de historias aleatorias")

while True:
    print("\n" + generar_historia())
    repetir = input("¿Quieres otra historia? (s/n): ")
    if repetir.lower() != 's':
        print("¡Gracias por usar el generador!")
        break