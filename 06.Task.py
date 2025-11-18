#Напишите программу, которая считывает целое число и выводит текст, 
#аналогичный приведенному в примере (пробелы важны!).
#The next number for the number 1534 is 1535.
#The previous number for the number 1534 is 1533.
Number_ = int(input())
Prev_Number = Number_ - 1
Next_Number = Number_ + 1
print('The next number for the number ', Number_, ' is ', Next_Number, '.', sep = '')
print('The previous number for the number ', Number_, ' is ', Prev_Number, '.', sep = '')