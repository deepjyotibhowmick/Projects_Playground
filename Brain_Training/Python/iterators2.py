class FibonacciSeries():
    def __init__(self, lim):
        self.prev = 0
        self.curr = 1
        self.limit = lim
        self.final = []
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == 0:
            self.final.append(self.prev)
            return self.final[self.index]
        elif self.index > 0 and self.curr >= self.limit:
            raise StopIteration
        else:
            self.final.append(self.curr)
            self.curr = self.prev + self.curr
            self.prev = self.curr - self.prev
            return self.final[self.index]

f = FibonacciSeries(100)

itr = iter(f)

while True:
    try:
        print(next(itr))
    except StopIteration:
        break





