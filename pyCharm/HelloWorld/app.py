age = 20
age = 30
price = 19.95
first_name = "Mike"
last_name = "Smith"
is_online = True

# print("Hello World!")
# print(age)
# print(first_name + " " + last_name)

# Ejercicio:
# name = input("cuál es tu nombre? ")
# birth_year = input("cuál es tu año de nacimiento? ")
# age = 2025 - int(birth_year)

# print("Hola " + name + ", tienes " + str(age) + " años.")

# Ejercicio: calculadora básica
# first = input("Primer número: ")
# second = input("Segundo número: ")
# suma = float(first) + float(second)
# print("sum: " + str(suma))

# course = "Python para principiantes"
# print(course.upper())  # Pone en mayúsculas
# print(course.lower())  # Pone en minúsculas
# print(course.find("y"))  # busca un carácter y devuelve su índice, es sen sible a mayúsculas y minúsculas
# print(course.replace("Python", "Java"))  # Reemplaza una subcadena por otra
# print(course)  # impresión normal

# Operadores aritméticos
# print(10 + 3)  # Suma
# print(10 - 3)  # Resta 
# print(10 * 3)  # Multiplicación
# print(10 / 3)  # División
# print(10 // 3)  # División entera
# print(10 % 3)  # Módulo (resto de la división) 
# print(10 ** 3)  # Exponente (potencia)

# precedencia de operadores
# print(10 + 3 * 2)  # Multiplicación antes de la suma
# print((10 + 3) * 2)  # Paréntesis para cambiar

# operadores de comparación
# print(10 > 3)  # Mayor que
# print(10 >= 3)  # Mayor o igual que
# print(10 < 3)  # Menor que
# print(10 <= 3)  # Menor o igual que
# print(10 == 3)  # Igual a
# print(10 != 3)  # Diferente de

# operadores lógicos
# print(10 > 3 and 10 < 20)  # AND lógico
# print(10 > 3 or 10 < 5)  # OR lógico
# print(not 10 > 3)  # NOT lógico

# Sentencias de control
# is_hot = True
# is_cold = False
# if is_hot:
#     print("It's a hot day")
# elif is_cold:
#     print("It's a cold day")
# else:
#     print("It's a lovely day")
# print("Enjoy your day!")

# Ejercicio peso:
# weight = input("Weight: ")
# unit = input("¿Libras o kilos? (l/k): ")
# if unit.upper() == "K":
#     converted = float(weight) / 0.45
#     print("Weight in Lbs: " + str(converted))
# elif unit.upper() == "L":
#     converted = float(weight) * 0.45
#     print("Weight in Kgs: " + str(converted))
# else:
#     print("Not allowed option. Please enter 'l' for pounds or 'k' for kilos.")

# while loops
# i = 1
# while i <= 10:
#     print(i * '*')
#     i += 1  # Incrementa i en 1

# Lista de números
# names = ["John", "Mary", "Bob", "Alice", "Sam"]
# names[0] = "Jon"
# print("Names:", names)
# print("First name:", names[0])  # Acceso al primer elemento
# print("Last name:", names[-1])  # Acceso al último elemento
# print(names[0:3])  # Acceso a un rango de elementos

# List methods
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)  # Añade un elemento al final
# numbers.insert(0, 0)  # Inserta un elemento en la posición 0
# numbers.remove(3)  # Elimina el primer elemento con valor 3
# numbers.pop()  # Elimina el último elemento
# numbers.clear()  # Limpia la lista
# numbers.sort()  # Ordena la lista
# numbers.reverse()  # Invierte el orden de la lista
# numbers_copy = numbers.copy()  # Crea una copia de la lista
# print("Numbers:", numbers)
# print("Numbers copy:", numbers_copy)
# print(len(numbers))  # Longitud de la lista

# bucles for
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print("Number:", item)

# i = 0
# while i < len(numbers):
#     print("Number:", numbers[i])
#     i += 1  # Incrementa i en 1

# función range

# numbers_range = range(5, 10, 2)  # Crea un rango de números del 5 al 9 (el 10 no se incluye) luego realiza un salto de 2
# for number in range(5):
#     print("Number from range:", number)

# tuple
coordinates = (10, 20, 30)  # Tupla de coordenadas, lleva corchetes y no se puede modificar
# coordinates[0] = 20  # Esto generará un error porque las tuplas son inmutables
print("Coordinates:", coordinates)