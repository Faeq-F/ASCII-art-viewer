from Components import canvas, frame, button, entryField, divider, Page
import os

"""
  The Convert to Ascii Page (3rd menu option)
"""
class pConvertToAscii(Page):
  def __init__(self, *args):
    Page.__init__(self)
    self.Filename = ""
    canvas(self.window, "./Resources/Images/pConvertToAscii.gif")
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
  @Filename.setter
  def browse(self, *args):
    try:
        from tkinter import filedialog
    except:
        from Tkinter import tkFileDialog as filedialog
    self.__filename =  filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
    self.displayArt()

  """
    Method to display the user's art
  """
  def displayArt(self, *args):
    self.window.destroy()
    if self.Filename == "":
      self.Filename = self.E.get()

    if not (self.Filename.lower().endswith(('.txt'))):
      self.Filename = self.Filename +'.txt'
    
    if os.path.exists("./Resources/Data/" + self.Filename) == True:
      self.Filename = "./Resources/Data/" + self.Filename

    elif os.path.exists(self.Filename) == True:
      open("./Resources/Data/NewDecodedArt.txt","w").close() #Erase the file
      WriteToFile = open("./Resources/Data/NewDecodedArt.txt","a")
      with open(self.Filename) as EncodedFile:
        for line in EncodedFile:
          line = line.replace("\n","")
          #decoding
          pairs = [(int(line[i:i+2]),line[i+2]) for i in range(0,len(line),3)]
          decodedString = (''.join(n * c for n, c in pairs)) + "\n"
          WriteToFile.write(decodedString)
      WriteToFile.close

      ReadFile = open("./Resources/Data/NewDecodedArt.txt",'r')
      rdrata = ReadFile.read()
      ReadFile.close()
      print(rdrata)
      from pArt import pArt
      Page = pArt(rdrata)
      ReadFile.close()
      Page.window.mainloop()
    else:
      from pError import pErrorNoFile
      Page = pErrorNoFile()
      Page.window.mainloop()
      self.__init__(self)
      return

if __name__ == "__main__":
  test = pConvertToAscii()
  test.window.mainloop()