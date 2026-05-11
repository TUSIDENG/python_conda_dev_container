from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass

class StripeGateway(PaymentGateway):
    def charge(self, amount):
        return f"Stripe charged {amount}"

    def refund(self, transaction_id):
        return f"Stripe refunded {transaction_id}"

# PaymentGateway()  # TypeError: 抽象类不能实例化
gateway = StripeGateway()
print(gateway.charge(100))  # Stripe charged 100
print(gateway.refund("txn_123"))  # Stripe refunded txn_123

print(isinstance(gateway, StripeGateway))       # True
print(isinstance(gateway, PaymentGateway))       # True
print(isinstance(gateway, ABC))                  # True
print(issubclass(StripeGateway, PaymentGateway))  # True
print(issubclass(StripeGateway, ABC))            # True