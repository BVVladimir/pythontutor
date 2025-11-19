#Заданы две клетки шахматной доски. 
#Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO. 
#Программа получает на вход четыре числа от 1 до 8 каждое, 
#задающие номер столбца и номер строки сначала для первой клетки, 
# потом для второй клетки.
Numbers_ = [1,2,3,4,5,6,7,8]
Column1 = int(input())
Row1 = int(input())
Column2 = int(input())
Row2 = int(input())
if Column1 and Row1 and Column2 and Row2 in Numbers_ :
    Sum_ = Column1 + Row1 + Column2 + Row2
if Sum_%2 == 0 : 
    print('YES')
else: 
    print('NO')