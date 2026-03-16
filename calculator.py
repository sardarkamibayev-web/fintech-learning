def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

print("Калькулятор")
print("-----------")

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print(f"Сложение: {a} + {b} = {add(a, b)}")
print(f"Вычитание: {a} - {b} = {subtract(a, b)}")
print(f"Умножение: {a} * {b} = {multiply(a, b)}")
print(f"Деление: {a} / {b} = {divide(a, b)}")