# Dado um algarismo romano, converta-o para um número inteiro. Symbol -> Value
# I -> 1
# V -> 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000
# Existem seis casos em que a subtração é usada:
# I pode ser colocado antes de V(5) e X(10) para formar 4 e 9.
# X pode ser colocado antes de L(50) e C(100) para formar 40 e 90.
# C pode ser colocado antes de D(500) e M(1000) para perfazer 400 e 900.

def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        current_value = roman_values[char]
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value
    
    return total

roman_number = "MMCMXLIX"
decimal_number = roman_to_int(roman_number)
print(f'O número decimal correspondente a {roman_number} é: {decimal_number}')
