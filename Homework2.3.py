
print('Введите число')
number2 = input()
import random

q = random.randint(1, 100)
if int(number2) < q:
      print('Вы ввели число ' + number2 + ', которое меньше ' + str(q))
elif int(number2) > q:
     print('Вы ввели число ' + number2 + ', которое больше ' + str(q))
else:
     print('Вы ввели число ' + number2 + ', которое равно ' + str(q))
