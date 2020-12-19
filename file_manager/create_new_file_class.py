class CreateNewFile:
    path = "result"
    
    def __init__(self, items, before_or_after, padding, string, join, extension):
        self.items = items
        self.before_or_after = before_or_after
        self.padding = padding
        self.string = string
        self.join = join
        self.extension = extension
    
    def create(self):
        for i in range(self.items):
            if self.before_or_after == 1:
                p = CreateNewFile.path + "/" + str(i+1).zfill(self.padding) + self.join + self.string +  "." + self.extension
                with open(p, "w") as f:
                    f.write("")
            elif self.before_or_after == 2:
                p = CreateNewFile.path + "/" + self.string + self.join + str(i+1).zfill(self.padding) + "." + self.extension
                with open(p, "w") as f:
                    f.write("")
