def happiness_ticket(ticket):
    summ_start_numbers = 0
    summ_end_numbers = 0
    for symbol in range(len(ticket)):
        if symbol < 3:
            summ_start_numbers += int(ticket[symbol])
        else:
            summ_end_numbers += int(ticket[symbol])

    if abs(summ_start_numbers - summ_end_numbers) == 1:
        return True
    return False


print(happiness_ticket("111112"))  # True, так как 111111 счастливый
print(happiness_ticket("227535"))  # False
print(happiness_ticket("511112"))  # Fasle
print(happiness_ticket("111110"))  # True, так как 111111 счастливый
print(happiness_ticket("333333"))  # Fasle, так как сам по себе счастливый
print(happiness_ticket("141112"))  # Fasle
