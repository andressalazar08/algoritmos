'''Problema:

Ejercicio 4: Contar Números Pares en una Lista'''

mi_lista=[2,5,6,0,8,15,6,8,9,7]
cantidad_de_numeros_pares=0
for numero in mi_lista:
    if numero%2==0:
        cantidad_de_numeros_pares+=1
print(cantidad_de_numeros_pares)
        