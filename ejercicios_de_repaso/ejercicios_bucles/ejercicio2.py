'''Problema:
Solicitar al usuario una palabra y contar cuántas letras tiene.
Ejercicio 2: Contar Vocales en un String'''

palabra=input("Ingrese la palabra ")
vocales="aeiouAEIOU"
contador_de_vocales=0
contador_de_letras=0
for letra in palabra:
    contador_de_letras+=1
    if letra in vocales:
        contador_de_vocales+=1
    
print(contador_de_vocales)
print(contador_de_letras)
    