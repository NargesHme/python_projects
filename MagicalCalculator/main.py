import re

print("Our Magical Calculator")
print("Type 'quit' to Exit...")
previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
        print("Goodbye!")
    else:
        equation = re.sub('[A-Za-z.()" ",:]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)



while run:
    perform_math()