def writelist(data, file):
    with open(file) as fl:
        for i in data:
            fl.write(str(i))
