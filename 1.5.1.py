
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0

    def can_add(self, v):
        if self.capacity >= v + self.counter:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.counter += v

t = MoneyBox(4)
t.add(1)
t.can_add(10)
t.add(6)
print(t.counter)
