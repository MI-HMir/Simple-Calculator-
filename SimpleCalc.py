
while True:

    try:
        num1 = float(input('Enter first number:'))
        num2 = float(input('Enter second number:'))



    except:
        print("Sorry I don't understand, please try again.")

        continue

    else:
        break

while True:
    sym = input('Addition, Subtraction, Multiplication or Division?:')
    if sym == 'multiplication' or sym == 'm' or sym =='multiply' or sym == 'Multiply' or sym == 'mul' or sym == 'x' or sym =='*':
        print(num1 * num2)
        break

    elif sym == 'add' or sym =='addition' or sym == 'a' or sym =='plus' or sym == 'Addition' or sym =='+':
        print(num1 + num2)
        break

    elif sym == 'division' or sym == 'div' or sym == 'd' or sym == 'Division' or sym =='divide' or sym =='/':
        print(num1 / num2)
        break

    elif sym == 'subtract' or sym == 'sub' or sym == 's' or sym == 'Subtract' or sym == 'take away' or sym == 'takeaway'or sym =='minus'or sym =='-':
        print(num1 - num2)
        break

    else:
        print("Sorry I don't understand, please try again.")
        continue


    quit()
