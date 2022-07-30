msgs = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]

msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(v):
    if -10 < v < 10 and v - round(v) == 0:
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (float(v1) == 1) or (float(v2) == 1) and v3 == '*':
        msg += msg_7
    if ((float(v1) == 0) or (float(v2) == 0)) and ((v3 == '*') or (v3 == '+') or (v3 == '-')):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
    return


result = 0
memory = 0
exit_flag = False
exit_flag1 = False
exit_flag3 = False
exit_flag2 = False
while True:
    while True:

        def is_float(m):
            try:
                float(m)
                return True
            except ValueError:
                return False


        calc = input('Enter an equation')
        calc = calc.split()
        x = calc[0]
        oper = calc[1]
        y = calc[2]
        if x == 'M':
            x = float(memory)
        if y == 'M':
            y = float(memory)
        if is_float(x) and is_float(y):
            if oper == "+":
                x = float(x)
                y = float(y)
                check(x, y, oper)
                result = float(x + y)
                print(result)
                break
            elif oper == '-':
                x = float(x)
                y = float(y)
                check(x, y, oper)
                result = float(x - y)
                print(result)
                break
            elif oper == '*':
                x = float(x)
                y = float(y)
                check(x, y, oper)
                result = float(x * y)
                print(result)
                break
            elif oper == '/' and y != 0:
                x = float(x)
                y = float(y)
                check(x, y, oper)
                result = float(x / y)
                print(result)
                break
            else:
                if y == 0:
                    check(x, y, oper)
                    print("Yeah... division by zero. Smart move...")
                else:
                    print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        else:
            print("Do you even know what numbers are? Stay focused!")
    while True:
        print("Do you want to store the result? (y / n):")
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msgs[msg_index])
                    answer3 = input()
                    if answer3 == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                            continue
                        else:
                            memory = float(result)
                            break
                    else:
                        if answer3 == 'n':
                            break
                        else:
                            continue
            else:
                memory = float(result)
            while True:
                print("Do you want to continue calculations? (y / n):")
                answer1 = input()
                if answer1 != 'y':
                    if answer1 == 'n':
                        exit_flag2 = True
                        exit_flag3 = True
                        exit_flag = True
                        break
                else:
                    if answer1 == 'y':
                        exit_flag = True
                        break
                exit_flag = True
                break
        else:
            while True:
                if answer == 'n':
                    while True:
                        print("Do you want to continue calculations? (y / n):")
                        answer2 = input()
                        if answer2 != 'y':
                            if answer2 == 'n':
                                exit_flag2 = True
                                exit_flag3 = True
                                exit_flag = True
                                break
                        else:
                            if answer2 == 'y':
                                exit_flag3 = True
                                exit_flag = True
                                break
                if exit_flag3:
                    break
        if exit_flag1:
            break
        if exit_flag:
            break
    if exit_flag2:
        break
