def copycontent(fileA, fileB):
    try:
        with open(fileA, 'r') as source:
            content = source.read()
        with open(fileB, 'w') as dest:
            dest.write(content)
    except FileNotFoundError:
        print("not found")
    except Exception as e:
        print("error: ",e)
    