class Math:
    def getn(self):
        self.n = int(input("Enter a number"))
    
    def show_result(self):
        if self.n%2 == 0 and self.n%3 == 0:
            print(str(self.n)+" is divisible by 2 and 3")
        else:
            print("Not divisible by 2 and 3")

obj = Math()
obj.getn()
obj.show_result()