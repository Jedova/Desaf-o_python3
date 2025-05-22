##diccionarios y condiciones

ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000,
    "Abril": 17000, "Mayo": 81000, "Junio": 13000,
    "Julio": 21000, "Agosto": 41200, "Septiembre": 25000,
    "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000,
}

umbral = int(input("Escribe un valor de venta límite: "))

nuevas_ventas = {}

for i, n in ventas.items():
    if n>umbral:
        nuevas_ventas[i] = n
print("Se indentifica el total de valores sobre el umbral")
print(nuevas_ventas)  
