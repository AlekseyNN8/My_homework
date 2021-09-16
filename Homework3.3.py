try:
    rubl = int(input('Введите '))
except ValueError:
    print("Вы ввели не число.")
    exit('Попробуйте заново')
if rubl < 0:
    print('Вы чо бля ')
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
    exchange()

