ticket = input()  # входная строка из шести цифр
digits = [int(d) for d in ticket]  # преобразуем в список цифр
sum1 = sum(digits[:3])  # суммируем первые три цифры
sum2 = sum(digits[3:])  # суммируем последние три цифры
if sum1 == sum2:
    print("Счастливый")
else:
    print("Обычный")








import math

a = int(input())
b = int(input())

lcm = (a * b) // math.gcd(a, b)

print(lcm)