#В некоторой школе решили набрать три новых математических класса 
#и оборудовать кабинеты для них новыми партами. 
#За каждой партой может сидеть два учащихся. 
#Известно количество учащихся в каждом из трех классов. 
#Выведите наименьшее число парт, которое нужно приобрести для них.
#Программа получает на вход три натуральных числа: 
#количество учащихся в каждом из трех классов.
import math
StudNumClass_1 = int(input())
StudNumClass_2 = int(input())
StudNumClass_3 = int(input())
print(math.trunc((StudNumClass_1 + 1)/2) + \
      math.trunc((StudNumClass_2 + 1)/2) + \
        math.trunc((StudNumClass_3 + 1)/2))
#print(math.trunc((StudNumClass_1 + 1)/2)) 
#print(math.trunc((StudNumClass_2 + 1)/2))
#print(math.trunc((StudNumClass_3 + 1)/2))