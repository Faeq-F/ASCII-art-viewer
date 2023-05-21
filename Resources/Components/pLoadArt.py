try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from Components import window, canvas, frame, button, center, Page

class pLoadArt(Page):
    def __init__(self, *args):
        Page.__init__(self)

        C = Canvas(self.window)
        background = PhotoImage(file="./Resources/Images/pLoadArt.gif")
        background_label = Label(self.window, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = background

        F = frame(self.window)

        #text entry field
        imag = tk.PhotoImage(file="entry.gif")
        
        # create a frame and pack it
        frame2 = tk.Frame(display,bg='#FFFFFF',padx=15)
        frame2.grid()

        #sizing image
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')

        #reference
        s.grid(column = 2, row = 5)
        s.image = imagee

        #entry field
        e = tk.Entry(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
        e.grid(column = 2, row = 5)

        # create a frame and pack it
        frame1 = tk.Frame(display,bg='#FFFFFF',padx=15)
        frame1.grid(sticky=tk.W)

        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()
        
        #creates enter rle button
        image = tk.PhotoImage(file="C.gif")
        
        #resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =displayArt,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee
        

    #       -----------------------------------------------------
        
        #loads button
        #imports file dialog to allow the user to brows for their art
        try:
            from tkinter import filedialog
        except:
            from Tkinter import tkFileDialog

        #There were a couple of methods here that need to be implemented
        
        #creates enter button
        image = tk.PhotoImage(file="BfF.gif")
        
        #resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =browse,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")
        
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

#creates enter button
        image = tk.PhotoImage(file="Back.gif")
        
        #resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =exit_this_displayer,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee
        
        #size of window
        display.geometry("724x592")
        
        #cant resize window
        display.resizable(width=False, height=False)
        
        #centers window
        center(display)