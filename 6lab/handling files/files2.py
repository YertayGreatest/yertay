import os
def checkpath(path):
    existence = os.path.exists(path)
    print(existence)
    redability = os.access(path, os.R_OK)
    print(redability)
    writable = os.access(path, os.W_OK)
    print(writable)
    execute = os.access(path, os.X_OK)
    print(execute)
path = "C:/Users/ASUS/Desktop/python projects/pythonUni"
print(checkpath(path))
    