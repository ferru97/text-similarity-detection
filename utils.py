import os

def readFileLines(name):
        lines = []
        with open(name, encoding="utf-8") as file_in:
            for line in file_in:
                lines.append(line.strip())
        return lines


def writeFile(name,content):
    with open(name, 'w', encoding="utf-8") as file_out:
        file_out.write(content)


def readFile(name):
    content = ""
    with open(name, 'r', encoding="utf-8") as file_in:
        content = file_in.read()
    return content


def getFilesList(folder, extension=None):
    all_files = []
    for file in os.listdir(folder):
        if extension==None or file.endswith(extension):
            all_files.append(file)
    return all_files