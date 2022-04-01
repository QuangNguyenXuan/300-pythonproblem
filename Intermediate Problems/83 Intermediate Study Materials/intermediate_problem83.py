from tkinter import * 
root = Tk()
root.title("Inserting Image....")
root.geometry("300x300")

img = PhotoImage(file="pic.png")
btn = Button(root, image=img)
btn.pack()
root.mainloop()