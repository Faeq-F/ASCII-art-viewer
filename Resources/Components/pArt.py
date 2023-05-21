try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from Components import window, canvas, frame, button, center, Page

class pArt(Page):
    def __init__(self, *args):
        Page.__init__(self)

        C = Canvas(self.window)
        background = PhotoImage(file="./Resources/Images/pArt.gif")
        background_label = Label(self.window, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = background

        F = frame(self.window)
        

        # creates enter rle button
        backimage = PhotoImage(file=self.ImageDir+"\\bBack.gif")

        # resizes background image
        backimagee = backimage.subsample(3, 3)
        Button = tk.Button(F, relief='flat', image=backimagee,command=self.BackToMenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on window
        Button.place(relx=0.5, rely=0.9, anchor=CENTER)
        Button.image = backimagee

    

if __name__ == "__main__":
    test = pArt()
    test.window.mainloop()