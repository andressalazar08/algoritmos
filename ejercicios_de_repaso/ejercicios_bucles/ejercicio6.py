'''Ejercicio 6: Clasificar Números en Positivos y Negativos'''
mi_lista=[-8,3,-6,2,4,5,-4]
cantidad_de_negativos=0
cantidad_de_positivos=0

for numero in mi_lista:
    if numero<0:
        cantidad_de_negativos+=1
    else:
        cantidad_de_positivos+=1
print(cantidad_de_positivos)
print(cantidad_de_negativos)