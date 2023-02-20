class Money():
    RUB = ['Российский рубль', 'RUB']
    USD = ['Доллар США', 'USD']
    EUR = ['Евро', 'EUR']
    GBP = ['Фунт стерлингов Соединённого королевства', 'GBP']
    BYN = ['Белорусский рубль', 'BYN']
    CNY = ['Китайский юань', 'CNY']
    RSD = ['Сербский динар', 'RSD']
    INR = ['Индийская рупия', 'INR']
    BRL = ['Бразильский реал', 'BRL']
    TRY = ['Турецкая лира', 'TRY']
    CHF = ['Швейцарский франк', 'CHF']
    KZT = ['Казахстанский тенге', 'KZT']
    JPY = ['Японская йена', 'JPY']
    KRW = ['Южнокорейская вона', 'KRW']
    PLN = ['Польский злотый', 'PLN']
    all_value = [RUB, USD, EUR, GBP, BYN, CNY, RSD, INR, BRL, TRY, CHF, KZT, JPY, KRW, PLN]

    @staticmethod
    def get_price(base, quote, amount):
        rez = (base/quote)*amount
        return round(rez, 2)