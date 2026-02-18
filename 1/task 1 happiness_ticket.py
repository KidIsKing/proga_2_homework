def is_almost_lucky(ticket_number: str) -> bool:
    """
    Checks if the ticket number is "almost lucky".

    An "almost lucky" ticket is one where the sum of the first three digits
    differs from the sum of the last three digits by exactly 1 (in either direction).

    :param ticket_number: Six-digit ticket number
    :return: True if the ticket is "almost lucky", False otherwise
    """
    # TODO: Implement the check for an "almost lucky" ticket

    # Валидация входных данных
    if not ticket_number.isdigit() or len(ticket_number) != 6:
        raise ValueError("Неподходящие данные")

    number = int(ticket_number)

    # Обработка граничного случая "000000"
    if number == 0:
        prev_ticket = None
    else:
        prev_ticket = str(number - 1).zfill(6)

    # Обработка граничного случая "999999"
    if number == 999999:
        next_ticket = None
    else:
        next_ticket = str(number + 1).zfill(6)

    def is_lucky(ticket: str) -> bool:
        """Вспомогательная функция проверки счастья"""
        left_sum = sum(int(d) for d in ticket[:3])  # Первые 3 цифры
        right_sum = sum(int(d) for d in ticket[3:])  # Последние 3 цифры
        return left_sum == right_sum

    # Проверка: предыдущий ИЛИ следующий билет счастливый
    if (prev_ticket and is_lucky(prev_ticket)) or (
        next_ticket and is_lucky(next_ticket)
    ):
        return True
    return False
