import glob, math, os, random, shutil

class RandomSampling:
    registered = [".docx", ".xlsx", ".pptx", ".pdf", ".jpg", ".png", ".mp3", ".mp4", ".py", ".ipynb", ".r", ".csv", ".json", ".xml", ".js", ".php", ".html", ".css", ".c", ".cpp", ".cs", ".java", ".sql", ".vb"]
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/data"
    result = path + "/result"
    files = ""

    def __init__(self, option, value, extension):
        self.option = option
        self.value = value
        self.extension = extension
    
    def sampling(self):
        RandomSampling.files = glob.glob(RandomSampling.path + "/*" + RandomSampling.registered[int(self.extension)-1])
        if self.option == 1:
            result = random.sample(RandomSampling.files, math.ceil(len(RandomSampling.files)*self.value))
        else:
            result = random.sample(RandomSampling.files, self.value)
        try:
            os.makedirs(RandomSampling.result)
        except:
            pass
        for r in result:
            shutil.copy2(r, RandomSampling.result + "/")
