try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from Components import window, canvas, frame, button, center

import pathlib, os


class Page(window):
  def __init__(self, *args):
        window.__init__(self)
        self.ImageDir = str(pathlib.Path(__file__).parent.resolve())
        self.ImageDir = self.ImageDir.replace("Components", "Images")

  def BackToMenu(self, *args):
    self.window.destroy()
    Home = HomePage()
    Home.window.mainloop()
    

class ExitProgram():
    def __init__(self, *args):
        self.window = tk.Tk()
        self.window.title("Bye!")
        self.window.geometry("200x100")
        self.window.resizable(width=False, height=False)
        self.window["bg"] = "#FFFFFF"
        self.window.attributes("-topmost", True)
        self.window.iconbitmap("./Resources/ASCII Art Viewer.ico")
        

        C = canvas(self.window, "./Resources/Images/pGoodbye.gif")
        F = frame(self.window)
        backImage = tk.PhotoImage(file="./Resources/Images/bGoodbye.gif").subsample(8, 8)
        Button = tk.Button(F, relief="flat", image=backImage, command=self.window.destroy, cursor="target")
        Button.place(relx=0.2, rely=0.7, anchor=CENTER)
        Button.image = backImage
        
        center(self.window)


class HomePage(window):
    def __init__(self, *args):
        window.__init__(self)

        C = Canvas(self.window)
        background = PhotoImage(file="./Resources/Images/pHome.gif")
        background_label = Label(self.window, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = background

        F = frame(self.window)

        menuOption1 = tk.PhotoImage(file="./Resources/Images/bEnterRLE.gif").subsample(3, 3)
        Button = tk.Button(F, relief=FLAT, image=menuOption1, command=self.Load_RLE_window, bg="#FFFFFF", fg='#FFFFFF', cursor="target")
        Button.place(relx=0.2, rely=0.59, anchor=CENTER)
        Button.image = menuOption1

        menuOption2 = tk.PhotoImage(file="./Resources/Images/bDisplayArt.gif").subsample(3, 3)
        ButtonToDisplayArt = tk.Button(F, command=self.ASCII_ART_DISPLAY_window,image=menuOption2, bg="#FFFFFF", fg='#FFFFFF', relief=FLAT, cursor="target")
        ButtonToDisplayArt.place(relx=0.2, rely=0.65, anchor=CENTER)
        ButtonToDisplayArt.image = menuOption2

        ConvertAimage = tk.PhotoImage(file="./Resources/Images/bConvertA.gif")
        ConvertAimagee = ConvertAimage.subsample(3, 3)
        ButtonToConvertArt = tk.Button(F, image=ConvertAimagee, bg="#FFFFFF",
                                        fg='#FFFFFF', relief=FLAT, cursor="target", command=self.Convert_ASCII_window)
        ButtonToConvertArt.place(relx=0.2, rely=0.705, anchor=CENTER)
        ButtonToConvertArt.image = ConvertAimagee

        ConvertRimage = tk.PhotoImage(file="./Resources/Images/bConvertR.gif")
        ConvertRimagee = ConvertRimage.subsample(3, 3)
        ButtonToConvertRLE = tk.Button(F, image=ConvertRimagee, bg="#FFFFFF",
                                        fg='#FFFFFF', relief=FLAT, cursor="target", command=self.Convert_rle_window)
        ButtonToConvertRLE.place(relx=0.2, rely=0.76, anchor=CENTER)
        ButtonToConvertRLE.image = ConvertRimagee

        Quitimage = tk.PhotoImage(file="./Resources/Images/bExit.gif")
        Quitimagee = Quitimage.subsample(3, 3)
        QuitButton = tk.Button(F, image=Quitimagee, bg="#FFFFFF",
                                fg='#FFFFFF', relief=FLAT, cursor="target", command=self.close)
        QuitButton.place(relx=0.2, rely=0.82, anchor=CENTER)
        QuitButton.image = Quitimagee

        AQAimage = tk.PhotoImage(file="./Resources/Images/Author.gif")
        AQAimagee = AQAimage.subsample(2, 2)
        Name = tk.Button(F, image=AQAimagee, command=self.Load_About_window, text="Program By Faeq Faisal ",
                            bg='#81D3E0', fg="#FFFFFF", font=("Segoe UI Emoji", 10), relief=FLAT, cursor="trek")
        Name.place(relx=0.91, rely=0.98, anchor=CENTER)
        Name.image = AQAimagee

        image = tk.PhotoImage(file="./Resources/Images/CheckReadMeNote.gif")
        read = tk.Label(F,image=image, background='white')
        read.place(relx=0.28, rely=0.99, anchor=CENTER)
        read.image = image


    def close(self, *args):
        self.window.destroy()
        ClosingWindow = ExitProgram()
        ClosingWindow.window.mainloop()

    def Load_RLE_window(self, *args):
        self.window.destroy()
        #Load_RLE_Window()

    def Load_About_window(self, *args):
        from AboutPage import AboutPage
        self.window.destroy()
        aboutPage = AboutPage()
        aboutPage.window.mainloop()

    def ASCII_ART_DISPLAY_window(self, *args):
        
        self.window.destroy()
        

    def Convert_ASCII_window(self, *args):
        self.window.destroy()
        #Convert_ASCII()

    def Convert_rle_window(self, *args):
        from ConvertAsciiPage import ConvertAsciiPage
        self.window.destroy()
        asciiPage = ConvertAsciiPage()
        asciiPage.window.mainloop()

if __name__ == "__main__":
    test = HomePage()
    test.window.mainloop()
