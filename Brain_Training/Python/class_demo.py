class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "play tennis")
        elif self.occupation == "actor":
            print(self.name, "Entertain us")

    def how_famous(self):
        if self.occupation == "tennis player":
            print(self.name + " is sports person")
        else:
            print(self.name + " is not sports person")
