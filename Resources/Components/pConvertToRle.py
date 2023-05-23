try:
  from tkinter import *
  import tkinter as tk
except ImportError:
  from Tkinter import *
  import Tkinter as tk

from Components import window, canvas, frame, button, center, Page

class pConvertToRle(Page):
    def __init__(self, *args):
        Page.__init__(self)

        C = Canvas(self.window)
        background = PhotoImage(file="./Resources/Images/pConvertToRLE.gif")
        background_label = Label(self.window, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = background

        F = frame(self.window)

        # text entry field
        imag = tk.PhotoImage(file="./Resources/Images/EntryField.gif")
        # sizing image to window size
        imagee = imag.subsample(3, 3)
        s = tk.Label(F, borderwidth=1, image=imagee, bg='#FFFFFF')
        s.place(relx=0.5, rely=0.5, anchor=CENTER)
        s.image = imagee

        # entry field
        entry = tk.Entry(F, width=20, bg='#FFFFFF', relief='flat', font=('Consolas', 18), fg='SteelBlue1')
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creates enter rle button
        backimage = PhotoImage(file=self.ImageDir+"\\bBack.gif")

        # resizes background image
        backimagee = backimage.subsample(3, 3)
        Button = tk.Button(F, relief='flat', image=backimagee,command=self.BackToMenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on window
        Button.place(relx=0.5, rely=0.9, anchor=CENTER)
        Button.image = backimagee

if __name__ == "__main__":
    test = pConvertToRle()
    test.window.mainloop()