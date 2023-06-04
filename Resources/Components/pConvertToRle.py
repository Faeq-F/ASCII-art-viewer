try:
  from tkinter import *
  import tkinter as tk
except ImportError:
  from Tkinter import *
  import Tkinter as tk

import os
from itertools import groupby

from Components import canvas, frame, button, Page, entryField, divider, noClose

class pConvertToRle(Page):
  def __init__(self, *args):
    Page.__init__(self)
    self.Filename = ""
    canvas(self.window, "./Resources/Images/pConvertToRLE.gif")
    F = frame(self.window)
    self.E = entryField(F, 0.24, 0.42)
    button(F, "./Resources/Images/bContinue.gif", 3, self.displayResults, 0.23, 0.51)
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
    self.displayResults()

  """
    Method to display the results of the compression
  """
  def displayResults(self, *args):
    self.window.destroy()
    
    if self.Filename == "":
      self.Filename = self.E.get()

    if not (self.Filename.lower().endswith(('.txt'))):
      self.Filename = self.Filename +'.txt'
    
    if os.path.exists("./Resources/Data/" + self.Filename) == True:
      self.Filename = "./Resources/Data/" + self.Filename

    elif not (os.path.exists(self.Filename) == True):
      from pError import pErrorNoFile
      Page = pErrorNoFile()
      Page.window.mainloop()
      self.__init__(self)
      return
    
    open("./Resources/Data/NewEncodedData.txt","w").close() #Erase the file

    WriteToFile = open("./Resources/Data/NewEncodedData.txt","a")
    with open(self.Filename) as FileToConvert:
      for line in FileToConvert:
        line = line.replace("\n","")
        #encoding
        partners = [(len(list(a)), b) for b, a in groupby(line)]
        endline = (''.join("%02d%s" % (c, d) for c, d in partners)) + '\n'
        WriteToFile.write(endline)
        WriteToFile.flush()
    WriteToFile.close

    #reading old file and calculating characters
    CharCount = open(self.Filename, 'r')
    OldCharacters = 0
    for line in CharCount:
      OldCharacters = OldCharacters + len(line)

    #reading new file and calculating characters
    NewCharacters = 0
    with open(self.ResDir + r"Data\NewEncodedData.txt") as myfile:
      for line in myfile:
        NewCharacters = NewCharacters + len(line)

    #difference
    dif = str(OldCharacters-NewCharacters)

    Page = pRes(OldCharacters, NewCharacters, dif)
    Page.window.mainloop()


"""
  Page that displays the user's results
"""
class pRes(Page):
  def __init__(self, old, new, dif, *args):
    self.old = old
    self.new = new
    self.dif = dif
    Page.__init__(self)
    canvas(self.window, "./Resources/Images/pResults.gif")
    F = frame(self.window)
    
    tk.Label(F, text= old, bg = '#FFFFFF', fg = 'SteelBlue1').place(relx=0.5, rely=0.3, anchor=CENTER)
    tk.Label(F, text= new, bg = '#FFFFFF', fg = 'SteelBlue1').place(relx=0.5, rely=0.6, anchor=CENTER)
    tk.Label(F, text= dif, bg = '#FFFFFF', fg = 'SteelBlue1').place(relx=0.5, rely=0.8, anchor=CENTER)
    button(F, "./Resources/Images/bBack.gif", 5, self.BackToMenu, 0.52, 0.94)

  """
    Method to move to the noClosingPage
  """
  def close(self, *args):
    self.window.destroy()
    ClosingWindow = noClose()
    ClosingWindow.window.mainloop()
    self.__init__(self, self.old, self.new, self.dif)


if __name__ == "__main__":
    test = pConvertToRle()
    test.window.mainloop()