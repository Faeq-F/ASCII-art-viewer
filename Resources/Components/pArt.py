try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk


from Components import canvas, frame, button, Page


"""
  Page that displays the user's art
"""
class pArt(Page):
  def __init__(self, data, *args):
    Page.__init__(self)
    canvas(self.window, "./Resources/Images/pArt.gif")
    F = frame(self.window)
    
    artishere = tk.Message(F, text=data, font=('Consolas',13), fg = 'SteelBlue1', bg = '#FFFFFF',width = 90000)
    artishere.place(relx=0.5, rely=0.5, anchor=CENTER)

    button(F, "./Resources/Images/bBack.gif", 5, self.BackToMenu, 0.52, 0.94)


if __name__ == "__main__":
  test = pArt("data")
  test.window.mainloop()