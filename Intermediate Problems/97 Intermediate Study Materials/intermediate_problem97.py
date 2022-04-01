class Five:
    def getn(self):
        self.n = int(input("Enter a number"))
    
    def show_result(self):
        if self.n%5 == 0:
            print(str(self.n)+" is divisible by 5")
        else:
            print("Not divisible by 5")

obj = Five()
obj.getn()
obj.show_result()