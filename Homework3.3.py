i = input('Введите сумму ')
USD = 72.96
EUR = 85.95
CHF = 79.29
GBP = 100.46
CNY = 11.30
def exchange():
    print('Вы ввели ' + i + ' RUB')
    c = int(i) * USD
    d = int(i) * EUR
    e = int(i) * CHF
    f = int(i) * GBP
    g = int(i) * CNY
    if int(i) <= 0:
        print("Введите положительное число.")
    # elif int(i) = ' ':
    #     print('Вы ввели пустое поле. Введите число.')
    # elif int(i) not str:
    #     print('Вы ввели не число. Введите число.')
    else:
        print('Конвертированная сумма ', ('%.2f' % c), ' USD')
        print('Конвертированная сумма ', ('%.2f' % d), ' EUR')
        print('Конвертированная сумма ', ('%.2f' % e), ' CHF')
        print('Конвертированная сумма ', ('%.2f' % f), ' GBP')
        print('Конвертированная сумма ', ('%.2f' % g), ' CNY')

exchange()