from lesson8_encapsulation import BankAccount

account = BankAccount(1000)
account.deposit(500)

print(account.get_balance())

account.withdraw(200)
print(account.get_balance())

