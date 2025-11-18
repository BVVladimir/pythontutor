#n школьников делят k яблок поровну, 
# неделящийся остаток остается в корзинке. 
# Сколько яблок достанется каждому школьнику? 
# Сколько яблок останется в корзинке? Программа получает на вход 
# числа n и k и должна вывести искомое количество яблок (два числа).
import math
n_pupils = int(input())
k_apples = int(input())
Sum = k_apples/n_pupils
print(math.trunc(Sum)) #math.trunc возвращает целое без остатка
print(k_apples - n_pupils * math.trunc(Sum))
