#Дано положительное действительное число X. Выведите его дробную часть.
#import math
a = float(input())
b = a - int(a)
print(round(b,5))
