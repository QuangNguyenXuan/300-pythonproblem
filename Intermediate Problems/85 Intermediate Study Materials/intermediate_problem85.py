from tkinter import * 
win = Tk()
win.title("Image as backgorund.,,")
# win.geometry("300x300")
img = PhotoImage(file="pic.png")
l = Label(win, image=img)
l.pack()
win.mainloop()

