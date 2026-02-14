def rational_to_decimal(numerator, denominator, precision=10):
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

    # Если число целое (нет остатка)
    if remainder == 0:
        # Добавляем нужное количество нулей после запятой
        result += "0" * precision
        return result

    # Для поиска периода будем хранить остатки и их позиции
    remainders = {}  # словарь: остаток -> позиция в дробной части
    decimal_digits = []  # список цифр дробной части
    repeating_start = -1  # начало периода (-1 значит периода нет)
    position = 0  # текущая позиция в дробной части

    # Делим "столбиком" пока не найдем период или не достигнем точности
    while (
        remainder != 0
        and (repeating_start == -1)
        and len(decimal_digits) < precision * 2
    ):
        # Запоминаем позицию текущего остатка
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
        result += "(" + "".join(repeating) + ")"

        # Если точность больше, чем мы вычислили, добавляем многоточие
        if precision > len(decimal_digits):
            result += "..."
    else:
        # Нет периода (конечная дробь) или достигли точности
        # Добавляем все вычисленные цифры
        result += "".join(decimal_digits)
        # Если нужно больше цифр, добавляем нули
        if len(decimal_digits) < precision:
            result += "0" * (precision - len(decimal_digits))

    return result


print(rational_to_decimal(1, 2))  # "0.5"
print(rational_to_decimal(1, 3))  # "0.(3)"
print(rational_to_decimal(5, 6))  # "0.8(3)"
print(rational_to_decimal(-1, 4))  # "-0.25"
print(rational_to_decimal(1, 7, 6))  # "0.(142857)..."
