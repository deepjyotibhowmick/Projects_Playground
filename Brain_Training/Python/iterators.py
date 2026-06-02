class RemoteControl():
    def __init__(self):
        self.channel = ['ESPN', 'TEN1', 'TEN2', 'Start Sports1', 'Start Sports2']
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.index += 1
            if self.index == len(self.channel):
                raise StopIteration("Reached the end of the channel sequence.")
            else:
                return self.channel[self.index]
        except StopIteration as e:
            print(f"Iteration stopped. Reason: {e}")

r = RemoteControl()
itr = iter(r)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))