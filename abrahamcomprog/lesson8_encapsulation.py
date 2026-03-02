class BankAccount:
    def __init__(self, balance):
        self._balance = balance # private
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance