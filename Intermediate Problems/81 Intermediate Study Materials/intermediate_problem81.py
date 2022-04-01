from tkinter import * 
root = Tk()
root.title("Button clicking...")
root.geometry("300x300")
def myfunc():
    print("Button is clicked.....")

btn = Button(root, text="Click me", command=myfunc)
btn.pack()
root.mainloop()