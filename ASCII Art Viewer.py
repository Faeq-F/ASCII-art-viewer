try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from math import *
import ctypes
import os
import sys
import time

data_from_rle_inputter = ""
textfile = ""


# :return: void


"""
  Creates Home page
"""


def menu():
    window_for_menu = tk.Tk()

    def Load_RLE_Window():

        mainWindow = tk.Tk()

        C = Canvas(mainWindow)
        backg = PhotoImage(file="ERd.gif")
        background_label = Label(mainWindow, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()
        C.img = backg

        # second part of process (uer entering the rle encoded data)
        def parttwo():

            number = e.get()
            mainWindow.destroy()

            # the error to show when the user enters a number below 3
            def error():
                error_window = tk.Tk()
                error_window.title("ASCII art program by Faeq Faisal")
                error_window.iconbitmap('Icon_for_windows.ico')

                # function to not allow program to end before any processes are complete
                def on_closing():
                    error_window.destroy()

                    mainWindow = tk.Tk()

                    fname = "NoClosing.gif.gif"
                    bg_image = tk.PhotoImage(file=fname)
                    w = bg_image.width()
                    h = bg_image.height()
                    mainWindow.geometry('724x592')
                    cv = tk.Canvas(width=w, height=h)
                    cv.pack(side='top', fill='both', expand='yes')
                    cv.create_image(0, 0, image=bg_image, anchor='nw')
                    cv.create_text(15, 20, text="", fill="red", anchor='nw')

                    mainWindow.iconbitmap('Icon_for_windows.ico')
                    mainWindow.resizable(width=False, height=False)
                    mainWindow.attributes('-topmost', True)
                    mainWindow["bg"] = "#FFFFFF"
                    mainWindow.overrideredirect(True)
                    mainWindow.resizable(width=False, height=False)

                    def noclose():
                        mainWindow.destroy()
                        error()

                    backimage = tk.PhotoImage(file="Back.gif")
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee,
                                       command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")
                    Button.pack(side='left', padx=3, pady=0, anchor='s')
                    Button.image = backimagee

                    center(mainWindow)
                    mainWindow.mainloop()

            #           -----------------------------------------------------
                # overides the close button ( 'X' button) to run the function above
                error_window.protocol("WM_DELETE_WINDOW", on_closing)

                # puts the window in front of all other windows
                error_window.attributes('-topmost', True)

                # frame for the bg image
                F1 = Frame(error_window)
                F1 = Frame(error_window, width=400, height=450)

                # placing the frame on the window
                F1.place(height=7000, width=4000, x=100, y=100)
                F1.grid(columnspan=10, rowspan=10)

                # configuring the placement of the frame on the window
                F1.grid_rowconfigure(0, weight=1)
                F1.grid_columnconfigure(0, weight=1)

                # image for bg
                photo = PhotoImage(file="errorLines.gif")
                label = Label(error_window, image=photo)

                label.image = photo  # keep a reference
                label.grid(row=0, column=0, columnspan=20, rowspan=20)

            #       -----------------------------------------------------

                # exits the error message
                def exit_the_error():

                    # takes away the error window
                    error_window.destroy()

                    # shows the previous window again
                    Load_RLE_Window()

            #       -----------------------------------------------------
                # creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                # resizes background image
                backimagee = backimage.subsample(3, 3)
                Button = tk.Button(error_window, relief='flat', image=backimagee,
                                   command=exit_the_error, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                # placing the button on the window
                Button.grid(row=18, column=4)
                Button.image = backimagee

                # size of window
                error_window.geometry("724x592")

                # can't resize window
                error_window.resizable(width=False, height=False)

                # centers window on the screen
                center(error_window)

            # checks if anything is inputted on the entry field
            if number == '':

                # if not it runs the error defined above
                error()

            # checks if the number put in was 3 or above
            elif float(number) < 3:

                # if not, it runs the error
                error()

            # if all requirements are met, it allows the user to enter their data
            else:

                # creates a checking variable to check the nuber of line inputted by the user
                check = 0

                # makes he number a integer
                number = int(number)

                # wipes the file
                open('NewDeCompressedData.txt', 'w').close()
                # ------------------------------#

                # while loop to check the number of lines
                while number > check:

                    # creates trhe window
                    window = tk.Tk()

                    # size of window
                    window.geometry("750x592")

                    # centers the window
                    center(window)

                    # can't resize window
                    window.resizable(width=False, height=False)

                    # does not allow window to be moved
                    window.overrideredirect(True)

                    # canvas to show bg image
                    C = Canvas(window)
                    backg = PhotoImage(file="input.gif")

                    # places the bg image on the window
                    background_label = Label(window, image=backg)
                    background_label.place(x=0, y=0, relwidth=1, relheight=1)

                    # references the bg image
                    C.grid()
                    C.img = backg

                    # creates empty space between widgets
                    emptyspace = Label(window, text=" ", bg="#FFFFFF")
                    emptyspace.grid(sticky=tk.W)

                    # text entry field
                    imag = tk.PhotoImage(file="entry.gif")

                    # create a frame and pack it
                    frame2 = tk.Frame(window, bg='#FFFFFF', padx=15)
                    frame2.grid()

                    # makes the image smaller (by subsampling)
                    imagee = imag.subsample(3, 3)
                    s = tk.Label(frame2, borderwidth=1,
                                 image=imagee, bg='#FFFFFF')

                    # places the image behind the entry field
                    s.grid(column=2, row=20)
                    s.image = imagee

                    # creartes a entry field that only allows integers to be entered
                    # (uses a class that I defined above)

                    entry = Entry(frame2, width=20, bg='#FFFFFF', relief='flat', font=(
                        'Consolas', 18), fg='SteelBlue1')
                    entry.grid(column=2, row=20)

                    # function to exit each window
                    def exitt():

                        # save data
                        data_from_rle_inputter = entry.get()

                        # saves data to new variable (easier to read what is going on)
                        encoded_string = data_from_rle_inputter

                        # the string to be decoded
                        string = encoded_string

    #       -----------------------------------------------------

                        # function to split string into list

                        def split(str, num):
                            return [str[start:start+num] for start in range(0, len(str), num)]

    #       -----------------------------------------------------

                        # splitting string into packets of 3
                        splitUpStringwiththree = split(string, 3)

                        # creating a new list to write to later
                        new_string = []

                        # spliting the string again but this time in packets of 2
                        splitUpStringg = split(string, 2)

                        # loop to split the splitted string into a list with items of length 1
                        for item in splitUpStringwiththree:

                            # splitting into packets
                            r = split(item, 1)

                            # saving to our new list made up of strings
                            new_string = new_string+r

                        # another new list we will write to later
                        splitUpStringg = []

                        # loop to split the list into the reoccurences of the characters without the actual character
                        for i in splitUpStringwiththree:

                            # splitting into packets
                            rrt = split(i, 2)

                            # saving to our new list
                            splitUpStringg = splitUpStringg+rrt

                        # assigning our old list to a new variable so that we have a copy of the list to refer to when the original is already in use
                        v = new_string

                        # deleting the third character in every item
                        k = 3

                        # actually deleting the character
                        del new_string[k-1::k]

                        # joining the characters for the number of occurences together
                        mmm = [''.join(x) for x in zip(
                            new_string[0::2], new_string[1::2])]

    #       -----------------------------------------------------

                        # replacing the 0 in any integer representing the number of occurrences
                        for w in mmm:

                            if w[0] == '0':

                                w.replace('0', '')

    #       -----------------------------------------------------

                        # turning every item in the list into a integer
                        mmm = list(map(int, mmm))

                        # loop to get rid of unwanted items in the list for occurences
                        for i in splitUpStringg:

                            # checking if the length is equal to 2 (if so, this shows the number of occurences)
                            if len(i) == 2:

                                # finding the index of the item in its list
                                lop = splitUpStringg.index(i)

                                # getting rid of the item using its index previously found
                                splitUpStringg.pop(lop)

                        # loop to multiply the numbver to be shown by its actual bnumber of occurences
                        decodedString = [item for item, count in zip(
                            splitUpStringg, mmm) for i in range(count)]

                        # making the list into a string without annoying commas or square brackets that should not be there
                        makeitastring = ''.join(map(str, decodedString))

                        # makes sure that the next line entered is on a new line in the file
                        decoded_string_to_write = makeitastring + "\n"

                        # writes the data to the file

                        # name of new file
                        textfile = "NewDeCompressedData.txt"

                        # creates and writes to a new file
                        WriteToFile = open(textfile, "a")

                        # writes to the file and closes it
                        WriteToFile.write(decoded_string_to_write)
                        WriteToFile.close()

                        # closes the window
                        window.destroy()

                    # background colour
                    window["bg"] = "SteelBlue1"

                    # create a frame and pack it
                    frame1 = tk.Frame(window, bg='#FFFFFF', padx=15)
                    frame1.grid(sticky=tk.W)

                    # creates empty space between widgets
                    emptyspace = Label(
                        frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
                    emptyspace.grid()

                    # creates enter rle button
                    image = tk.PhotoImage(file="C.gif")

                    # resizes background image
                    imagee = image.subsample(3, 3)
                    ButtonToEnter = tk.Button(
                        frame1, relief=FLAT, image=imagee, command=exitt, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                    # places image button
                    ButtonToEnter.grid(sticky=tk.W)
                    ButtonToEnter.image = imagee

                    # creates empty space between widgets
                    emptyspace = Label(
                        frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
                    emptyspace.grid()

                    # runs the window
                    window.mainloop()

                    # during the window being shown, itr checks if it is still
                    # active to stop more windows from going over them
                    while True:

                        # try and except is used as the user can close the window at any time,
                        # and when they do, I want to not get a defining error
                        try:

                            # 'checks if the window is running
                            if 'normal' == window.state():

                                # if it is, the program does nothing
                                time.sleep(0)

                        # if the window is no longer running, the check variable is updated and the loop is broken
                        except:

                            # check is updated
                            check = check + 1
                            break

                # runs the function above
                display()

                # ------------------------------#

    # ------------------------------#

                # title for window
        mainWindow.title("ASCII art program by Faeq Faisal")

        # icon for window
        try:
            mainWindow.iconbitmap('Icon_for_windows.ico')

        except:
            time.sleep(0)

    #       -----------------------------------------------------

            # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                mainWindow.destroy()
            except:
                time.sleep(0)

            # create window
            WinDow = tk.Tk()
            WinDow.title('background image')

            # file for bg image
            fname = "NoClosing.gif.gif"
            bg_image = tk.PhotoImage(file=fname)

            # get the width and height of the image
            w = bg_image.width()
            h = bg_image.height()

            # size the window so the image will fill it
            WinDow.geometry('724x592')
            cv = tk.Canvas(width=w, height=h)

            # canvas placed on window
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="", fill="red", anchor='nw')

            # window's icon
            try:
                WinDow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

            # can't resize window
            WinDow.resizable(width=False, height=False)

            # creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            # puts the window in front of the menu
            WinDow.attributes('-topmost', True)

            # creates background
            WinDow["bg"] = "#FFFFFF"

            # does not allow window to be moved
            WinDow.overrideredirect(True)

            # does not allow it to be resized
            WinDow.resizable(width=False, height=False)

            # back to prev. window
            def noclose():

                # close window
                WinDow.destroy()

                # back to prev. window
                Load_RLE_Window()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # places button on window
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs window
            center(WinDow)
            WinDow.mainloop()

    #       -----------------------------------------------------

        # overide close window
        mainWindow.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of the others
        mainWindow.attributes('-topmost', True)

        # creates empty space between widgets
        emptyspace = Label(mainWindow, text=" ", bg="#FFFFFF")
        emptyspace.grid(sticky=tk.W)

        # text entry field
        imag = tk.PhotoImage(file="entry.gif")

        # create a frame and pack it
        frame2 = tk.Frame(mainWindow, bg='#FFFFFF', padx=15)
        frame2.grid()

        # subsample image
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg='#FFFFFF')

        # places image
        s.grid(column=2, row=20)
        s.image = imagee

        # entry field
        e = integersOnly(frame2, width=20, bg='#FFFFFF',
                         relief='flat', font=('Consolas', 18), fg='SteelBlue1')
        e.grid(column=2, row=20)

        # create a frame and pack it
        frame1 = tk.Frame(mainWindow, bg='#FFFFFF', padx=15)
        frame1.grid(sticky=tk.W)

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter rle button
        image = tk.PhotoImage(file="C.gif")

        # resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=parttwo, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='grey')
        emptyspace.grid()

        # function to exit the window and run the menu again

        def exitAndDoMenu():

            # destroys the window
            mainWindow.destroy()

            # loads the menu again
            menu()

    #       -----------------------------------------------------

       # creates enter button
        image = tk.PhotoImage(file="Back.gif")

        # resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=exitAndDoMenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # size of window
        mainWindow.geometry("750x592")

        # cant resize window
        mainWindow.resizable(width=False, height=False)

        # centers window
        center(mainWindow)

    #       -----------------------------------------------------

        # runs the function
        show_results()

    show_results()
    # what will happen if the file does not exist
 else:

                # closes the window
                Convert_rle.destroy()

                # runs the error function
                errorNoFile()

    #       -----------------------------------------------------

    #       -----------------------------------------------------

        # create a frame and pack it
        frame1 = tk.Frame(Convert_rle, bg='#FFFFFF', padx=15)
        frame1.grid(sticky=tk.W)

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter rle button
        image = tk.PhotoImage(file="C.gif")

        # resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=CompressData, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # importing filedialog in local scope to make function work
        try:
            from tkinter import filedialog
            # python 2 is below
        except:
            from Tkinter import tkFileDialog

            # function to browse for file
        def browse():

            # opens file dialog and lets user to browse for file
            Convert_rle.filename = filedialog.askopenfilename(
                filetypes=(('text files', 'txt'),))

            # asigns the file location to the variable
            file = Convert_rle.filename

            # runs the function to load the art through the browse function
            CcompressData()

    #       -----------------------------------------------------

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter button
        image = tk.PhotoImage(file="BfF.gif")

        # resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=browse, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='grey')
        emptyspace.grid()

    #       -----------------------------------------------------

        # function to exit the window
        def exit_rle_converter():

            # takes away the window
            Convert_rle.destroy()

            # displays the menu again
            menu()

    #       -----------------------------------------------------

       # creates enter button
        image = tk.PhotoImage(file="Back.gif")

        # resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=exit_rle_converter, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # size of window
        Convert_rle.geometry("724x592")

        # can't resize window
        Convert_rle.resizable(width=False, height=False)

        # centers window
        center(Convert_rle)

 #    ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    #                                           #-----------------------------------------------------------------------#
    #                                           |       function to create a new window for converting ascii art        |
    #                                           #-----------------------------------------------------------------------#

    def Convert_ASCII():

        ASCII_Converter = tk.Tk()

        # canvas for bg
        C = Canvas(ASCII_Converter)
        backg = PhotoImage(file="CtAAa.gif")

        # places image on canvas
        background_label = Label(ASCII_Converter, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # reference
        C.grid()
        C.img = backg

        # title for window
        ASCII_Converter.title("ASCII art program by Faeq Faisal")

        # icon for window
        try:
            ASCII_Converter.iconbitmap('Icon_for_windows.ico')

        except:
            time.sleep(0)

    #       -----------------------------------------------------

        # function to not allow program to end before any processes are complete
            # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                ASCII_Converter.destroy()
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

            # canvas for bg image
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

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
                Convert_ASCII()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # plces button on bg
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs window
            center(mainWindow)
            mainWindow.mainloop()

    #       -----------------------------------------------------

        # overide close button
        ASCII_Converter.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of the others
        ASCII_Converter.attributes('-topmost', True)

        # background colour
        ASCII_Converter["bg"] = "SteelBlue1"

        # creates empty space between widgets
        emptyspace = Label(ASCII_Converter, text=" ", bg="#FFFFFF")
        emptyspace.grid(sticky=tk.W)

        # text entry field
        imag = tk.PhotoImage(file="entry.gif")

        # create a frame and pack it
        frame2 = tk.Frame(ASCII_Converter, bg='#FFFFFF', padx=15)
        frame2.grid()

        # resiuzes bg for canvas
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg='#FFFFFF')

        # reference
        s.grid(column=2, row=5)
        s.image = imagee

        # entry field
        ASCII_Converter.entry = tk.Entry(
            frame2, width=20, bg='#FFFFFF', relief='flat', font=('Consolas', 18), fg='SteelBlue1')
        ASCII_Converter.entry.grid(column=2, row=5)

    #       -----------------------------------------------------

        # function to load and decode the data

        def load_data():

            # adds file extension if there isnt one already
            if ASCII_Converter.entry.get().lower().endswith(('.txt')):

                enterredfilename = ASCII_Converter.entry.get()
            else:

                enterredfilename = ASCII_Converter.entry.get()+'.txt'

            # Checks if the file exists
            if os.path.exists(enterredfilename) == True:

                # saves the text in entry field to a variable
                filename = enterredfilename

                # adds file extension to name of file so it can open
                file = enterredfilename

                # name of new file
                textfile = "NewDecodedArt.txt"

                # opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
                open(textfile, "w").close()

                # opens file
                openfile = open(file)

    #       -----------------------------------------------------

                # creates a while loop so that i can check every line one at a time
                while True:

                    # reads the line
                    line = openfile.readline()

                    # takes away the part that would indicate a new line so that it can be decoded
                    encoded_string = line.replace("\n", "")

                    # the string to be decoded
                    string = encoded_string

    #       -----------------------------------------------------

                    # function to split string into list

                    def split(str, num):
                        return [str[start:start+num] for start in range(0, len(str), num)]

    #       -----------------------------------------------------

                    # splitting string into packets of 3
                    splitUpStringwiththree = split(string, 3)

                    # creating a new list to write to later
                    new_string = []

                    # spliting the string again but this time in packets of 2
                    splitUpStringg = split(string, 2)

                    # loop to split the splitted string into a list with items of length 1
                    for item in splitUpStringwiththree:

                        # splitting into packets
                        r = split(item, 1)

                        # saving to our new list made up of strings
                        new_string = new_string+r

                    # another new list we will write to later
                    splitUpStringg = []

                    # loop to split the list into the reoccurences of the characters without the actual character
                    for i in splitUpStringwiththree:

                        # splitting into packets
                        rrt = split(i, 2)

                        # saving to our new list
                        splitUpStringg = splitUpStringg+rrt

                    # assigning our old list to a new variable so that we have a copy of the list to refer to when the original is already in use
                    v = new_string

                    # deleting the third character in every item
                    k = 3

                    # actually deleting the character
                    del new_string[k-1::k]

                    # joining the characters for the number of occurences together
                    mmm = [''.join(x) for x in zip(
                        new_string[0::2], new_string[1::2])]

    #       -----------------------------------------------------

                    # replacing the 0 in any integer representing the number of occurrences
                    for w in mmm:
                        if w[0] == '0':
                            w.replace('0', '')

    #       -----------------------------------------------------

                    # turning every item in the list into a integer
                    mmm = list(map(int, mmm))

                    # loop to get rid of unwanted items in the list for occurences
                    for i in splitUpStringg:

                        # checking if the length is equal to 2 (if so, this shows the number of occurences)
                        if len(i) == 2:

                            # finding the index of the item in its list
                            lop = splitUpStringg.index(i)

                            # getting rid of the item using its index previously found
                            splitUpStringg.pop(lop)

                    # loop to multiply the numbver to be shown by its actual bnumber of occurences
                    decodedString = [item for item, count in zip(
                        splitUpStringg, mmm) for i in range(count)]

                    # making the list into a string without annoying commas or square brackets that should not be there
                    makeitastring = ''.join(map(str, decodedString))

                    # adds the \n so that the next line can be put in when the loop goes again
                    decoded_string_with_new_line = makeitastring + "\n"

                    # creates and writes to a new file
                    WriteToFile = open(textfile, "a")

                    # writes the data to the file
                    WriteToFile.write(decoded_string_with_new_line)
                    WriteToFile.close

                    # if there is not another line:
                    if not line:

                        # ends loop
                        break

                # closes the file
                openfile.close()

                # opens file
                ReadFile = open(textfile, 'r')

                # reads file
                data = ReadFile.read()

                # closes file
                ReadFile.close()

                # creates a new window

                def WindowToDisplayArt():
                    try:
                        ASCII_Converter.destroy()
                    except:
                        time.sleep(0)

                    # opens text in window
                    ASCIIartONwindow = Tk()

                    # title for window
                    ASCIIartONwindow.title("ASCII art program by Faeq Faisal")

                    # icon for window
                    try:
                        ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')

                    except:
                        time.sleep(0)

    #       -----------------------------------------------------

                        # function to not allow program to end before any processes are complete

                    def on_closing():

                        # close window
                        try:
                            ASCIIartONwindow.destroy()
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

                        # canvas for bg image
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
                            WindowToDisplayArt()

                        # resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee,
                                           command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                        # places button on bg
                        Button.pack(side='left', padx=3, pady=0, anchor='s')
                        Button.image = backimagee

                        # runs window
                        center(mainWindow)
                        mainWindow.mainloop()

                    # overide close button
                    ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)

                    # puts the window in front of the others
                    ASCIIartONwindow.attributes('-topmost', True)

                    # background colour
                    ASCIIartONwindow["bg"] = "SteelBlue1"

                    # frame for bg
                    F1 = Frame(ASCIIartONwindow)
                    F1 = Frame(ASCIIartONwindow, width=400, height=450)
                    F1.place(height=7000, width=4000, x=100, y=100)

                    # configuring frame to size
                    F1.grid(columnspan=10, rowspan=10)
                    F1.grid_rowconfigure(0, weight=1)
                    F1.grid_columnconfigure(0, weight=1)

                    # bg image
                    photo = PhotoImage(file="HIYA.gif")
                    label = Label(ASCIIartONwindow, image=photo)

                    label.image = photo  # keep a reference!
                    label.grid(row=0, column=0, columnspan=20, rowspan=20)

                    # opens file
                    ReadFile = open(textfile, 'r')

                    # reads file
                    data = ReadFile.read()

                    # closes file
                    ReadFile.close()
                    artishere = tk.Message(ASCIIartONwindow, text=data, font=(
                        'Consolas', 13), fg='SteelBlue1', bg='#FFFFFF', width=90000)
                    artishere.grid(row=8, column=8)

                    # function to get mack to the menu
                    def backtomenu():
                        ASCIIartONwindow.destroy()
                        menu()

                    # creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    # resizes background image
                    backimagee = backimage.subsample(3, 3)
                    Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee,
                                       command=backtomenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                    # places button on bg
                    Button.grid(row=10, column=8)
                    Button.image = backimagee

                    # window size
                    ASCIIartONwindow.geometry("724x592")

                    # centers window
                    center(ASCIIartONwindow)

                WindowToDisplayArt()

    #       -----------------------------------------------------

                # if the file does not exist:
            else:

                # closes window
                ASCII_Converter.destroy()

                # runs the error
                errorNoFileForConverter()

    #       -----------------------------------------------------

        def Load_data():

            # gets file name from file dilog
            file = ASCII_Converter.filename

            # name of new file
            textfile = "NewDecodedArt.txt"

            # opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
            open(textfile, "w").close()

            # opens file
            openfile = open(file)

    #       -----------------------------------------------------

            # creates a while loop so that i can check every line one at a time
            while True:

                # reads the line
                line = openfile.readline()

                # takes away the part that would indicate a new line so that it can be decoded
                encoded_string = line.replace("\n", "")

                # the string to be decoded
                string = encoded_string

    #       -----------------------------------------------------

                # function to split string into list
                def split(str, num):
                    return [str[start:start+num] for start in range(0, len(str), num)]

    #       -----------------------------------------------------

                # splitting string into packets of 3
                splitUpStringwiththree = split(string, 3)

                # creating a new list to write to later
                new_string = []

                # spliting the string again but this time in packets of 2
                splitUpStringg = split(string, 2)

                # loop to split the splitted string into a list with items of length 1
                for item in splitUpStringwiththree:

                    # splitting into packets
                    r = split(item, 1)

                    # saving to our new list made up of strings
                    new_string = new_string+r

                # another new list we will write to later
                splitUpStringg = []

                # loop to split the list into the reoccurences of the characters without the actual character
                for i in splitUpStringwiththree:

                    # splitting into packets
                    rrt = split(i, 2)

                    # saving to our new list
                    splitUpStringg = splitUpStringg+rrt

                # assigning our old list to a new variable so that we have a copy of the list to refer to when the original is already in use
                v = new_string

                # deleting the third character in every item
                k = 3

                # actually deleting the character
                del new_string[k-1::k]

                # joining the characters for the number of occurences together
                mmm = [''.join(x)
                       for x in zip(new_string[0::2], new_string[1::2])]

    #       -----------------------------------------------------

                # replacing the 0 in any integer representing the number of occurrences
                for w in mmm:
                    if w[0] == '0':
                        w.replace('0', '')

    #       -----------------------------------------------------

                # turning every item in the list into a integer
                mmm = list(map(int, mmm))

                # loop to get rid of unwanted items in the list for occurences
                for i in splitUpStringg:

                    # checking if the length is equal to 2 (if so, this shows the number of occurences)
                    if len(i) == 2:

                        # finding the index of the item in its list
                        lop = splitUpStringg.index(i)

                        # getting rid of the item using its index previously found
                        splitUpStringg.pop(lop)

                # loop to multiply the numbver to be shown by its actual bnumber of occurences
                decodedString = [item for item, count in zip(
                    splitUpStringg, mmm) for i in range(count)]

                # making the list into a string without annoying commas or square brackets that should not be there
                makeitastring = ''.join(map(str, decodedString))

                # adds the \n so that the next line can be put in when the loop goes again
                decoded_string_with_new_line = makeitastring + "\n"

                # creates and writes to a new file
                WriteToFile = open(textfile, "a")

                # writes the data to the file
                WriteToFile.write(decoded_string_with_new_line)
                WriteToFile.close

                # if there is not another line:
                if not line:

                    # ends loop
                    break

    #       -----------------------------------------------------

            # closes the file
            openfile.close()

            # opens file
            ReadFile = open(textfile, 'r')

            # reads file
            data = ReadFile.read()

            # closes file
            ReadFile.close()

            # creates a new window
            def WindowToDisplayArt():

                try:
                    ASCII_Converter.destroy()
                except:
                    time.sleep(0)

                # opens text in window
                ASCIIartONwindow = Tk()

                # title for window
                ASCIIartONwindow.title("ASCII art program by Faeq Faisal")

                # icon for window
                try:
                    ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')
                except:
                    time.sleep(0)

    #       -----------------------------------------------------

                    # function to not allow program to end before any processes are complete

                def on_closing():

                    # close window
                    try:
                        ASCIIartONwindow.destroy()
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

                    # canvas for bg
                    cv.pack(side='top', fill='both', expand='yes')
                    cv.create_image(0, 0, image=bg_image, anchor='nw')

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
                        WindowToDisplayArt()

                    # resizes background image
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee,
                                       command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                    # places button on bg
                    Button.pack(side='left', padx=3, pady=0, anchor='s')
                    Button.image = backimagee

                    # runs window
                    center(mainWindow)
                    mainWindow.mainloop()

    #       -----------------------------------------------------

                # overide close button
                ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)

                # puts the window in front of the others
                ASCIIartONwindow.attributes('-topmost', True)

                # background colour
                ASCIIartONwindow["bg"] = "SteelBlue1"

                # frame for bg
                F1 = Frame(ASCIIartONwindow)
                F1 = Frame(ASCIIartONwindow, width=400, height=450)
                F1.place(height=7000, width=4000, x=100, y=100)

                # configures freame for size
                F1.grid(columnspan=10, rowspan=10)
                F1.grid_rowconfigure(0, weight=1)
                F1.grid_columnconfigure(0, weight=1)

                # bg image
                photo = PhotoImage(file="HIYA.gif")
                label = Label(ASCIIartONwindow, image=photo)

                label.image = photo  # keep a reference
                label.grid(row=0, column=0, columnspan=20, rowspan=20)

                # opens file
                ReadFile = open(textfile, 'r')

                # reads file
                data = ReadFile.read()

                # closes file
                ReadFile.close()
                artishere = tk.Message(ASCIIartONwindow, text=data, font=(
                    'Consolas', 13), fg='SteelBlue1', bg='#FFFFFF', width=90000)
                artishere.grid(row=8, column=8)

                # function to get back to menu
                def backtomenu():
                    ASCIIartONwindow.destroy()
                    menu()

                # creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                # resizes background image
                backimagee = backimage.subsample(3, 3)
                Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee,
                                   command=backtomenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                # places buytton on window
                Button.grid(row=10, column=8)
                Button.image = backimagee

                # centers window
                center(ASCIIartONwindow)

            # runs function above
            WindowToDisplayArt()

    #       -----------------------------------------------------

        # create a frame and pack it
        frame1 = tk.Frame(ASCII_Converter, bg='#FFFFFF', padx=15)
        frame1.grid(sticky=tk.W)

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter rle button
        image = tk.PhotoImage(file="C.gif")

        # resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=load_data, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # allows user to browse for file
        try:
            from tkinter import filedialog

        except:
            from Tkinter import tkFileDialog

    #       -----------------------------------------------------

        def browse():

            # opens file dialog and lets user to browse for file
            ASCII_Converter.filename = filedialog.askopenfilename(
                filetypes=(('text files', 'txt'),))

            # asigns the file location to the variable
            file = ASCII_Converter.filename

            # runs the function to load the art through the browse function
            Load_data()

    #       -----------------------------------------------------

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter button
        image = tk.PhotoImage(file="BfF.gif")

        # resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=browse, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='grey')
        emptyspace.grid()

    #       -----------------------------------------------------

        # function to exit the window

        def exit_converter():

            # takes away the window
            ASCII_Converter.destroy()

            # shows the menu again
            menu()

    #       -----------------------------------------------------

       # creates enter button
        image = tk.PhotoImage(file="Back.gif")

        # resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=exit_converter, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # size of window
        ASCII_Converter.geometry("775x592")

        # cant resize window
        ASCII_Converter.resizable(width=False, height=False)

        # centers window
        center(ASCII_Converter)


# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                                               #-------------------------------------------------------------------#
#                                               |       function to create a new window for loading ascii art       |
#                                               #-------------------------------------------------------------------#

    def ASCII_ART_DISPLAYER():

        display = tk.Tk()

        # canvas for bg
        C = Canvas(display)
        backg = PhotoImage(file="LYAA.gif")

        # bg image
        background_label = Label(display, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # reference
        C.grid()
        C.img = backg

        # title for window
        display.title("ASCII art program by Faeq Faisal")

        # icon for window
        try:
            display.iconbitmap('Icon_for_windows.ico')

        except:
            time.sleep(0)

    #       -----------------------------------------------------

        # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                display.destroy()
            except:
                time.sleep(0)

            # window created
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

            # canvas for bg
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

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
                ASCII_ART_DISPLAYER()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # places button on bg
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs window
            center(mainWindow)
            mainWindow.mainloop()

    #       -----------------------------------------------------

        # overides the close button
        display.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of the menu
        display.attributes('-topmost', True)

        # background colour
        display["bg"] = "SteelBlue1"

        # creates empty space between widgets
        emptyspace = Label(display, text=" ", bg="#FFFFFF")
        emptyspace.grid()

    #       -----------------------------------------------------

        # what happens when you press the button
        def displayArt():

            # adds file extension if there isnt one already
            if e.get().lower().endswith(('.txt')):

                enterredfilename = e.get()
            else:

                enterredfilename = e.get()+'.txt'

            # Checks if the file exists
            if os.path.exists(enterredfilename) == True:

                # saves the text in entry field to a variable
                filename = enterredfilename

                # adds file extension to name of file so it can open
                file = enterredfilename

                # opens file
                ReadFile = open(file, 'r')

                # reads file
                data = ReadFile.read()

                # closes file
                ReadFile.close()

    #       -----------------------------------------------------

                # creates a new window
                def WindowToDisplayArt():

                    display.destroy()

                    # opens text in window
                    ASCIIartONwindow = Tk()

                    # title for window
                    ASCIIartONwindow.title("ASCII art program by Faeq Faisal")

                    # icon for window
                    try:
                        ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')

                    except:
                        time.sleep(0)

    #       -----------------------------------------------------

                    # function to not allow program to end before any processes are complete

                    def on_closing():

                        # close window
                        try:
                            ASCIIartONwindow.destroy()
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

                        # canvas for bg
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
                            ASCII_ART_DISPLAYER()

                        # resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee,
                                           command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                        # places button on bg
                        Button.pack(side='left', padx=3, pady=0, anchor='s')
                        Button.image = backimagee

                        # runs window
                        center(mainWindow)
                        mainWindow.mainloop()

    #       -----------------------------------------------------

                    # overides the close button
                    ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)

                    # puts the window in front of the menu
                    ASCIIartONwindow.attributes('-topmost', True)

                    # does not allow it to be resized
                    ASCIIartONwindow.resizable(width=False, height=False)

                    # background colour
                    ASCIIartONwindow["bg"] = "SteelBlue1"

                    # frame for bg
                    F1 = Frame(ASCIIartONwindow)
                    F1 = Frame(ASCIIartONwindow, width=400, height=450)
                    F1.place(height=7000, width=4000, x=100, y=100)

                    # confiugres frame for size
                    F1.grid(columnspan=10, rowspan=10)
                    F1.grid_rowconfigure(0, weight=1)
                    F1.grid_columnconfigure(0, weight=1)

                    # bg image
                    photo = PhotoImage(file="HIYA.gif")
                    label = Label(ASCIIartONwindow, image=photo)

                    label.image = photo  # keep a reference
                    label.grid(row=0, column=0, columnspan=20, rowspan=20)

                    # opens file
                    ReadFile = open(file, 'r')

                    # reads file
                    data = ReadFile.read()

                    # closes file
                    ReadFile.close()
                    artishere = tk.Message(ASCIIartONwindow, text=data, font=(
                        'Consolas', 13), fg='SteelBlue1', bg='#FFFFFF', width=90000)
                    artishere.grid(row=8, column=8)

                    # funtion to back to menu
                    def backtomenu():
                        ASCIIartONwindow.destroy()
                        menu()

                    # creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    # resizes background image
                    backimagee = backimage.subsample(3, 3)
                    Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee,
                                       command=backtomenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                    # places button on bg
                    Button.grid(row=10, column=8)
                    Button.image = backimagee

                    # centers window
                    center(ASCIIartONwindow)

                    # runs function
                WindowToDisplayArt()

                # if the file does not exist:
            else:
                display.destroy()

                # runs the error
                errorNoFileForDisplayer()

    #       -----------------------------------------------------

        # text entry field
        imag = tk.PhotoImage(file="entry.gif")

        # create a frame and pack it
        frame2 = tk.Frame(display, bg='#FFFFFF', padx=15)
        frame2.grid()

        # sizing image
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg='#FFFFFF')

        # reference
        s.grid(column=2, row=5)
        s.image = imagee

        # entry field
        e = tk.Entry(frame2, width=20, bg='#FFFFFF', relief='flat',
                     font=('Consolas', 18), fg='SteelBlue1')
        e.grid(column=2, row=5)

        # create a frame and pack it
        frame1 = tk.Frame(display, bg='#FFFFFF', padx=15)
        frame1.grid(sticky=tk.W)

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter rle button
        image = tk.PhotoImage(file="C.gif")

        # resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=displayArt, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

    #       -----------------------------------------------------

        # loads button
        # imports file dialog to allow the user to brows for their art
        try:
            from tkinter import filedialog
        except:
            from Tkinter import tkFileDialog

        # what happens when you press the button
        def displayArtt():

            # gets file location
            file = display.filename

            # opens file
            ReadFile = open(file, 'r')

            # reads file
            data = ReadFile.read()

            # closes file
            ReadFile.close()

    #       -----------------------------------------------------

            # creates a new window
            def WindowToDisplayArt():
                try:
                    display.destroy()
                except:
                    time.sleep(0)

                # opens text in window
                ASCIIartONwindow = Tk()

                # title for window
                ASCIIartONwindow.title("ASCII art program by Faeq Faisal")

                # icon for window
                try:
                    ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')

                except:
                    time.sleep(0)

    #       -----------------------------------------------------

                # function to not allow program to end before any processes are complete

                def on_closing():

                    # close window
                    try:
                        ASCIIartONwindow.destroy()
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

                    # canvas for bg
                    cv.pack(side='top', fill='both', expand='yes')
                    cv.create_image(0, 0, image=bg_image, anchor='nw')

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
                        displayArtt()

                    # resizes background image
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee,
                                       command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                    # places button on bg
                    Button.pack(side='left', padx=3, pady=0, anchor='s')
                    Button.image = backimagee

                    # runs the window
                    center(mainWindow)
                    mainWindow.mainloop()

    #       -----------------------------------------------------

                # overides the close button
                ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)

                # puts the window in front of the menu
                ASCIIartONwindow.attributes('-topmost', True)

                # does not allow it to be resized
                ASCIIartONwindow.resizable(width=False, height=False)

                # background colour
                ASCIIartONwindow["bg"] = "SteelBlue1"

                # frame for bg
                F1 = Frame(ASCIIartONwindow)
                F1 = Frame(ASCIIartONwindow, width=400, height=450)
                F1.place(height=7000, width=4000, x=100, y=100)

                # configures frame to window size
                F1.grid(columnspan=10, rowspan=10)
                F1.grid_rowconfigure(0, weight=1)
                F1.grid_columnconfigure(0, weight=1)

                # image for bg
                photo = PhotoImage(file="HIYA.gif")
                label = Label(ASCIIartONwindow, image=photo)

                label.image = photo  # keep a reference
                label.grid(row=0, column=0, columnspan=20, rowspan=20)

                # opens file
                ReadFile = open('logoart.txt', 'r')

                # reads file
                data = ReadFile.read()

                # closes file
                ReadFile.close()
                artishere = tk.Message(ASCIIartONwindow, text=data, font=(
                    'Consolas', 13), fg='SteelBlue1', bg='#FFFFFF', width=90000)
                artishere.grid(row=8, column=8)

                # function to go back to menu
                def backtomenu():
                    ASCIIartONwindow.destroy()
                    menu()

                # creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                # resizes background image
                backimagee = backimage.subsample(3, 3)
                Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee,
                                   command=backtomenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

                # places button on bg
                Button.grid(row=10, column=8)
                Button.image = backimagee

                # centers window
                center(ASCIIartONwindow)

                # runs function
            WindowToDisplayArt()

    #       -----------------------------------------------------

        # allows user to browse for file

        def browse():

            # opens file dialog and lets user to browse for file
            display.filename = filedialog.askopenfilename(
                filetypes=(('text files', 'txt'),))

            # asigns the file location to the variable
            file = display.filename

            # runs the function to load the art through the browse function
            displayArtt()

    #       -----------------------------------------------------

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='SteelBlue1')
        emptyspace.grid()

        # creates enter button
        image = tk.PhotoImage(file="BfF.gif")

        # resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=browse, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # creates empty space between widgets
        emptyspace = Label(
            frame1, text="_____________________________________________________________________", bg="#FFFFFF", fg='grey')
        emptyspace.grid()

    #       -----------------------------------------------------

        # function to exit the window

        def exit_this_displayer():

            # destroys the window
            display.destroy()

            # shows the menu again
            menu()

    #       -----------------------------------------------------

       # creates enter button
        image = tk.PhotoImage(file="Back.gif")

        # resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee,
                                  command=exit_this_displayer, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        # size of window
        display.geometry("724x592")

        # cant resize window
        display.resizable(width=False, height=False)

        # centers window
        center(display)

# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    def About():

        About_window = tk.Tk()

        # canvas for bg
        C = Canvas(About_window)
        backg = PhotoImage(file="About.gif")

        # bg on canvas
        background_label = Label(About_window, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # reference
        C.grid()
        C.img = backg

        # window's title
        About_window.title("ASCII art program by Faeq Faisal")

        # window's icon
        try:
            About_window.iconbitmap('Icon_for_windows.ico')

        except:
            time.sleep(0)

#       -----------------------------------------------------

    # function to not allow program to end before any processes are complete

        def on_closing():

            # close window
            try:
                About_window.destroy()
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

            # canvas for bg
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')

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
                About()

            # resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee,
                               command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

            # places button on bg
            Button.pack(side='left', padx=3, pady=0, anchor='s')
            Button.image = backimagee

            # runs window
            center(mainWindow)
            mainWindow.mainloop()

#       -----------------------------------------------------

        # overides the close button ( 'X' button) to run the function above
        About_window.protocol("WM_DELETE_WINDOW", on_closing)

        # puts the window in front of all other windows
        About_window.attributes('-topmost', True)

        # background colour
        About_window["bg"] = "#FFFFFF"

        # creates empty space between widgets
        emptyspace = Label(About_window, text=" ", bg="#FFFFFF")
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF")
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF")
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF",
                           width=1, font=('calibri', 9), fg='SteelBlue1')
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

        # creates empty space between widgets
        emptyspace = Label(About_window, text="", bg="#FFFFFF", width=1)
        emptyspace.grid(sticky="w")

#       -----------------------------------------------------

        # exits the error message
        def exit_the_about():

            # takes away the error window
            About_window.destroy()

            # shows the previous window again
            menu()

#       -----------------------------------------------------

        # create a frame and pack it
        frame1 = tk.Frame(About_window, bg='#FFFFFF', padx=109)
        frame1.grid(sticky=tk.W)

        # creates enter rle button
        backimage = tk.PhotoImage(file="Back.gif")

        # resizes background image
        backimagee = backimage.subsample(5, 5)
        Button = tk.Button(frame1, relief=FLAT, image=backimagee,
                           command=exit_the_about, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        Button.grid()
        Button.image = backimagee

        # size of window
        About_window.geometry("724x592")

        # can't resize window
        About_window.resizable(width=False, height=False)

        # centers window on the screen
        center(About_window)


# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                             #------------------------------------------------------------------------------------------#
#                             |                                 menu's code starts here                                  |
#                             #------------------------------------------------------------------------------------------#

# function to not allow program to end before any processes are complete


    def on_closing():

        # close window
        try:
            window_for_menu.destroy()
        except:
            time.sleep(0)

        # new window created
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

        # new canvas for bg
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(0, 0, image=bg_image, anchor='nw')

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
            menu()

        # resizes background image
        backimagee = backimage.subsample(2, 2)
        Button = tk.Button(cv, relief='flat', image=backimagee,
                           command=noclose, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on bg
        Button.pack(side='left', padx=3, pady=0, anchor='s')
        Button.image = backimagee

        # runs window
        center(mainWindow)
        mainWindow.mainloop()

#       -----------------------------------------------------

    # overides the close button
    window_for_menu.protocol("WM_DELETE_WINDOW", on_closing)

    # puts the window in front of the others
    window_for_menu.attributes('-topmost', False)

    # creates a canvas to put the image on
    PutImageForBackground = Canvas(window_for_menu)

    # displays canvas
    PutImageForBackground.grid()

    # puts image for background onto canvas
    image1 = PhotoImage(file="new.gif")

    # keep a link to the image to stop the image being garbage collected
    PutImageForBackground.img = image1

    # resizes background image
    displayimage = image1.subsample(1, 1)

    # displays image in background
    PutImageForBackground.create_image(400, 300, image=displayimage)


#       -----------------------------------------------------

    # creating the class, Window, and the Frame

    class Window(Frame):

        # Define settings
        def __init__(self, master=None):

            # parameters that are sent through the Frame class.
            Frame.__init__(self, master)

            # reference to the window
            self.master = master

            # runs the settings
            self.init_window()

        # Creation of init_window
        def init_window(self):

            #       -----------------------------------------------------

            # icon for the window
            try:
                self.master.iconbitmap('Icon_for_windows.ico')

            except:
                time.sleep(0)

            # changing the title of the window
            self.master.title("ASCII art program by Faeq Faisal")

            # window size created
#       -----------------------------------------------------

            self.master.geometry("724x592")

            self.master.resizable(width=False, height=False)

#       -----------------------------------------------------

            # allowing the text to take the full space of the window
            self.grid()


# ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            # creating a menu
            menu = Menu(self.master)
            self.master.config(menu=menu)
            # create the file object
            file = Menu(menu)

            def exit_program():
                self.master.destroy()

                mainWindow = tk.Tk()
                mainWindow.title('Bye!')

                fname = "Bye.gif"
                bg_image = tk.PhotoImage(file=fname)
                w = bg_image.width()
                h = bg_image.height()
                mainWindow.geometry('200x100')
                cv = tk.Canvas(width=w, height=h)
                cv.pack(side='top', fill='both', expand='yes')
                cv.create_image(0, 0, image=bg_image, anchor='nw')
                cv.create_text(15, 20, text="", fill="red", anchor='nw')

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

            PutImageForBackground.create_window(900, 900)
            edit = Menu(menu)

        def client_exit(self):
            exit()

    app = Window(window_for_menu)
    center(window_for_menu)
    window_for_menu.mainloop()


if __name__ == '__main__':
  menu()

