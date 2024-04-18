import re

def entered_number(input_str):
    if re.match(r'^-?\d*(?:[\.,]?\d+)?$', input_str):
        if input_str.replace(',', '').replace('.', '') == '0':
            return "You entered zero 0"
        if input_str.startswith('-') and '.' not in input_str and ',' not in input_str:
            if input_str.lstrip('-0') == '':
                return "You entered zero 0"
            else:
                return f"You entered a negative integer: {input_str}"
        if input_str.startswith('-'):
            return f"You entered a negative fractional number: {input_str}"
        if '.' not in input_str and ',' not in input_str:
            if input_str.lstrip('0') == '':
                return "You entered zero 0"
            else:
                return f"You entered a positive integer: {input_str}"
        return f"You entered a positive fractional number: {input_str}"

    return f"You have entered an incorrect number: {input_str}"

while True:
    user_input = input("Enter a number or 'вихід', 'exit', 'quit', 'e' or 'q' to exit: ").lower()
    if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
        print("The program is complete.")
        break
    else:
        result = entered_number(user_input)
        print(result)
