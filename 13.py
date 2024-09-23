
def check_parts(numbers):
    sum1 = 0
    sum2 = 0
    n_len = len(str(numbers))/2
    for number in str(numbers)[0:int(n_len)]:
        sum1 += int(number)

    for number in str(numbers)[int(n_len):]:
        sum2 += int(number)

    return sum1 == sum2


def main(number):
    first_check = (len(str(number)) % 2) == 0

    if first_check and check_parts(number):
        return False
    else:
        return True


def ticket_input():
    process = True
    i = 0
    while process:
        i += 1
        try:
            ticket = int(input('Введите билет '))
            process = main(ticket)
        except ValueError:
            print('Номер билета может содержать только числа')

    print(f'Введен счастливый билет - {ticket}, его номер - {i}')


ticket_input()
