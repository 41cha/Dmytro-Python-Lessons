class NegativeDepositError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class NegativeWithdrawalError(Exception):
    pass

class BankAccount():
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError('Deposit amount cannot be negative')
        self.__balance += amount        
        
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeWithdrawalError('Withdrawal amount cannot be negative')
        
        if amount > self.__balance:
            raise InsufficientFundsError('Not enough funds')

        self.__balance -= amount

    def get_balance(self):
        return self.__balance

acct = BankAccount()

try:
    acct.deposit(100)
    acct.withdraw(50)
    acct.withdraw(100)
except NegativeDepositError as nde:
    print("Deposit error:", nde)
except NegativeWithdrawalError as nwe:
    print("Withdrawal error:", nwe)
except InsufficientFundsError as ife:
    print("Funds error:", ife)
