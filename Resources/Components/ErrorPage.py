 # error for there not being a file saved which is entered


    def errorNoFile():

        error = tk.Tk()

        # title for window
        error.title("ASCII art program by Faeq Faisal")

        # icon for window
        try:
            error.iconbitmap('Icon_for_windows.ico')
        except:
            time.sleep(0)

#       -----------------------------------------------------

            # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                error.destroy()
            except:
                time.sleep(0)

            mainWindow = tk.Tk()
            mainWindow.title('background image')

            # pick a .gif image file you have in the working directory
            fname = "NoClosing.gif.gif"
            bg_image = tk.PhotoImage(file=fname)

            # get the width and height of the image
            w = bg_image.width()
            h = bg_image.height()

            # size the window so the image will fill it
            mainWindow.geometry('724x592')

            # creates a canvas to show bg image
            cv = tk.Canvas(width=w, height=h)
            cv.pack(side='top', fill='both', expand='yes')

            cv.create_image(0, 0, image=bg_image, anchor='nw')
            # add canvas text at coordinates x=15, y=20

            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="", fill="red", anchor='nw')

            # window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

            # can't resize window
            mainWindow.resizable(width=False, height=False)

            # creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            # puts the window in front of the menu
            mainWindow.attributes('-topmost', True)

            # creates background
            mainWindow["bg"] = "#FFFFFF"

            # does not allow window to be moved
            mainWindow.overrideredirect(True)

            # does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

            # back to prev. window

            def noclose():

                # close window
                mainWindow.destroy()

                # back to prev. window
                errorNoFile()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # shows button
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs window
            center(mainWindow)
            mainWindow.mainloop()

#       -----------------------------------------------------

        # overides the close button
        error.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of all others
        error.attributes('-topmost', True)

        # creates a frame to show bg image
        F1 = Frame(error)
        F1 = Frame(error, width=400, height=450)
        F1.place(height=7000, width=4000, x=100, y=100)

        # displays frame (transparent)
        F1.grid(columnspan=10, rowspan=10)

        # configured to fit on window
        F1.grid_rowconfigure(0, weight=1)
        F1.grid_columnconfigure(0, weight=1)

        # file for bg
        photo = PhotoImage(file="errorNoFile.gif")
        label = Label(error, image=photo)

        label.image = photo  # keep a reference
        label.grid(row=0, column=0, columnspan=20, rowspan=20)

#     -----------------------------------------------------

        # returns the user to the menu
        def exit_the_error():

            # takes away the error window
            error.destroy()

            # shows the previous window again
            Convert_Rle()

#     -----------------------------------------------------
         # creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        # resizes background image
        backimagee = backimage.subsample(4, 4)
        Button = tk.Button(error, relief='flat', image=backimagee,
                           command=exit_the_error, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # showing button
        Button.grid(row=17, column=1)
        Button.image = backimagee

        # size of window
        error.geometry("724x592")

        # cant resize window
        error.resizable(width=False, height=False)

        # centers window
        center(error)

# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    # error for there not being a file saved which is entered

    def errorNoFileForConverter():

        error = tk.Tk()

        # title for window
        error.title("ASCII art program by Faeq Faisal")

        # icon for window
        try:
            error.iconbitmap('Icon_for_windows.ico')
        except:
            time.sleep(0)

#     -----------------------------------------------------

            # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                error.destroy()
            except:
                time.sleep(0)

            mainWindow = tk.Tk()
            mainWindow.title('background image')

            # pick a .gif image file you have in the working directory
            fname = "NoClosing.gif.gif"
            bg_image = tk.PhotoImage(file=fname)

            # get the width and height of the image
            w = bg_image.width()
            h = bg_image.height()

            # size the window so the image will fill it
            mainWindow.geometry('724x592')
            cv = tk.Canvas(width=w, height=h)

            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

            # add canvas text at coordinates x=15, y=20
            # anchor='nw' implies upper left corner coordinates

            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            # now add some button widgets

            # window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                # can't resize window
            mainWindow.resizable(width=False, height=False)
            # creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            # puts the window in front of the menu
            mainWindow.attributes('-topmost', True)

            # creates background
            mainWindow["bg"] = "#FFFFFF"

            # does not allow window to be moved
            mainWindow.overrideredirect(True)

            # does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

            # back to prev. window

            def noclose():

                # close window
                mainWindow.destroy()

                # back to prev. window
                errorNoFileForConverter()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # showing button
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            center(mainWindow)
            mainWindow.mainloop()

#     -----------------------------------------------------

        # overides the close button
        error.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of all others
        error.attributes('-topmost', True)

       # frame to show bg
        F1 = Frame(error)
        F1 = Frame(error, width=400, height=450)
        F1.place(height=7000, width=4000, x=100, y=100)

        # placing frame on window
        F1.grid(columnspan=10, rowspan=10)

        # configuring to be on top of image
        F1.grid_rowconfigure(0, weight=1)
        F1.grid_columnconfigure(0, weight=1)

        # file for bg
        photo = PhotoImage(file="errorNoFile.gif")
        label = Label(error, image=photo)

        label.image = photo  # keep a reference
        label.grid(row=0, column=0, columnspan=20, rowspan=20)


#     -----------------------------------------------------

        # returns the user to the menu


        def exit_the_error():

            # takes away the error window
            error.destroy()

            # shows the previous window again
            Convert_ASCII()

#     -----------------------------------------------------

        # creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        # resizes background image
        backimagee = backimage.subsample(4, 4)
        Button = tk.Button(error, relief='flat', image=backimagee,
                           command=exit_the_error, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # showing button
        Button.grid(row=17, column=1)
        Button.image = backimagee

        # size of window
        error.geometry("724x592")

        # cant resize window
        error.resizable(width=False, height=False)

        # centers window
        center(error)

# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    # error for there not being a file saved which is entered

    def errorNoFileForDisplayer():

        error = tk.Tk()

        # title for window
        error.title("ASCII art program by Faeq Faisal")

        # icon for window
        try:
            error.iconbitmap('Icon_for_windows.ico')

        except:
            time.sleep(0)

#       -----------------------------------------------------

            # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                error.destroy()
            except:
                time.sleep(0)

            mainWindow = tk.Tk()
            mainWindow.title('background image')

            # pick a .gif image file you have in the working directory
            fname = "NoClosing.gif.gif"

            bg_image = tk.PhotoImage(file=fname)
            # get the width and height of the image

            w = bg_image.width()
            h = bg_image.height()

            # size the window so the image will fill it
            mainWindow.geometry('724x592')
            cv = tk.Canvas(width=w, height=h)

            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

            # add canvas text at coordinates x=15, y=20
            # anchor='nw' implies upper left corner coordinates

            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            # now add some button widgets

            # window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                # can't resize window
            mainWindow.resizable(width=False, height=False)

            # puts the window in front of the menu
            mainWindow.attributes('-topmost', True)

            # creates background
            mainWindow["bg"] = "#FFFFFF"

            # does not allow window to be moved
            mainWindow.overrideredirect(True)

            # does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

            # back to prev. window

            def noclose():

                # close window
                mainWindow.destroy()

                # back to prev. window
                errorNoFileForDisplayer()

                # creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # places button on window
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs window
            center(mainWindow)
            mainWindow.mainloop()
#       -----------------------------------------------------

        # overide close button
        error.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of all others
        error.attributes('-topmost', True)

       # frame for window
        F1 = Frame(error)
        F1 = Frame(error, width=400, height=450)

        # places frame on window
        F1.place(height=7000, width=4000, x=100, y=100)
        F1.grid(columnspan=10, rowspan=10)

        # reconfiguring frame for window size
        F1.grid_rowconfigure(0, weight=1)
        F1.grid_columnconfigure(0, weight=1)

        # image for bg
        photo = PhotoImage(file="errorNoFile.gif")
        label = Label(error, image=photo)

        label.image = photo  # keep a reference
        label.grid(row=0, column=0, columnspan=20, rowspan=20)


#       -----------------------------------------------------

        # returns the user to the menu


        def exit_the_error():

            # takes away the error window
            error.destroy()

            # shows the previous window again
            ASCII_ART_DISPLAYER()

#       -----------------------------------------------------

        # creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        # resizes background image
        backimagee = backimage.subsample(4, 4)
        Button = tk.Button(error, relief='flat', image=backimagee,
                           command=exit_the_error, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # place image button
        Button.grid(row=17, column=1)
        Button.image = backimagee

        # size of window
        error.geometry("724x592")

        # cant resize window
        error.resizable(width=False, height=False)

        # centers window
        center(error)