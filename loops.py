transactions = [100, 250, 50, 1000, 75]

print("--- История транзакций ---")
total = 0
for amount in transactions:
    total += amount
    print(f"Транзакция: {amount} | Итого: {total}")

print(f"Общая сумма: {total}")

print("--- Снятие денег ---")
balance = 500

while balance > 0:
    balance -= 100
    print(f"Сняли 100. Остаток: {balance}")

print("Баланс исчерпан!")