import random #importar paquete random

numeros=list(range(1,101))
random.shuffle(numeros)

valor = int(input("Escribe un número del 1 al 101: "))

for i, n in enumerate (numeros): ##parte siempre de un valor i n entregados por defecto por el programa de ciclo for y enumerate
    print(i,n)
    if n == valor:
        print(f"el valor se ha encontrado en {i}. {valor}")
        break
print("Busqueda finalizada")