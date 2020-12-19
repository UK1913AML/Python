import glob, os

class ChangeFileName:
    path = "result"
    files = ""

    def __init__(self, target, before_or_after, padding, string, join, extension):
        self.target = target
        self.before_or_after = before_or_after
        self.padding = padding
        self.string = string
        self.join = join
        self.extension = extension

    def target_extension(self):
        if self.target == "":
            ChangeFileName.files = glob.glob(ChangeFileName.path + "/*")
        else:
            ChangeFileName.files = glob.glob(ChangeFileName.path + "/*." + self.target)

    def change(self):
        for i, f in enumerate(ChangeFileName.files):
            if self.before_or_after == 1:
                os.rename(f, os.path.join(ChangeFileName.path, str(i+1).zfill(self.padding) + self.join + self.string + "." + self.extension))
            elif self.before_or_after == 2:
                os.rename(f, os.path.join(ChangeFileName.path, self.string + self.join + str(i+1).zfill(self.padding) + "." + self.extension))
