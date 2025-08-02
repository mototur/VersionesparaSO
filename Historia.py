import random

print("Generador de historias aleatorias")

nombres = ["Lucía", "Carlos", "Paula", "Tomás"]
lugares = ["una cueva", "el bosque encantado", "una ciudad perdida"]
acciones = ["descubrió", "encontró", "vio", "tocó"]

nombre = random.choice(nombres)
lugar = random.choice(lugares)
accion = random.choice(acciones)

historia = f"{nombre} fue a {lugar} y {accion} algo misterioso."
print("\nTu historia:")
print(historia)

