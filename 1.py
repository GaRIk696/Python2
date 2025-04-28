i = input("Введите числа через пробела: ")
numbers = i.split()
power = int(input("Введите степень: "))
result = []
for item in numbers:
    try:
        num = float(item)

        if num.is_integer():
            num = int(num)

        powered = num ** power
        result.append(str(powered))
    except ValueError:

        result.append(item * power)
print("Вывод:", " ".join(result))
