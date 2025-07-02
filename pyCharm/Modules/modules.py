import math # Así se realiza un import
import sys # Importa el módulo sys
import random as rdm# Importa el módulo random
from enum import Enum # Importa la clase Enum del módulo enum
import kansas # Importa el módulo kansas

print(math.pi) # Imprime el valor de pi
# random.choice("123") # Elige un elemento aleatorio de la cadena "123"

# for item in dir(rdm):
#     print(item)  # Imprime todos los atributos y métodos del módulo random

# print(kansas.capital)  # Imprime la capital de Kansas
# kansas.randomfunfact()  # Llama a la función randomfunfact del módulo kansas

print(__name__)  # Imprime el nombre del módulo actual
print(kansas.__name__)  # Imprime el nombre del módulo kansas