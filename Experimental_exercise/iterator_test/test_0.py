class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.indicator = self.start
        return self

    def __next__(self):
        if self.indicator <= self.end:
            i = self.indicator
            self.indicator += 1
            return i
        else:
            raise StopIteration


counter = Counter(0, 5)
count_iter = iter(counter)
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))
