# i = input('Какую сумму выхотите перевести? ')
# i = int(i)
# USD = 72.96
# USD = float(USD)
# def dollar(i, USD):
#
#     if int(i) == 1:
#       print('Вы ввели ' + str(i) + ' рубль')
#     elif int(i) > 1 and int(i) < 5:
#         print('Вы ввели ' + str(i) + ' рубля')
#     elif int(i) > 4 and int(i) < 21:
#         print('Вы ввели ' + str(i) + ' рублей')
#
#     c = i * USD
#     c = float(c)
#
#     # print(type(c))
#     # print(type(i))
#     # print(type(USD))
#     print('Конвертированная сумма в USD ',  '%.2f' % c)
# dollar(i, USD)
#
#
# # ('%.2f' % c)


i = input("Введите жалаемую сумму ")
USD = 72.96
def dollar(i, USD):
    print("Вы ввели " + i + " RUB")
    c = int(i) * USD

    print("Конвертированная сумма ", ("%.2f" % c), " USD")
dollar(i, USD)

