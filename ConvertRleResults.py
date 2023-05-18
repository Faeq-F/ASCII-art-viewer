
#       -----------------------------------------------------

# function to show the results of the compression
def show_results():

     # creates the window
     result = tk.Tk()

      # title for window
      result.title("ASCII art program by Faeq Faisal")

       # icon for window
       try:
            result.iconbitmap('Icon_for_windows.ico')

        except:
            time.sleep(0)

    #       -----------------------------------------------------
            # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                result.destroy()
            except:
                time.sleep(0)

            # creates a window
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

            # canvas to use bg image
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="",
                           fill="red", anchor='nw')

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
                show_results()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # places the button on the window
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs the window
            center(mainWindow)
            mainWindow.mainloop()

    #       -----------------------------------------------------

        # overides close button
        result.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of the others
        result.attributes('-topmost', True)

        # background for window
        result["bg"] = "SteelBlue1"

        # frame for bg image
        F1 = Frame(result)
        F1 = Frame(result, width=400, height=450)

        # places the frame on the window
        F1.place(height=7000, width=4000, x=100, y=100)
        F1.config()

        # configures size of frame
        F1.grid(columnspan=10, rowspan=10)
        F1.grid_rowconfigure(0, weight=1)
        F1.grid_columnconfigure(0, weight=1)

        # bg image
        photo = PhotoImage(file="Results.gif")
        label = Label(result, image=photo)

        label.image = photo  # keep a reference
        label.grid(row=0, column=0, columnspan=20, rowspan=20)

        # concatenates the strings together
        text_to_show = str(characters_in_original)

        # number of characters in the old file
        ResulT = Label(result, text=text_to_show, bg="#FFFFFF", font=(
            "Consolas", 15), fg="SteelBlue1")
        ResulT.grid(sticky=tk.W, row=5, padx=150)

        # concatenates the strings together
        text_to_show = str(characters_in_new)

        # number of characters in the new file
        ResulT = Label(result, text=text_to_show, bg="#FFFFFF", font=(
            "Consolas", 20), fg="SteelBlue1")
        ResulT.grid(sticky=tk.W, row=8, padx=30)

        # concatenates the strings together
        text_to_show = str(difference)

        # shows difference in characters
        ResulT = Label(result, text=text_to_show, bg="#FFFFFF", font=(
            "Consolas", 20), fg="SteelBlue1")
        ResulT.grid(sticky=tk.W, row=15, padx=30)

    #       -----------------------------------------------------

        # ends this part of the program
        def end_this_part():

            # takes away the window
            result.destroy()

            # shows the menu again
            menu()

    #       -----------------------------------------------------

        # creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        # resizes background image
        backimagee = backimage.subsample(5, 5)
        Button = tk.Button(result, relief='flat', image=backimagee,
                           command=end_this_part, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on the window
        Button.grid(row=19)
        Button.image = backimagee

        # size of window
        result.geometry("775x592")

        # can't resize window
        result.resizable(width=False, height=False)

        # centers window
        center(result)
