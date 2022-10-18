"""
Ввести с клавиатуры целое число n.

Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.

Реализовать в 2-х вариантах: используя цикл while и цикл for
"""
n = int(input("Enter the value: "))
amount = 0
for i in range(1, n+1):
    if not i % 3 == 0:
        i **= 3
        amount += i
print(amount)

a = 0
i = 1
amount = 0
while a <= n:
    if a % 3 == 0:
        a += 1
        continue
    i = a**3
    amount += i
    a += 1
print(amount)