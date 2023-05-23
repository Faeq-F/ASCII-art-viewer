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
    self.E = entryField(F, 0.24, 0.42)
    button(F, "./Resources/Images/bContinue.gif", 3, self.displayArt, 0.23, 0.51)
    divider(F, 0.2, 0.59)
    button(F, "./Resources/Images/bBrowseFile.gif", 2, self.browse, 0.23, 0.69)
    divider(F, 0.2, 0.79)
    button(F, "./Resources/Images/bBack.gif", 5, self.BackToMenu, 0.23, 0.89)

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
    
    if os.path.exists("./Resources/Data/"+self.Filename) == True:
      ReadFile = open("./Resources/Data/"+self.Filename,'r')
      data = ReadFile.read()
      ReadFile.close()

      from pArt import pArt
      self.window.destroy()
      Page = pArt(data)
      Page.window.mainloop()
    elif os.path.exists(self.Filename) == True:
      ReadFile = open(self.Filename,'r')
      data = ReadFile.read()
      ReadFile.close()

      from pArt import pArt
      self.window.destroy()
      Page = pArt(data)
      Page.window.mainloop()
    else:
      from pError import pErrorNoFile
      self.window.destroy()
      Page = pErrorNoFile()
      Page.window.mainloop()
      self.__init__(self)

if __name__ == "__main__":
  test = pLoadArt()
  test.window.mainloop()