list1 = input("Введите первый список через пробел: ").split()
list2 = input("Введите второй список через пробел: ").split()


def num(items):
    nums = []
    for item in items:

        try:
            num = float(item) if '.' in item else int(item)
            nums.append(str(num))
        except ValueError:
            continue
    return nums


num1 = num(list1)
num2 = num(list2)

if not num1 or not num2:
    print("Один или оба списка не содержат чисел.")
else:
    common = set(num1) & set(num2)
    result = ' '.join(common) if common else "нет общих элементов"
    print("Общие элементы:", result)