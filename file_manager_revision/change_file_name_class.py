import glob, os, shutil

class ChangeFileName:
    registered = [".docx", ".xlsx", ".pptx", ".pdf", ".jpg", ".png", ".mp3", ".mp4", ".py", ".ipynb", ".r", ".csv", ".json", ".xml", ".js", ".php", ".html", ".css", ".c", ".cpp", ".cs", ".java", ".sql", ".vb"]
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/data"
    result = path + "/result"
    copy = ""
    rename = ""

    def __init__(self, target, position, padding, string, join, extension):
        self.target = target
        self.position = position
        self.padding = padding
        self.string = string
        self.join = join
        self.extension = extension

    def change(self):
        if self.target == "":
            ChangeFileName.copy = glob.glob(ChangeFileName.path + "/*")
        else:
            ChangeFileName.copy = glob.glob(ChangeFileName.path + "/*" + ChangeFileName.registered[int(self.target)-1])
        try:
            os.makedirs(ChangeFileName.result)
        except:
            pass      
        for c in ChangeFileName.copy:
            shutil.copy2(c, ChangeFileName.result + "/")
        if self.target == "":
            ChangeFileName.rename = glob.glob(ChangeFileName.result + "/*")
        else:
            ChangeFileName.rename = glob.glob(ChangeFileName.result + "/*" + ChangeFileName.registered[int(self.target)-1])
        for i, r in enumerate(ChangeFileName.rename):
            if self.position == 1:
                os.rename(r, os.path.join(ChangeFileName.result, str(i+1).zfill(self.padding) + self.join + self.string + ChangeFileName.registered[self.extension-1]))
            else:
                os.rename(r, os.path.join(ChangeFileName.result, self.string + self.join + str(i+1).zfill(self.padding) + ChangeFileName.registered[self.extension-1]))
