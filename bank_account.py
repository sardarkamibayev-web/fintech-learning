class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Ошибка: сумма должна быть больше нуля"
        self.balance += amount
        return f"Пополнено на {amount}. Баланс: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Ошибка: сумма должна быть больше нуля"
        if amount > self.balance:
            return "Ошибка: недостаточно средств"
        self.balance -= amount
        return f"Снято {amount}. Баланс: {self.balance}"

    def get_balance(self):
        return f"Владелец: {self.owner} | Баланс: {self.balance}"


# Создаём счета
account1 = BankAccount("Sardor", 500)
account2 = BankAccount("Amir")

print(account1.get_balance())
print(account2.get_balance())

print(account1.deposit(200))
print(account1.withdraw(100))
print(account1.withdraw(1000))
print(account2.deposit(-50))
