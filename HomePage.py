try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from Components import window, canvas, frame, button


class ExitProgram(window):
    def __init__(self, *args):
        window.__init__(self, "200x100")
        self.window.title('Bye!')

        C = canvas(self.window, "./Resources/Images/pGoodbye.gif")
        F = frame(self.window)
        B = button(F, "./Resources/Images/bGoodbye.gif",
                   8, self.window.destroy, 'left', 300, 30, 'nw')

    def close(self, *args):
        self.window.destroy()


"""
class HomePage(window):
    def __init__(self, *args):
        window.__init__(self)

        C = Canvas(self.window)
        backg = PhotoImage(file="./Resources/Images/pHome.gif")
        background_label = Label(self.window, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = backg


    def close(self, *args):
        self.window.destroy()
        ClosingWindow = ExitProgram()
        ClosingWindow.window.mainloop()

        def exit_program():

                backimage = tk.PhotoImage(file="goodBYE.gif")
                backimagee = backimage.subsample(8, 8)
                Button = tk.Button(cv, relief='flat', image=backimagee,
                                   command=mainWindow.destroy, bg="#FFFFFF", fg='#FFFFFF', cursor="target")
                Button.pack(side='left', padx=30, pady=5, anchor='sw')
                Button.image = backimagee

                mainWindow.iconbitmap('Icon_for_windows.ico')
                mainWindow.resizable(width=False, height=False)
                center(mainWindow)
                mainWindow.mainloop()

            def Load_RLE_window():
                window_for_menu.destroy()
                Load_RLE_Window()

            def Load_About_window():
                window_for_menu.destroy()
                About()

            def ASCII_ART_DISPLAYER_window():
                window_for_menu.destroy()
                ASCII_ART_DISPLAYER()

            def Convert_ASCII_window():
                window_for_menu.destroy()
                Convert_ASCII()

            def Convert_rle_window():
                window_for_menu.destroy()
                Convert_Rle()

            labelspace = tk.Label(PutImageForBackground, text="", background='white', font=(
                "calibri", 12), justify=LEFT)
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground, text="", background='white', font=(
                "calibri", 12), justify=LEFT)
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground, text="", background='white', font=(
                "calibri", 12), cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")

            button_flag = True

            frame1 = tk.Frame(PutImageForBackground, bg='#FFFFFF', padx=109)
            frame1.grid(sticky=tk.W)

            imagetobeused = tk.PhotoImage(file="1.gif")
            imagetobeusede = imagetobeused.subsample(3, 3)
            Button = tk.Button(frame1, relief=FLAT, image=imagetobeusede,
                               command=Load_RLE_window, bg="#FFFFFF", fg='#FFFFFF', cursor="target")
            Button.grid()
            Button.image = imagetobeusede

            Displayimage = tk.PhotoImage(file="2.gif")
            Displayimagee = Displayimage.subsample(3, 3)
            ButtonToDisplayArt = tk.Button(frame1, command=ASCII_ART_DISPLAYER_window,
                                           image=Displayimagee, bg="#FFFFFF", fg='#FFFFFF', relief=FLAT, cursor="target")
            ButtonToDisplayArt.grid()
            ButtonToDisplayArt.image = Displayimagee

            ConvertAimage = tk.PhotoImage(file="3.gif")
            ConvertAimagee = ConvertAimage.subsample(3, 3)
            ButtonToConvertArt = tk.Button(frame1, image=ConvertAimagee, bg="#FFFFFF",
                                           fg='#FFFFFF', relief=FLAT, cursor="target", command=Convert_ASCII_window)
            ButtonToConvertArt.grid(sticky="w")
            ButtonToConvertArt.image = ConvertAimagee

            ConvertRimage = tk.PhotoImage(file="4.gif")
            ConvertRimagee = ConvertRimage.subsample(3, 3)
            ButtonToConvertRLE = tk.Button(frame1, image=ConvertRimagee, bg="#FFFFFF",
                                           fg='#FFFFFF', relief=FLAT, cursor="target", command=Convert_rle_window)
            ButtonToConvertRLE.grid(sticky="w")
            ButtonToConvertRLE.image = ConvertRimagee

            Quitimage = tk.PhotoImage(file="5.gif")
            Quitimagee = Quitimage.subsample(3, 3)
            QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF",
                                   fg='#FFFFFF', relief=FLAT, cursor="target", command=exit_program)
            QuitButton.grid(sticky="w")
            QuitButton.image = Quitimagee

            AQAimage = tk.PhotoImage(file="AQA.gif")
            AQAimagee = AQAimage.subsample(2, 2)
            Name = tk.Button(PutImageForBackground, image=AQAimagee, command=Load_About_window, text="Program By Faeq Faisal ",
                             bg='#81D3E0', fg="#FFFFFF", font=("Segoe UI Emoji", 10), relief=FLAT, cursor="trek")
            Name.grid(sticky="e")
            Name.image = AQAimagee

            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")

            image = tk.PhotoImage(file="r.gif")
            read = tk.Label(PutImageForBackground,
                            image=image, background='white')
            read.grid(sticky="w")
            read.image = image

            labelspace = tk.Label(PutImageForBackground, text="   ", background='#FFFFFF',
                                  fg='SteelBlue1', font=("Calibri", 9), cursor="arrow")
            labelspace.grid(sticky='w')
            labelspace = tk.Label(PutImageForBackground,
                                  text="", background='white', cursor="trek")
            labelspace.grid(sticky="w")
            labelspace = tk.Label(PutImageForBackground, text=".                                                                                                                                                                                                                                              .", background='white', cursor="trek")
            labelspace.grid(sticky="w")
"""

if __name__ == '__main__':
    test = ExitProgram()
    test.window.mainloop()
