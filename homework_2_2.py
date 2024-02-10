# Задание 2
# Напишите функцию, которая принимает аргумент – список целых чисел A и возвращает 2 списка: нечетных и четных чисел из A.
# Пример: [1, 2, 3, 4, 5]` Возврат: ([1, 3, 5], [2, 4])

# Выполнил Лазо Александр

def list_division (list_numeric: list):
    list_even = []
    list_odd = []
    #for item in range(len(list_numeric)):
    for item in list_numeric:
        if item % 2:
            list_even.append(item)
        else:
            list_odd.append(item)
    return list_even, list_odd

if __name__ == '__main__':
    list_numeric = [1, 2, 3, 4, 5]
    #Вывод результата
    print(list_division(list_numeric))

    # можно реализовать по другому деление двух списков  через filter и lambda
    list_even = list(filter(lambda item: not item % 2, list_numeric))
    list_odd = list(filter(lambda item: item % 2, list_numeric))
