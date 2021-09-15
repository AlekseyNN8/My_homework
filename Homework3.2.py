
i = input('Введите жалаемую сумму ')
USD = 72.96
EUR = 85.95
CHF = 79.29
GBP = 100.46
CNY = 11.30
def dollar(i, USD):
    print('Вы ввели ' + i + ' RUB')
    c = int(i) * USD
    d = int(i) * EUR
    e = int(i) * CHF
    f = int(i) * GBP
    g = int(i) * CNY
    print('Конвертированная сумма ', ('%.2f' % c), ' USD')
    print('Конвертированная сумма ', ('%.2f' % d), ' EUR')
    print('Конвертированная сумма ', ('%.2f' % e), ' CHF')
    print('Конвертированная сумма ', ('%.2f' % f), ' GBP')
    print('Конвертированная сумма ', ('%.2f' % g), ' CNY')
dollar(i, USD)
