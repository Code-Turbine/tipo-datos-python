variable_string_comillas_simples = 'Contenido del string en comillas simples'

variable_string_comillas_dobles = "Contenido del string en comillas dobles"

print(variable_string_comillas_simples)
print(variable_string_comillas_dobles)

print(variable_string_comillas_simples[0])

print(variable_string_comillas_simples[1])

variable_integer_negativa = -800
variable_integer_positiva = 300

print(variable_integer_negativa)
print(variable_integer_positiva)

print(type(variable_string_comillas_simples))
print(type(variable_string_comillas_dobles))
print(type(variable_integer_negativa))
print(type(variable_integer_positiva))

variable_string_de_un_entero_negativo = str(variable_integer_negativa)
variable_string_de_un_entero_positivo = str(variable_integer_positiva)

print(variable_string_de_un_entero_negativo)
print(variable_string_de_un_entero_positivo)

print(type(variable_string_de_un_entero_negativo))
print(type(variable_string_de_un_entero_positivo))

#***************************Otros tipos de datos***************************

print('***************************Otros tipos de datos***************************')

#float (Número de coma flotante): Almacena números con decimales, como 3.14 o -2.7.
numero_flotante = 3.14 
#complex (Número complejo): Almacena números complejos con parte real e imaginaria, como 2 + 3j. 
numero_complejo = 2 + 3j 

print(type(numero_flotante)) # Output: <class 'float'>
print(type(numero_complejo)) # Output: <class 'complex'>

#list (Lista): Almacena una colección ordenada de elementos, que pueden ser de diferentes tipos. 
lista = [1, 2, "Hola", True]
#tuple (Tupla): Almacena una colección ordenada de elementos, similar a una lista, pero no se puede modificar una vez creada. 
tupla = (1, 2, "Hola")
#range (Rango): Genera una secuencia de números enteros en un rango específico. 
rango = range(5)

print(type(lista))  # Output: <class 'list'>
print(type(tupla))  # Output: <class 'tuple'>
print(type(rango))  # Output: <class 'range'>

#dict (Diccionario): Almacena datos en formato clave-valor.
diccionario = {"nombre": "Juan", "edad": 30}
#bool (Booleano): Almacena valores de verdad (True o False).
booleano = True
#set (Conjunto): Almacena una colección de elementos únicos.
conjunto = {1, 2, 3}
#bytes (Bytes): Almacena datos binarios como una secuencia de bytes.
bytes_dato = b"Hola mundo"

print(type(diccionario)) # Output: <class 'dict'>
print(type(booleano))   # Output: <class 'bool'>
print(type(conjunto))   # Output: <class 'set'>
print(type(bytes_dato)) # Output: <class 'bytes'>