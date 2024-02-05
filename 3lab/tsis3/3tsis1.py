class tmethods:
    def __init__(self):
        self.inputstring = ""
    
    def getString(self):
        self.inputstring = input("enter string: ")
    def printString(self):
        print(self.inputstring.upper())

instance = tmethods()
instance.getString()
instance.printString()