class Test:
    def __init__(self):
        print("Test init")
        self.a = 10
        self.b = 20

    def display(self):
        print("a = ", self.a)
        print("b = ", self.b)


class Demo(Test):
    def __init__(self):
        print("Demo init")
        self.c = 30
        self.d = 40

    def show(self):
        print("c = ", self.c)
        print("d = ", self.d)


def main():
    obj = Demo()
    obj.display()
    obj.show()



def run():
    return main()


if __name__ == '__main__':
    run()