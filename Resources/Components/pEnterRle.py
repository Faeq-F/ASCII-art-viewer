from Components import canvas, frame, button, integersOnlyEntryField, divider, Page

"""
  The EnterRLE Page (1st menu option)
"""
class pEnterRle(Page):
  def __init__(self, *args):
    Page.__init__(self)
    self.Lines = ""
    canvas(self.window, "./Resources/Images/pEnterRLE.gif")
    F = frame(self.window)
    self.E = integersOnlyEntryField(F, 0.24, 0.52)
    button(F, "./Resources/Images/bContinue.gif", 3, self.EnterLines, 0.23, 0.61)
    divider(F, 0.2, 0.75)
    button(F, "./Resources/Images/bBack.gif", 5, self.BackToMenu, 0.23, 0.89)

  """
    Method to move to the windows that allow the user to enter the data line by line
  """
  def EnterLines(self, *args):
    if self.Lines == "":
      self.Lines = self.E.get()

    self.window.destroy()

    if self.Lines == "" or int(self.Lines) < 3:
      from pError import pErrorLines
      Page = pErrorLines()
      Page.window.mainloop()
      self.__init__(self)
      return
    
    self.Lines = int(self.Lines)
    open('./Resources/Data/NewDeCompressedData.txt', 'w').close() #wipes the file

    from pEnterLine import pEnterLine
    for i in range(0, self.Lines):
      Line = pEnterLine()
      Line.window.mainloop()

    ReadFile = open("./Resources/Data/NewDeCompressedData.txt",'r')
    data = ReadFile.read()
    ReadFile.close()
    from pArt import pArt
    Page = pArt(data)
    Page.window.mainloop()

if __name__ == "__main__":
  test = pEnterRle()
  test.window.mainloop()