class ExtendedStack(list):
    def sum(self):  # операция сложения
        first = self.pop()
        second = self.pop()
        res = first + second
        self.append(res)
        return self

    def sub(self):  # операция вычитания
        first = self.pop()
        second = self.pop()
        res = first - second
        self.append(res)
        return self

    def mul(self):  # операция умножения
        first = self.pop()
        second = self.pop()
        res = first * second
        self.append(res)
        return self

    def div(self):  # операция целочисленного деления
        first = self.pop()
        second = self.pop()
        res = first // second
        self.append(res)
        return self
