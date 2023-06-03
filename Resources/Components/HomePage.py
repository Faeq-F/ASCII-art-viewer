try:
  from tkinter import *
  import tkinter as tk
except ImportError:
  from Tkinter import *
  import Tkinter as tk


from Components import window, canvas, frame, button, center


"""
  The window displayed when the user exits the program from the HomePage
"""
class ExitProgram(window):
  def __init__(self, *args):
    window.__init__(self)
    self.window.title("Bye!")
    self.window.geometry("200x100")
    center(self.window) # Recenter as geometry changed

    C = canvas(self.window, "./Resources/Images/pGoodbye.gif")
    F = frame(self.window)
    B = button(F, "./Resources/Images/bGoodbye.gif", 8, self.window.destroy, 0.2, 0.7)


"""
  The HomePage for the program
  ( Main menu for the program )
"""
class HomePage(window):
  def __init__(self, *args):
    window.__init__(self)

    C = canvas(self.window, "./Resources/Images/pHome.gif")
    F = frame(self.window)

    B = button(F, "./Resources/Images/bEnterRLE.gif", 3, self.EnterRle, 0.2, 0.59)
    B = button(F, "./Resources/Images/bDisplayArt.gif", 3, self.DisplayArt, 0.2, 0.65)
    B = button(F, "./Resources/Images/bConvertToAscii.gif", 3, self.ConvertToAscii, 0.2, 0.705)
    B = button(F, "./Resources/Images/bConvertToRle.gif", 3, self.ConvertToRle, 0.2, 0.76)
    B = button(F, "./Resources/Images/bExit.gif", 3, self.close, 0.2, 0.82)
    
    AuthorImage = tk.PhotoImage(file="./Resources/Images/Author.gif").subsample(2, 2)
    AuthorButton = tk.Button(F, image=AuthorImage, command=self.About,
        text="Program By Faeq Faisal ", bg='#80d8df', fg="#FFFFFF",
        font=("Segoe UI Emoji", 10), relief=FLAT, cursor="trek")
    AuthorButton.place(relx=0.91, rely=0.98, anchor=CENTER)
    AuthorButton.image = AuthorImage

    CheckReadMeNoteImage = tk.PhotoImage(file="./Resources/Images/CheckReadMeNote.gif")
    CheckReadMeNote = tk.Label(F,image=CheckReadMeNoteImage, background='white')
    CheckReadMeNote.place(relx=0.28, rely=0.99, anchor=CENTER)
    CheckReadMeNote.image = CheckReadMeNoteImage

  """
    Method to move to the EnterRlePage
  """
  def EnterRle(self, *args):
    from pEnterRle import pEnterRle
    self.window.destroy()
    Page = pEnterRle()
    Page.window.mainloop()

  """
    Method to move to the LoadArtPage
  """
  def DisplayArt(self, *args):
    from pLoadArt import pLoadArt
    self.window.destroy()
    Page = pLoadArt()
    Page.window.mainloop()

  """
    Method to move to the ConvertToAsciiPage
  """
  def ConvertToAscii(self, *args):
    from pConvertToAscii import pConvertToAscii
    self.window.destroy()
    Page = pConvertToAscii()
    Page.window.mainloop()

  """
    Method to move to the ConvertToRlePage
  """
  def ConvertToRle(self, *args):
    from pConvertToRle import pConvertToRle
    self.window.destroy()
    Page = pConvertToRle()
    Page.window.mainloop()

  """
    Method to move to the AboutPage
  """
  def About(self, *args):
    from pAbout import pAbout
    self.window.destroy()
    Page = pAbout()
    Page.window.mainloop()

  """
    Method to move to the ExitProgram window
  """
  def close(self, *args):
    self.window.destroy()
    ClosingWindow = ExitProgram()
    ClosingWindow.window.mainloop()

if __name__ == "__main__":
  test = HomePage()
  test.window.mainloop()