def custom_string_to_int(string_representation: str) -> int:
    """
    Converts a string representation of an integer to its corresponding int value.

    Args:
    string_representation (str): The string to convert. Must represent a valid integer.

    Returns:
    int: The integer value represented by the string.

    Raises:
    ValueError: If the input string is not a valid integer representation.
    """
    # TODO: Implement the conversion logic here

    # Проверка на пустую строку
    if len(string_representation) == 0:
        raise ValueError("Нет числа(")

    result_number = 0
    start_index = 0  # будем проходиться по числу с 1го символа
    is_negative = False

    # Проверка на отрицательность
    if string_representation[0] == "-":
        is_negative = True
        start_index = 1  # будем проходиться по числу со 2го символа
        # Проверка на случай, если после минуса ничего нет
        if len(string_representation) == 1:
            raise ValueError("Числа нет, только \"-\"")

    for el in range(start_index, len(string_representation)):
        # Проверка, что символ действительно цифра (от '0' до '9')
        if string_representation[el] < "0" or string_representation[el] > "9":
            raise ValueError("Некоректный символ")

        # Преобразование символа в цифру: у каждого символа есть числовой
        # код (ASCII), если из кода символа вычесть код '0', получим саму цифру
        digit = ord(string_representation[el]) - ord("0")

        # Как собирается число: умножение на 10 "сдвигает" число влево,
        # освобождая место для новой цифры
        result_number = result_number * 10 + digit

    # Если число было отрицательным - меняем знак
    if is_negative:
        result_number = -result_number

    return result_number
