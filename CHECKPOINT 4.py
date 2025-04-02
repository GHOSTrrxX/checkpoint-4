lista = ["manzana","pera","banana"]
tupla = ("rojo","verde","azul")
float = 7.3
entero = 10
from decimal import Decimal
decimal = Decimal("3.14")
diccionario = {"nombre": "daniel", "edad": 22, "ciudad": "Bilbao"}

import math
import math

float_redondeado = math.ceil(float)
raiz_cuadrada = math.sqrt(float)


primer_elemento_diccionario = list(diccionario.values())[0]
segundo_elemento_tupla = tupla[1]

lista.append("naranja")
lista[0] ="Limon"

lista.sort()
tupla = tupla + ("Marron",)

print("Lista ordenada:", lista)
print("Tupla Actualizada:", tupla)
print("Float redondeado:", float_redondeado)
print("Raíz cuadrada del float:", raiz_cuadrada)
print("Primer elemento diccionario:", primer_elemento_diccionario)
print("Segundo elemento tupla:", segundo_elemento_tupla)