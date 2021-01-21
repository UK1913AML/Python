import glob, os

class ChangeFileName:
    registered = [".docx", ".xlsx", ".pptx", ".pdf", ".jpg", ".png", ".mp3", ".mp4", ".py", ".ipynb", ".r", ".csv", ".json", ".xml", ".js", ".php", ".html", ".css", ".c", ".cpp", ".cs", ".java", ".sql", ".vb"]
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/result"
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
            ChangeFileName.files = glob.glob(ChangeFileName.path + "/*" + ChangeFileName.registered[int(self.target)-1])

    def change(self):
        for i, f in enumerate(ChangeFileName.files):
            if self.before_or_after == 1:
                os.rename(f, os.path.join(ChangeFileName.path, str(i+1).zfill(self.padding) + self.join + self.string + ChangeFileName.registered[self.extension-1]))
            elif self.before_or_after == 2:
                os.rename(f, os.path.join(ChangeFileName.path, self.string + self.join + str(i+1).zfill(self.padding) + ChangeFileName.registered[self.extension-1]))
