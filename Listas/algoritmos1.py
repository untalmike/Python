#sumatoria de una lista
lista = [2, 4, 6, 1, 2]
sumatoria = 0

for num in lista:
    sumatoria += num

# print("La sumatoria de la lista es:", sumatoria)

# promedio de una lista
promedio = 0
for num in lista:
    promedio += num

promedio /= len(lista)
print("El promedio de la lista es:", promedio)

max = 0
for num in lista:
    if num > max:
        max = num