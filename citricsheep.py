# Start with the string "CitricSheep".
# Use the ASCII values of each character in the string and generate a list of these values.
# Multiply each value in the list by the number of characters in the string.
# Find the sum of all numbers in the resulting list.
# Use this sum to generate a SHA256 hash.
# Convert this hash to a hexadecimal string.
#--------------------------------------
# Comece com a string "CitricSheep".
# Use os valores ASCII de cada caractere da string e gere uma lista desses valores.
# Multiplique cada valor da lista pelo número de caracteres da string.
# Encontre a soma de todos os números na lista resultante.
# Use esta soma para gerar um hash SHA256.
# Converta esse hash em uma string hexadecimal.

import hashlib

# Passo 1: Inicializar a string
input_string = "CitricSheep"

# Passo 2: Gerar uma lista dos valores ASCII dos caracteres
ascii_values = [ord(char) for char in input_string]

# Passo 3: Multiplicar cada valor pela quantidade de caracteres na string
multiplied_values = [value * len(input_string) for value in ascii_values]

# Passo 4: Calcular a soma dos números na lista resultante
sum_result = sum(multiplied_values)

# Passo 5: Gerar um hash SHA256 da soma
hashed_value = hashlib.sha256(str(sum_result).encode()).hexdigest()

# Exibir a string hexadecimal resultante
print("String hexadecimal resultante:", hashed_value)