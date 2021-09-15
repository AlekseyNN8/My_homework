i = input('Введите сумму ')
USD = 0.0138
EUR = 0.0116
CHF = 0.0127
GBP = 0.0099
CNY = 0.0886
def exchange():
    if not i.isdigit():
        return input('Вы ввели не число, повторите снова ')
    print('Вы ввели ' + i + ' RUB')
    c = int(i) * USD
    d = int(i) * EUR
    e = int(i) * CHF
    f = int(i) * GBP
    g = int(i) * CNY
    print('Конвертированная сумма ', ('%.4f' % c), ' USD')
    print('Конвертированная сумма ', ('%.4f' % d), ' EUR')
    print('Конвертированная сумма ', ('%.4f' % e), ' CHF')
    print('Конвертированная сумма ', ('%.4f' % f), ' GBP')
    print('Конвертированная сумма ', ('%.4f' % g), ' CNY')
    while True:
        if not i.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        elif not 0 <= int(i):
            print("Введите положительное число.")
        break
exchange()