#Дано натуральное число. Найдите число десятков в его десятичной записи.
a = int(input())
a_str = str(a)
if len(a_str) == 1 :
    print('0')
elif len(a_str) > 1 :
    print(a_str[len(a_str)-2])