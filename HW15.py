def entered_number(input_str):
    if input_str == '0':
        return "You entered zero"

    if '-' in input_str:
        if '.' in input_str or ',' in input_str:
            if input_str.count('.') == 1 or input_str.count(',') == 1:
                number = input_str.split('.') if '.' in input_str else input_str.split(',')
                if len(number[0]) == 1 and number[0] == '-':
                    number[0] += '0'
                if number[0].replace('-', '').isdigit() and number[1].isdigit():
                    return f"You entered a negative fractional number: {input_str}"
                else:
                    return f"You have entered an incorrect number: {input_str}"
            else:
                return f"You have entered an incorrect number: {input_str}"
        else:
            return f"You entered a negative integer: {input_str}"

    if '.' in input_str or ',' in input_str:
        if input_str.count('.') == 1 or input_str.count(',') == 1:
            number = input_str.split('.') if '.' in input_str else input_str.split(',')
            if len(number[0]) == 0:
                number[0] = '0'
            if number[0].isdigit() and number[1].isdigit():
                return f"You entered a positive fractional number: {input_str}"
            else:
                return f"You have entered an incorrect number: {input_str}"
        else:
            return f"You have entered an incorrect number: {input_str}"
    elif input_str.isdigit():
        return f"You entered a positive integer: {input_str}"
    else:
        return f"You have entered an incorrect number: {input_str}"


while True:
    user_input = input("Enter a number or 'вихід', 'exit', 'quit', 'e' or 'q' to exit: ").lower()
    if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
        print("The program is complete.")
        break
    else:
        result = entered_number(user_input)
        print(result)
