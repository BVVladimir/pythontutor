#Дано трехзначное число. Найдите сумму его цифр.
a = int(input())
b = 0
while a >= 100 :
    a = a -100
    b = b + 1

while a >= 10 :
    a = a - 10
    b = b + 1

while a > 0 :
    a = a - 1
    b = b + 1    

print(b)