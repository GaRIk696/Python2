def find_intersection():
    list1 = list(map(int, input("Введите первый список: ").split()))
    list2 = list(map(int, input("Введите второй список: ").split()))
    intersection = set(list1) & set(list2)
    common_elements = sorted(intersection)

    print("Общие элементы:", " ".join(map(str, common_elements)))
find_intersection()