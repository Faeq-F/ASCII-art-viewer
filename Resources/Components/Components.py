try:
  from tkinter import *
  import tkinter as tk
except ImportError:
  from Tkinter import *
  import Tkinter as tk


import pathlib, os


"""
  Generic window for the program
"""
class window:
  def __init__(self, *args):
    # create window
    self.window = tk.Tk()
    self.window.title("ASCII Art Program by Faeq")
    self.window.geometry("775x592")
    self.window.resizable(width=False, height=False)
    self.window["bg"] = "#FFFFFF"
    self.window.attributes("-topmost", True)
    self.window.iconbitmap("./Resources/ASCII Art Viewer.ico")
    self.window.protocol("WM_DELETE_WINDOW", self.close)
    center(self.window)

  """
    Method to move to the noClosingPage
  """
  def close(self, *args):
    self.window.destroy()
    ClosingWindow = noClose()
    ClosingWindow.window.mainloop()
    self.__init__(self)


"""
  Generic page for the program
"""
class Page(window):
  def __init__(self, *args):
    window.__init__(self)
    self.ResDir = str(pathlib.Path(__file__).parent.resolve()).replace("Components", "")

  """
    Method to move from the page, back to the menu
  """
  def BackToMenu(self, *args):
    from HomePage import HomePage
    self.window.destroy()
    Home = HomePage()
    Home.window.mainloop()


"""
  The window that appears when the user tries to exit the program outside of the HomePage window
"""
class noClose(window):
  def __init__(self, *args):
    window.__init__(self)
    self.window.title("Please use the menu exit")
    C = canvas(self.window, "./Resources/Images/pNoClosing.gif")
    F = frame(self.window)
    B = button(F, "./Resources/Images/bBack.gif", 3, self.window.destroy, 0.25, 0.8)


"""
  Canvas to display the background image for windows
  :param window: The window to place the canvas on
  :param image: The background image for the window
  :return: The canvas created
"""
def canvas(window, image):
  C = Canvas(window)
  backg = PhotoImage(file=image, master=window)
  background_label = Label(window, image=backg)
  background_label.place(x=0, y=0, relwidth=1, relheight=1)
  C.pack()
  C.img = backg
  return C


"""
  Frame to display additional components on windows with a canvas
  :param window: The window to place the frame on
  :return: The frame created
"""
def frame(window):
  return tk.Frame(window, bg="#FFFFFF", padx=18, borderwidth=0, relief="flat", highlightbackground="white", highlightthickness=2).pack(side=TOP)


"""
  Button for user interaction with the program
  :param frame: The frame to place the button on
  :param image: The image for the button
  :param subsample: The amount to subsample
  :param command: The command the button executes when clicked on
  :param x: The relx placement of the button
  :param y: The rely placement of the button
  :return: The button created
"""
def button(frame, image, subsample, command, x, y):
  Image = tk.PhotoImage(file=image).subsample(subsample, subsample)
  Button = tk.Button(frame, relief="flat", image=Image, command=command, cursor="target", bg="#FFFFFF", fg='#FFFFFF')
  Button.place(relx=x, rely=y, anchor=CENTER)
  Button.image = Image
  return Button

"""
  EntryField for typing in filenames, etc.
  :param frame: The frame to place the field on
  :param x: The relx placement of the field
  :param y: The rely placement of the field
  :return: The field created
"""
def entryField(frame, x, y):
  #entry field image
  image = tk.PhotoImage(file="./Resources/Images/EntryField.gif").subsample(3, 3)
  imageLabel = tk.Label(frame, borderwidth=1, image=image, bg = '#FFFFFF')
  imageLabel.place(relx=x, rely=y, anchor=CENTER)
  imageLabel.image = image

  #entry field widget
  entry = tk.Entry(frame,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
  entry.place(relx=x, rely=y, anchor=CENTER)
  return entry

"""
  Divider for widgets on a window
  :param frame: The frame to place the divider on
  :param x: the relx placement of the divider
  :param y: the rely placement of the divider
  :return: the divider created
"""
def divider(frame, x, y):
  divider = Label(frame, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
  divider.place(relx=x, rely=y, anchor=CENTER)
  return divider


"""
  Entry Field that only accepts integers
"""
class integersOnly(tk.Entry):
  def __init__(self, master=None, **kwargs):
    self.var = tk.StringVar()
    tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
    self.old_value = (
      "" # empty string for characters other than integers to be replaced with
    )
    self.var.trace("w", self.check)
    self.get, self.set = self.var.get, self.var.set

  """
  Checks that the field only contains numbers
  """
  def check(self, *args):
    if self.get().isdigit() or self.get()=="":
      self.old_value = self.get()
    else:
      self.set(self.old_value)  # rejects change and reverts


"""
  integersOnly EntryField
  :param frame: The frame to place the field on
  :param x: The relx placement of the field
  :param y: The rely placement of the field
  :return: The field created
"""
def integersOnlyEntryField(frame, x, y):
  #entry field image
  image = tk.PhotoImage(file="./Resources/Images/EntryField.gif").subsample(3, 3)
  imageLabel = tk.Label(frame, borderwidth=1, image=image, bg = '#FFFFFF')
  imageLabel.place(relx=x, rely=y, anchor=CENTER)
  imageLabel.image = image

  #entry field widget
  entry = integersOnly(frame,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
  entry.place(relx=x, rely=y, anchor=CENTER)
  return entry


"""
  centers all windows on-screen
  :param Tk: the window to center
"""
def center(Tk):
  Tk.update_idletasks()
  width = Tk.winfo_width()
  height = Tk.winfo_height()
  x = (Tk.winfo_screenwidth() // 2) - (width // 2)
  y = (Tk.winfo_screenheight() // 2) - (height // 2)
  Tk.geometry("{}x{}+{}+{}".format(width, height, x, y))


if __name__ == "__main__":
  print(str(pathlib.Path(__file__).parent.resolve()).replace("Components", ""))
  test = window("775x592")
  test.window.mainloop()