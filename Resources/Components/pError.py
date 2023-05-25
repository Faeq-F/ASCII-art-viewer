from Components import canvas, frame, button, Page

class pErrorNoFile(Page):
  def __init__(self, *args):
    Page.__init__(self)
    C = canvas(self.window, "./Resources/Images/pErrorNoFile.gif")
    F = frame(self.window)
    B = button(F, "./Resources/Images/bBack.gif", 4, self.window.destroy, 0.1, 0.89)

class pErrorLines(Page):
  def __init__(self, *args):
    Page.__init__(self)
    C = canvas(self.window, "./Resources/Images/pErrorLines.gif")
    F = frame(self.window)
    B = button(F, "./Resources/Images/bBack.gif", 4, self.window.destroy, 0.1, 0.89)

if __name__ == "__main__":
  test = pErrorNoFile()
  test.window.mainloop()