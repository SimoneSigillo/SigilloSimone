import numpy
from random import randint
numeri=""
for x in range(8):
    numeri= numeri + "," + str(randint(1,8))
    lista=numeri.split(",")
    lista.pop
    x=numpy.array(lista)
    print(lista)
    numero_scelto=input("scegli un numero: \n")
    volte=lista.count(numero_scelto)
print(volte)