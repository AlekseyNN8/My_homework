# 7) Сделать скрипт используя функцию input().

print('Введите число')
number = input()

if int(number) < 30:
   print('Вы ввели число ' + number + ', которое меньше 30')

elif int(number) > 30:
   print('Вы ввели число ' + number + ', которое больше 30' )
else:
   print('Вы ввели число ' + number + ', которое равно 30')
