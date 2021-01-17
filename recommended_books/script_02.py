read = "raw_data.txt"
path = "result.txt"

with open(read, "r", encoding="UTF-8") as f:
    lines = f.readlines()
with open(path, "w", encoding="UTF-8") as f:
    for line in lines:
        string = (line.replace("example", ""))
        f.write(str(string[len("example"):]))
