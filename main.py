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

    def loop(self):
        while True:
            arg = input('-> ')
            if arg == 'quit':
                print(self.user_string)
                break
            else:
                self.user_string += arg


if __name__ == '__main__':
    g = Gurney()
    g.loop()

    d = Daniel()
    d.loop()

    j = Jonathan()
    j.loop()
