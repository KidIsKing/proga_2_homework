def custom_string_to_int(number):
    if len(number) == 0:
        raise ValueError("Нет числа(")

    result_number = 0
    start_index = 0
    is_negative = False
    if number[0] == "-":
        is_negative = True
        start_index = 1
        if len(number) == 1:
            raise ValueError("Числа нет, только \"-\"")

    for el in range(start_index, len(number)):
        if number[el] < "0" or number[el] > "9":
            raise ValueError("Некоректный символ")

        digit = ord(number[el]) - ord("0")
        result_number = result_number*10 + digit

    if is_negative:
        result_number = -result_number

    return result_number


print(custom_string_to_int("123"))  # Вывод: 123
print(custom_string_to_int("-456"))  # Вывод: -456
print(custom_string_to_int("0"))  # Вывод: 0
print(custom_string_to_int("-0"))  # Вывод: 0
# custom_string_to_int("12a3")  # Должно вызвать ValueError
# custom_string_to_int("")  # Должно вызвать ValueError
