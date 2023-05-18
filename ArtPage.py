# function to display the art
            def display():

                 # opens text in window
                 ASCIIartONwindowThatIsDecompressed = Tk()

                  # title for window
                  ASCIIartONwindowThatIsDecompressed.title(
                       "ASCII art program by Faeq Faisal")

                   # icon for window
                   try:
                        ASCIIartONwindowThatIsDecompressed.iconbitmap(
                            'Icon_for_windows.ico')

                    except:
                        time.sleep(0)

            #       -----------------------------------------------------

                    # function to not allow program to end before any processes are complete

                    def on_closing():

                        # close window
                        try:
                            ASCIIartONwindowThatIsDecompressed.destroy()
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

                        # puts image on window
                        cv.pack(side='top', fill='both', expand='yes')
                        cv.create_image(0, 0, image=bg_image, anchor='nw')

                        # configuring the image to be in the north west corner
                        cv.create_text(15, 20, text="",
                                       fill="red", anchor='nw')

                        # window's icon
                        try:
                            mainWindow.iconbitmap('Icon_for_windows.ico')

                        except:
                            time.sleep(0)

                        # user can't resize window
                        mainWindow.resizable(width=False, height=False)

                        # image for button
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
                            menu()

                        # resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee,
                                           command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                        # placing the button on the window
                        Button.pack(side='left', padx=3, pady=0, anchor='s')
                        Button.image = backimagee

                        # runing the window
                        center(mainWindow)
                        mainWindow.mainloop()

            #       -----------------------------------------------------

                    # overides close button
                    ASCIIartONwindowThatIsDecompressed.protocol(
                        "WM_DELETE_WINDOW", on_closing)

                    # puts the window in front of the menu
                    ASCIIartONwindowThatIsDecompressed.attributes(
                        '-topmost', True)

                    # background colour
                    ASCIIartONwindowThatIsDecompressed["bg"] = "SteelBlue1"

                    # frame to show bg image
                    F1 = Frame(ASCIIartONwindowThatIsDecompressed)
                    F1 = Frame(ASCIIartONwindowThatIsDecompressed,
                               width=400, height=450)
                    F1.place(height=7000, width=4000, x=100, y=100)

                    # places frame on the window
                    F1.grid(columnspan=10, rowspan=10)

                    # configures for window
                    F1.grid_rowconfigure(0, weight=1)
                    F1.grid_columnconfigure(0, weight=1)

                    # image for bg
                    photo = PhotoImage(file="HIYA.gif")
                    label = Label(
                        ASCIIartONwindowThatIsDecompressed, image=photo)

                    label.image = photo  # keep a reference
                    label.grid(row=0, column=0, columnspan=20, rowspan=20)

                    # opens file
                    ReadFile = open("NewDeCompressedData.txt", 'r')

                    # reads file
                    data = ReadFile.read()

                    # closes file
                    ReadFile.close()

                    # message widget to show art
                    artishere = tk.Message(ASCIIartONwindowThatIsDecompressed, text=data, font=(
                        'Consolas', 13), fg='SteelBlue1', bg='#FFFFFF', width=90000)
                    artishere.grid(row=8, column=8)

                    # function to go back to menu
                    def backtomenu():

                        # closes window
                        ASCIIartONwindowThatIsDecompressed.destroy()

                        # runs the menu
                        menu()

                    # creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    # resizes background image
                    backimagee = backimage.subsample(3, 3)
                    Button = tk.Button(ASCIIartONwindowThatIsDecompressed, relief='flat', image=backimagee,
                                       command=backtomenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                    # places button on window
                    Button.grid(row=10, column=8)
                    Button.image = backimagee

            #       -----------------------------------------------------

                    # window size
                    ASCIIartONwindowThatIsDecompressed.geometry("724x592")

                    # centers window
                    center(ASCIIartONwindowThatIsDecompressed)
