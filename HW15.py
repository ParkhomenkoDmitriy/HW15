def entered_number(input_str):
    if input_str == '0':
        return "Ви ввели нуль"

    if '-' in input_str:
        if '.' in input_str or ',' in input_str:
            if input_str.count('.') == 1 or input_str.count(',') == 1:
                number = input_str.split('.') if '.' in input_str else input_str.split(',')
                if len(number[0]) == 1 and number[0] == '-':
                    number[0] += '0'
                if number[0].replace('-', '').isdigit() and number[1].isdigit():
                    return f"Ви ввели від'ємне дробове число: {input_str}"
                else:
                    return f"Ви ввели неправильне число: {input_str}"
            else:
                return f"Ви ввели неправильне число: {input_str}"
        else:
            return f"Ви ввели від'ємне ціле число: {input_str}"

    if '.' in input_str or ',' in input_str:
        if input_str.count('.') == 1 or input_str.count(',') == 1:
            number = input_str.split('.') if '.' in input_str else input_str.split(',')
            if len(number[0]) == 0:
                number[0] = '0'
            if number[0].isdigit() and number[1].isdigit():
                return f"Ви ввели позитивне дробове число: {input_str}"
            else:
                return f"Ви ввели неправильне число: {input_str}"
        else:
            return f"Ви ввели неправильне число: {input_str}"
    elif input_str.isdigit():
        return f"Ви ввели позитивне ціле число: {input_str}"
    else:
        return f"Ви ввели неправильне число: {input_str}"


while True:
    user_input = input("Введіть число або 'вихід', 'exit', 'quit', 'e' або 'q' для виходу: ").lower()
    if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
        print("Програма завершена.")
        break
    else:
        result = entered_number(user_input)
        print(result)
