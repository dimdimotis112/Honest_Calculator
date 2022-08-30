def start():
    print("Enter an equation")
    calc = input()
    return calc


def splitter(user_input):
    x, oper, y = user_input.split()
    return x, oper, y


def converter(x, y):
    try:
        if '.' in x:
            x = float(x)
        elif x == 'M':
            x = memory
        else:
            x = int(x)

        if '.' in y:
            y = float(y)
        elif y == 'M':
            y = memory
        else:
            y = int(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        return x, y, False
    else:
        return x, y, True


def operand_check(operand):
    if operand not in ('+', '-', '*', '/'):
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        return False

    return True


def is_one_digit(number):
    if isinstance(number, float):
        if -10 < number < 10 and number.is_integer():
            return True
        return False
    else:
        if -10 < number < 10:
            return True
        return False


def laziness_checker(x, y, operand):
    msg = ""

    if is_one_digit(x) and is_one_digit(y):
        msg = msg + " ... lazy"
    if float(x) == 1.0 or float(y) == 1.0 and operand == '*':
        msg = msg + " ... very lazy"
    if float(x) == 0.0 or float(y) == 0.0 and operand in ('*', '+', '-'):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


def calculate(x, operand, y):
    if operand == '+':
        return float(x + y)
    elif operand == '-':
        return float(x - y)
    elif operand == '*':
        return float(x * y)
    elif operand == '/':
        if y == 0:
            return False
        else:
            return float(x / y)


def continue_input(result):
    def continue_calculations():
        while True:
            print("Do you want to continue calculations? (y / n):")
            proceed = input()

            if proceed == 'y':
                return 'toStart'
            elif proceed == 'n':
                return 'exit'
            else:
                continue

    while True:
        print("Do you want to store the result? (y / n):")
        answer = input()
        messages = ["Are you sure? It is only one digit! (y / n)",
                    "Don't be silly! It's just one number! Add to the memory? (y / n)",
                    "Last chance! Do you really want to embarrass yourself? (y / n)"]
        msg_index = 0

        global memory

        if answer == 'y':
            if is_one_digit(result):
                while True:
                    print(messages[msg_index])
                    answer_to_msg = input()
                    if answer_to_msg == 'y':
                        if msg_index < 2:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer_to_msg == 'n':
                        break
                    else:
                        continue
            else:
                memory = result
            return continue_calculations()
        elif answer == 'n':
            return continue_calculations()
        else:
            continue


memory = 0

while True:
    calc = start()
    x, oper, y = splitter(calc)
    x, y, passed = converter(x, y)
    is_operand = operand_check(oper)

    if not passed or not is_operand:
        continue
    elif passed and is_operand:
        result = calculate(x, oper, y)
        if oper == '*' and result == 0.0 or result:  # If result is successfully printed, continue with asking user if they wish to continue.
            laziness_checker(x, y, oper)
            print(result)
            user_action = continue_input(result)
            if user_action == 'toStart':
                continue
            elif user_action == 'exit':
                pass
        else:
            laziness_checker(x, y, oper)
            print("Yeah... division by zero. Smart move...")
            continue

        break
