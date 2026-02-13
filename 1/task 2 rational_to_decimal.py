def rational_to_decimal(numerator, denominator, precision=10):
    result = f"{numerator/denominator}"  # :.{precision}f
    # перевод строки во float и удаление незначащих нулей
    float_result = float(result.strip("0"))
    # for numb in range(len(result[2:])):
    #     for el in result[numb]:
    #         if el[]
    return float_result


print(rational_to_decimal(1, 2))  # Вывод: "0.5"
print(rational_to_decimal(1, 3))  # Вывод: "0.(3)"
print(rational_to_decimal(5, 6))  # Вывод: "0.8(3)"
print(rational_to_decimal(-1, 4))  # Вывод: "-0.25"
print(rational_to_decimal(1, 7, 6))  # Вывод: "0.(142857)..."
