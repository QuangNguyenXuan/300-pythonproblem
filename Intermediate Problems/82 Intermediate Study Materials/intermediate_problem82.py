from tkinter import * 
root = Tk()
root.title("Quit Window....")
root.geometry("300x300")
def myfunc():
    root.quit()

btn = Button(root, text="Close this window", command=myfunc)
btn.pack()
root.mainloop()