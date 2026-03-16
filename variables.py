# ТИПЫ ДАННЫХ в Python

# int - целое число
age = 25
balance = 1000

# float - число с точкой (деньги всегда float!)
amount = 99.99
rate = 0.05

# str - строка (текст)
name = "Sardor"
bank = "Revolut"

# bool - True или False (да/нет)
is_verified = True
is_blocked = False

# None - пустое значение (аккаунт ещё не создан)
account_id = None

# Выводим всё на экран
print(f"Имя: {name}")
print(f"Банк: {bank}")
print(f"Баланс: {balance}")
print(f"Верифицирован: {is_verified}")
print(f"ID аккаунта: {account_id}")

# УСЛОВИЯ - if/elif/else
print("\n--- Проверка баланса ---")

if balance >= 1000:
    print("Статус: Премиум клиент")
elif balance >= 500:
    print("Статус: Обычный клиент")
else:
    print("Статус: Пополни счёт!")

# Проверка верификации (важно в финтехе!)
if is_verified and not is_blocked:
    print("Транзакция разрешена ✓")
else:
    print("Транзакция заблокирована ✗")
    
