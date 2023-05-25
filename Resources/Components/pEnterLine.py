from Components import canvas, frame, button, entryField, divider, Page

"""
  The EnterLine Page (for EnterRLE option)
"""
class pEnterLine(Page):
  def __init__(self, *args):
    Page.__init__(self)
    self.Line = ""
    canvas(self.window, "./Resources/Images/pRLEline.gif")
    F = frame(self.window)
    self.E = entryField(F, 0.24, 0.62)
    button(F, "./Resources/Images/bContinue.gif", 3, self.next, 0.23, 0.71)
  
  def next(self, *args):
    if self.Line == "":
      self.Line = self.E.get()

    #decoding
    pairs = [(int(self.Line[i:i+2]),self.Line[i+2]) for i in range(0,len(self.Line),3)]
    decodedString = (''.join(n * c for n, c in pairs)) + "\n"

    WriteToFile = open("./Resources/Data/NewDeCompressedData.txt","a") #appending to the end of the file
    WriteToFile.write(decodedString)
    WriteToFile.close()

    self.window.destroy()

if __name__ == "__main__":
  test = pEnterLine()
  test.window.mainloop()