import os
def deletepth(path):
    if not os.path.exists(path):
        return False
    if not os.access(path, os.W_OK) or not os.access(path, os.X_OK) or not os.access(path,os.R_OK):
        return False
    try:
        os.remove(path)
        return True
    except OSError as er:
        print("Error ",er)
        return False

    