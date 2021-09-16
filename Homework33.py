while True:
    try:
        rubl = int(input('Введите сумму: '))
        if int(rubl) <= 0:
            print('Вы ввели меньше нуля ')
            continue
    except ValueError:
        print("Вы ввели не число. Попробуйте заново.")
        continue
    else:
        def exchange():
            rubl_euro = int(rubl) * 0.0116
            rubl_usd = int(rubl) * 0.0138
            rubl_GBP = int(rubl) * 0.0099
            rubl_CHF = int(rubl) * 0.0127
            rubl_CNY = int(rubl) * 0.0886
            print('Конвертируем в долляры', ('%.4f' % rubl_usd), 'USD')
            print('Конвертируем в еврики', ('%.4f' %rubl_euro), 'EUR')
            print('Конвертируем в стерлинги', ('%.4f' %rubl_GBP), 'GBP')
            print('Конвертируем в юани', ('%.4f' %rubl_CHF), 'CHF')
            print('Конвертируем во что не понятное', ('%.4f' %rubl_CNY), 'CNY')
                 # print(type(rubl_euro))
        exchange()
        break

# i = input('Введите сумму ')
# USD = 0.0138
# EUR = 0.0116
# CHF = 0.0127
# GBP = 0.0099
# CNY = 0.0886
# def exchange():
#     if not i.isdigit():
#         return input('Вы ввели не число, повторите снова ')
#     elif not 0 <= int(i):
#         return print("Введите положительное число.")
#     print('Вы ввели ' + i + ' RUB')
#     c = int(i) * USD
#     d = int(i) * EUR
#     e = int(i) * CHF
#     f = int(i) * GBP
#     g = int(i) * CNY
#     print('Конвертированная сумма ', ('%.4f' % c), ' USD')
#     print('Конвертированная сумма ', ('%.4f' % d), ' EUR')
#     print('Конвертированная сумма ', ('%.4f' % e), ' CHF')
#     print('Конвертированная сумма ', ('%.4f' % f), ' GBP')
#     print('Конвертированная сумма ', ('%.4f' % g), ' CNY')
#
#
#     while True:
#         if not i.isnumeric():
#             return input("Вы ввели не число. Попробуйте снова: ")
#         elif not 0 <= int(i):
#             return input("Введите положительное число.")
#             # break
# exchange()