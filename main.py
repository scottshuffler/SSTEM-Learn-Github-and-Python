class Gurney:
    def __init__(self):
        self.user_string = ''

    def loop(self):
        while True:
            arg = input('-> ')
            if arg == 'quit':
                print(self.user_string)
                break
            else:
                self.user_string += arg


class Daniel:
    def __init__(self):
        self.user_string = ''

    def loop(self):
        while True:
            arg = input('-> ')
            if arg == 'quit':
                print(self.user_string)
                break
            else:
                self.user_string += arg


class Jonathan:
    def __init__(self):
        self.user_string = ''

    def add(self, uno, dos):
        addop = uno + dos
        return addop

    def subtract(self, num1, num2):
        subop = num1 - num2
        return subop
    def multiply(self, num1, num2):
        multop = num1 * num2
        return multop
    def divide(self, num1, num2):
        divop = num1 / num2
        return divop
    def main(self):
        print('ezpz calculatorino')
        while True:
            num1 = int(input('Enter your first number: '))
            op = input('Choose an operator(+,-,*,/)')
            num2 = int(input('Enter your second number: '))
            if (op == '+'):
                answer = Jonathan().add( num1, num2)
                print(num1, "+", num2, "=", answer)
                break
            elif (op == '-'):
                answer = Jonathan().subtract(num1, num2)
                print(num1, "-", num2, "=", answer)
                break
            elif (op == '*'):
                answer = Jonathan().multiply(num1, num2)
                print(num1, "*", num2, "=", answer)
                break
            elif (op == '/'):
                answer = Jonathan().divide(num1, num2)
                print(num1, "/", num2, "=", answer)
                break
            else:
                print('invalid string') 


if __name__ == '__main__':
    g = Gurney()
    g.loop()

    d = Daniel()
    d.loop()

    j = Jonathan()
    j.main()
