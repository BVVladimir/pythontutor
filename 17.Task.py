#Шахматный конь ходит буквой “Г” — на две клетки 
#по вертикали в любом направлении и на одну клетку по горизонтали, 
#или наоборот. Даны две различные клетки шахматной доски, 
#определите, может ли конь попасть с первой клетки на вторую одним ходом.
Column_1 = int(input())
Row_1 = int(input())
Column_2 = int(input())
Row_2 = int(input())

Numbers_ = [1,2,3,4,5,6,7,8]

if Column_1 in Numbers_ and \
Column_2 in Numbers_ and Row_1 in Numbers_ and Row_2 in Numbers_ :

    if (abs(Column_1 - Column_2) == 1 and abs(Row_1 - Row_2) == 2) or \
        (abs(Column_1 - Column_2) == 2 and abs(Row_1 - Row_2) == 1) :
        print('YES')
    else :
        print('NO')
else :
    print('Некорректные координаты')