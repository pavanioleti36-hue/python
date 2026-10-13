class InvalidPaymentAmountError(Exception):
    pass
class Payment:
    def pay(self, amount):
        try:
            if amount <= 0:
                raise InvalidPaymentAmountError("Payment amount must be positive")
            print("Payment successful:", amount)
        except InvalidPaymentAmountError as e:
            print(e)
payment = Payment()
payment.pay(-500)