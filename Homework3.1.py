print('Введите жалаемую сумму')
i = input()
USD = 72.96
def dollar(i, USD):
    print('Ты ввёл ' + i + 'рубля')
    c = int(i) * USD

    print('Конвертированная сумма в USD', ('%.2f' % c))
dollar(i, USD)


