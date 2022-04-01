class Jafri:
    def __init__(self):
        self.name = None
        self.u_id = None

    def getData(self):
        self.name = input("Enter your name")
        self.u_id = input("Enter your id")
    
    def show(self):
        print(self.name)
        print(self.u_id)
    
obj = Jafri()
obj.getData()
obj.show()