def countline(file):
    with open(file, 'r') as fl:
        lines = fl.readlines()
        return len(lines)
