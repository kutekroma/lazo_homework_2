### Задание 1
# Напишите функцию, которая принимает параметр – натуральное число N и выводит на экран линию из N символов '–'.
# Пример: Введите N: 10 `----------`

# Выполнил Лазо Александр

def print_line (number_line):
    print('-'*int(number_line))

if __name__ == '__main__':
    #Ввод данных с клавиатуры
    number = input("Введите целое N: ")
    #Проверка на ввод числа
    while not number.isdigit():
        print("Вводите только целое число")
        number = input("Введите целое N: ")
    print_line(number)
