import string
import random

size = int(input("Enter a length of password"))
result = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k = size))
print("You Strong Passowrd is "+str(result))