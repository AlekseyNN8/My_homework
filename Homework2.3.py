



# IN Process
# loading ............... 10 %

print('Введите число')
number2 = input()
import random

q = random.randint(1, 100)
w = random.randint(1, 100)
if q > int(number2) and w > int(number2):
    print('Вы ввели число ' + number2 + ', которое меньше ' + str(q) + ' и меньше ' + str(w))
if q > int(number2) and w < int(number2):
    print('Вы ввели число ' + number2 + ', которое меньше ' + str(q) + ' и больше ' + str(w))
if q < int(number2) and w < int(number2):
    print('Вы ввели число ' + number2 + ', которое больше ' + str(q) + ' и больше ' + str(w))
if q < int(number2) and w > int(number2):
    print('Вы ввели число ' + number2 + ', которое больше ' + str(q) + ' и меньше ' + str(w))
if q == int(number2) and w == int(number2):
    print('Ура! Вы ввели число ' + number2 + ', которое равно' + str(q) + ' и равно ' + str(w) + '/nВы супер герой!')



