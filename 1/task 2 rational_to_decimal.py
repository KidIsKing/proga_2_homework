def rational_to_decimal(numerator: int, denominator: int, precision: int = 10) -> str:
    """
    Converts a rational number to its decimal representation.

    Args:
    numerator (int): The numerator of the rational number.
    denominator (int): The denominator of the rational number.
    precision (int, optional): The number of decimal places. Defaults to 10.

    Returns:
    str: The decimal representation of the rational number.

    Raises:
    ValueError: If the denominator is zero or inputs are not integers.
    """
    # Проверка типов входных данных
    if not isinstance(numerator, int) or not isinstance(denominator, int) or not isinstance(precision, int):
        raise ValueError("Все аргументы должны быть целыми числами")
    
    # Проверка на ноль в знаменателе
    if denominator == 0:
        raise ValueError("Знаменатель не может быть нулем")

    # Определяем знак результата
    is_negative = False
    if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
        is_negative = True
    # Работаем с положительными числами
    numerator = abs(numerator)
    denominator = abs(denominator)

    # Выделяем целую часть
    integer_part = numerator // denominator
    remainder = numerator % denominator

    # Формируем результат: знак + целая часть + точка
    if is_negative and (integer_part != 0 or remainder != 0):
        result = "-"
    else:
        result = ""
    result += str(integer_part) + "."

    # Для поиска периода будем хранить остатки и их позиции
    remainders = {}  # словарь: остаток -> позиция в дробной части
    decimal_digits = []  # список цифр дробной части
    repeating_start = -1  # начало периода (-1 значит периода нет)
    position = 0  # текущая позиция в дробной части

    # Делим "столбиком" пока не найдем период или остаток не станет 0
    while remainder != 0 and repeating_start == -1:
        # Проверяем, встречали ли этот остаток раньше
        if remainder in remainders:
            repeating_start = remainders[remainder]
            break

        remainders[remainder] = position
        remainder *= 10
        digit = remainder // denominator
        decimal_digits.append(str(digit))
        remainder %= denominator
        position += 1

    # Формируем дробную часть с учетом периода
    if repeating_start != -1:
        # Есть период
        non_repeating = decimal_digits[:repeating_start]  # цифры до периода
        repeating = decimal_digits[repeating_start:]  # цифры периода

        # Собираем результат
        result += "".join(non_repeating)
        
        # Если период длиннее precision, показываем первые precision цифр с многоточием
        if len(repeating) > precision:
            result += "".join(repeating[:precision]) + "..."
        else:
            # Период помещается полностью - показываем в скобках
            result += "(" + "".join(repeating) + ")"
    else:
        # Нет периода (конечная дробь) или достигли точности
        # Добавляем все вычисленные цифры
        result += "".join(decimal_digits)

    # '0.' != '0.0'
    if decimal_digits == []:
        result += "0"

    return result