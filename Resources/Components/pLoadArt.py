from Components import canvas, frame, button, entryField, divider, Page
import os

"""
  The LoadArt Page (2nd menu option)
"""
class pLoadArt(Page):
  def __init__(self, *args):
    Page.__init__(self)
    self.Filename = ""
    canvas(self.window, "./Resources/Images/pLoadArt.gif")
    F = frame(self.window)
    self.E = entryField(F, 0.21, 0.32)
    button(F, "./Resources/Images/bContinue.gif", 3, self.displayArt, 0.2, 0.41)
    divider(F, 0.2, 0.48)
    button(F, "./Resources/Images/bBrowseFile.gif", 2, self.browse, 0.2, 0.65)
    divider(F, 0.2, 0.77)
    button(F, "./Resources/Images/bBack.gif", 5, self.BackToMenu, 0.2, 0.89)

  """
  Method to allow the user to browse for their art
  """
  def browse(self, *args):
    try:
        from tkinter import filedialog
    except:
        from Tkinter import tkFileDialog as filedialog
    self.Filename =  filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
    self.displayArt()

  """
    Method to display the user's art
  """
  def displayArt(self, *args):
    
    if self.Filename == "":
      self.Filename = self.E.get()

    if not (self.Filename.lower().endswith(('.txt'))):
      self.Filename = self.Filename +'.txt'
    
    if os.path.exists("./Resources/Data/" + self.Filename) == True:
      self.Filename = "./Resources/Data/" + self.Filename

    elif not (os.path.exists(self.Filename) == True):
      from pError import pErrorNoFile
      self.window.destroy()
      Page = pErrorNoFile()
      Page.window.mainloop()
      self.__init__(self)
      return

    ReadFile = open(self.Filename,'r')
    data = ReadFile.read()
    ReadFile.close()

    from pArt import pArt
    self.window.destroy()
    Page = pArt(data)
    Page.window.mainloop()

if __name__ == "__main__":
  test = pLoadArt()
  test.window.mainloop()