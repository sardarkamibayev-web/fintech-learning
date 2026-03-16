# ФУНКЦИИ - многоразовые блоки кода

# Простая функция
def greet(name):
    return f"Привет, {name}!"

print(greet("Sardor"))
print(greet("Revolut"))

# Функция с несколькими параметрами
def transfer(sender, receiver, amount):
    if amount <= 0:
        return "Ошибка: сумма должна быть больше нуля"
    return f"{sender} отправил {receiver} сумму {amount}$"

print(transfer("Sardor", "Amir", 500))
print(transfer("Sardor", "Amir", -100))

# Функция которая что-то считает и возвращает результат
def calculate_fee(amount, percent=0.015):
    fee = amount * percent
    total = amount + fee
    return fee, total

fee, total = calculate_fee(1000)
print(f"Комиссия: {fee}$, Итого: {total}$")

fee, total = calculate_fee(1000, 0.02)
print(f"Комиссия: {fee}$, Итого: {total}$")
