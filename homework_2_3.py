# Задание 3
# Напишите функцию, которая принимает 2 аргумента – строка S и строка sep и возвращает новую строку в которой sep вставлен между символами из S.
# Пример:`"Привет", sep="-*-"`Возврат:`"П-*-р-*-и-*-в-*-е-*-т"`
#
# Выполнил Лазо Александр

def join_str(S: str, sep:str) -> str:
    S = "Привет"
    sep = "-*-"
    return sep.join(S)


if __name__ == '__main__':
    str_first = "Привет"
    separator = "-*-"
    print(join_str(str_first, separator))