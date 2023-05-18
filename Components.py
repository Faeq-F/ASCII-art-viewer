try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

"""
  centers all windows on-screen
  :param win: the window to center
"""


def center(Tk):
    Tk.update_idletasks()
    width = Tk.winfo_width()
    height = Tk.winfo_height()
    x = (Tk.winfo_screenwidth() // 2) - (width // 2)
    y = (Tk.winfo_screenheight() // 2) - (height // 2)
    Tk.geometry('{}x{}+{}+{}'.format(width, height, x, y))


"""
  Entry Field that only accepts integers
"""


class integersOnly(tk.Entry):

    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''  # empty string for characters other than integers to be replaced with
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    """
    Checks that the field only contains numbers
    """

    def check(self, *args):
        if self.get().isdigit():
            self.old_value = self.get()
        else:
            self.set(self.old_value)  # rejects change and reverts


"""
  Generic window for the program
  :param window: the window
"""


class window():
    def __init__(self, geometry, *args):
        # create window
        self.window = tk.Tk()
        self.window.title('ASCII Art Program by Faeq')
        self.window.geometry(geometry)
        self.window.resizable(width=False, height=False)
        self.window["bg"] = "#FFFFFF"
        self.window.attributes('-topmost', True)
        self.window.iconbitmap('./Resources/ASCII Art Viewer.ico')
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        center(self.window)

    def close(self, *args):
        self.window.destroy()
        ClosingWindow = noClose()
        ClosingWindow.window.mainloop()
        self.__init__(self, "775x592")


def canvas(window, image):
    C = Canvas(window)
    backg = PhotoImage(file=image)
    background_label = Label(window, image=backg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    C.img = backg
    return C


def frame(window):
    return tk.Frame(window, bg='#FFFFFF', padx=15,
                    borderwidth=0, relief='flat').pack(side='left', padx=3, pady=0, anchor='s')


def button(frame, image, subsample, command, side, padx, pady, anchor):
    backimage = tk.PhotoImage(
        file=image).subsample(subsample, subsample)
    Button = tk.Button(frame, relief='flat', image=backimage,
                       command=command, cursor="target")
    Button.pack(side=side, padx=padx, pady=pady, anchor=anchor)
    Button.image = backimage
    return Button


class noClose(window):
    def __init__(self, *args):
        window.__init__(self, "775x592")
        self.window.title('Please use the menu exit')
        C = canvas(self.window, "./Resources/Images/pNoClosing.gif")
        F = frame(self.window)
        B = button(F, "./Resources/Images/bBack.gif", 2,
                   self.window.destroy, 'left', 3, 0, 's')


if __name__ == '__main__':
    test = window("775x592")
    test.window.mainloop()
