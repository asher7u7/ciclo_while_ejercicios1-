# while

x = 0
while x < 10:
    print("el valor de x es: ",x)
    x +=1


# 2

num=int(input("ingrese un número positivo:"))

while num < 0:
    print("este es un número negativo, prueba de nuevo")
    num=int(input("ingrese un número positivo:"))
print("el número es:",num)

#3 
num=int(input("Menú: 1.Ver números    0.Salir: "))
while num!=0 :

    x=0
    while x<10:
        print("el valor de x es: ",x)
        x +=1


    print("saliendo,,,")
    num=int(input("Menú: 1.Ver números    0.Salir: "))
print("Gracias")

#4 
from cmath import sqrt
import math

numero=int(input("digite un número: "))

while numero<0:
    print("ha ocurrido un error, el número debe ser positivo")
    numero=int(input("digite un número: "))
print("\nSu raiz cuadrada es: ",numero**0.5)

#5
i=0

while i<10:
    print("hola mundo")
    i+=1