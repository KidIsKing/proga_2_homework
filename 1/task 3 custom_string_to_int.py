def custom_string_to_int(number):
    # Проверка на пустую строку
    if len(number) == 0:
        raise ValueError("Нет числа(")

    result_number = 0
    start_index = 0  # будем проходиться по числу с 1го символа
    is_negative = False

    # Проверка на отрицательность
    if number[0] == "-":
        is_negative = True
        start_index = 1  # будем проходиться по числу со 2го символа
        # Проверка на случай, если после минуса ничего нет
        if len(number) == 1:
            raise ValueError("Числа нет, только \"-\"")

    for el in range(start_index, len(number)):
        # Проверка, что символ действительно цифра (от '0' до '9')
        if number[el] < "0" or number[el] > "9":
            raise ValueError("Некоректный символ")

        # Преобразование символа в цифру: у каждого символа есть числовой
        # код (ASCII), если из кода символа вычесть код '0', получим саму цифру
        digit = ord(number[el]) - ord("0")

        # Как собирается число: умножение на 10 "сдвигает" число влево,
        # освобождая место для новой цифры
        result_number = result_number * 10 + digit

    # Если число было отрицательным - меняем знак
    if is_negative:
        result_number = -result_number

    return result_number


print(custom_string_to_int("123"))  # Вывод: 123
print(custom_string_to_int("-456"))  # Вывод: -456
print(custom_string_to_int("0"))  # Вывод: 0
print(custom_string_to_int("-0"))  # Вывод: 0
# custom_string_to_int("12a3")  # Должно вызвать ValueError
# custom_string_to_int("")  # Должно вызвать ValueError
