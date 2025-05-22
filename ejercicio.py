##contador regresivo##
import time ##para importar time.sleep

i= int(input("escribe un valor para iniciar la cuenta regresiva: "))

while i >= 0:
    print (i)
    time.sleep(1) #espera 1 seg antes de continuar
    i-=1

print ("Cuenta regresiva completada: ¡¡¡BooM!!!")

