#Функция конвертации в доллары
# def as_currency(amount):
#     if amount >= 0:
#         return '${:,.2f}'.format(amount)
#     else:
#         return '-${:,.2f}'.format(-amount)

# c = as_currency(-123456.7801)
# print(c)

class MoneyFmt:
    def init(self,cash):
        self.cash = cash

    def update(self,cash):
        self.cash = cash

    def repr(self):
        return f'{self.cash}'


    def dollarize(self):
        if self.cash >= 0:
            return '${:,.2f}'.format(self.cash)
        else:
            return '-${:,.2f}'.format(self.cash)

    def __str__(self):
         return f'Конвертируем число в доллары {self.cash}, ${self.cash}'
        

cash = MoneyFmt(12345678.021)
print(cash.dollarize())
cash.update(100000.4567)
print(cash.dollarize())
cash.update(-0.3)
print(cash.dollarize())
print(repr(cash))
print(cash)