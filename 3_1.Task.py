#Дано натуральное число. Выведите его последнюю цифру.

a = int(input())

a_str = str(a)
print(a_str[len(a_str)-1])