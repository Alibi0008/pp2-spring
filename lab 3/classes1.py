class twomethods:
    def __init__(self):
        self.input = ""
    def getString(self):
        self.input = input()
    def printString(self):
        self.input = print(self.input.upper())
a  = twomethods()
a.getString()
a.printString()