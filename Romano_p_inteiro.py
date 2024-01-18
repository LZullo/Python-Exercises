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

s="LVIII"

def romanToInt(s):
  translations = {
      "I": 1, "V": 5, "D": 500,
      "X": 10,"L": 50, "C": 100,
      "M": 1000
  }
  number = 0
  s = s.replace("IV", "IIII").replace("IX", "VIIII")
  s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
  s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
  for char in s:
      number += translations[char]
  return number

print(romanToInt(s))