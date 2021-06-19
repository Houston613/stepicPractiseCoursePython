class Buffer:
    def __init__(self):
        self.current_part = []

    def add(self, *a):
        global sum5
        self.current_part.extend(a)

        while len(self.current_part) >= 5:

            count = 0
            sum5 = 0
            remover = 0

            while count != 5:
                sum5 += self.current_part[count]
                count += 1

            print(sum5)
            while remover != 5:
                del self.current_part[0]
                remover += 1

    def get_current_part(self):
        print(self.current_part)
        return self.current_part


buf = Buffer()

buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
