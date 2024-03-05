import os
path = "C:/Users/ASUS/Desktop/python projects/pythonUni"
def onlydirec(path):
    return [d for d in os.listdir() if os.path.isdir(os.path.join(path, d))]
print(onlydirec(path))

def all(path):
    return os.listdir(path)
print(all(path))
