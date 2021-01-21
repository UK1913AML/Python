import os

class CreateNewFile:
    registered = [".py", ".ipynb", ".r", ".csv", ".json", ".xml", ".js", ".php", ".html", ".css", ".c", ".cpp", ".cs", ".java", ".sql", ".vb"]
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/result"

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
                p = CreateNewFile.path + "/" + str(i+1).zfill(self.padding) + self.join + self.string + CreateNewFile.registered[self.extension-1]
                with open(p, "w", encoding="UTF-8") as f:
                    f.write("")
            elif self.before_or_after == 2:
                p = CreateNewFile.path + "/" + self.string + self.join + str(i+1).zfill(self.padding) + CreateNewFile.registered[self.extension-1]
                with open(p, "w", encoding="UTF-8") as f:
                    f.write("")
