try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from Components import window, canvas, frame, button, center
from HomePage import Page

class AboutPage(Page):
    def __init__(self, *args):
        Page.__init__(self)

        C = Canvas(self.window)
        background = PhotoImage(file="./Resources/Images/pAbout.gif")
        background_label = Label(self.window, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = background

        F = frame(self.window)


        #creates enter rle button
        backimage = tk.PhotoImage(file="./Resources/Images/bBack.gif")
        
        #resizes background image
        backimagee = backimage.subsample(5, 5)
        Button = tk.Button(F, relief=FLAT, image=backimagee, command =self.BackToMenu,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        Button.place(relx=0.3, rely=0.93, anchor=CENTER)
        Button.image = backimagee
    
if __name__ == "__main__":
  test = AboutPage()
  test.window.mainloop()