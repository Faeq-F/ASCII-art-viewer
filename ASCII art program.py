#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#
#
#                                                     #---------------------------------------------------#
#                                                     |       imports everything I need from modules      |
#                                                     #---------------------------------------------------#
#
#                                                       allows me to make a graphical user interface (GUI)
#
#                           used try and except due to the fact that tkinter uses capitalisation on some versions of python and not on others
#                                  both have 'as tk' so that I can use the same code no matter what version of python the user is on
#

try:
    from tkinter import *
    
    #makes sure that no matter what update you are on, the program will still try to work
    import tkinter as tk

    
except ImportError:
    
    from Tkinter import *
    
    #used if on a lower update eventhough being on the latest version of python is advised
    import Tkinter as tk


#allows me to use math to decompress and compress data
from math import *


#allows me to check the screen resolution being used by the user and
#modify the look of the proram according to what the screen can support
import ctypes


#allows me to manipulate os (mostly used for checking if things exist)
import os


#used for the program to pass errors that would fail the program when on different operating systems
import time


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#
#
#                                                           #---------------------------------------#
#                                                           |           global variables            |
#                                                           #---------------------------------------#
#
#
#                                                        these are variables used throughout the program
#                                                   so instead of declaring them continously as local variables
#                                                     I can declare them once, here, as a global variable
#                                                        and change their value throughout the program.
#                                                        This allows the program to be faster as less
#                                                        variables are used and needed to be checked
#                                                    every single time the program moves to a new window

data_from_rle_inputter = ""

textfile = ""
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                                                        #-------------------------------------------#
#                                                        |       centers all windows on screen       |
#                                                        #-------------------------------------------#


def center(win):
    
    #updates window to make it active
    win.update_idletasks()
    
    #finds width of screen
    width = win.winfo_width()
    
    #finds height of screen
    height = win.winfo_height()
    
    #creates the x coordinate for the window by finding the center by dividing it by 2
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    
    #creates the y coordinate for the window by finding the center by dividing it by 2
    y = (win.winfo_screenheight() // 2) - (height // 2)
    
    #creates the final coordinates
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                                                           #-----------------------------------#
#                                                           |       Creates original menu       |
#                                                           #-----------------------------------#
#                                                           
#
#                                                           the functions after this section are
#                                                         declared and programmed to do their job.
#                                                          They are then used by the buttons that
#                                                         are declared and showed, afterwards, on
#                                                                        the menu.


def menu():
    
    #creates window
    window_for_menu = tk.Tk()
    
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


        
#          #----------------------------------------------------------------------------------------------------------------------------------#
#          |       Class so that the entry field in the next function can only allow numbers so that there can only be a integer inputted     |
#          #----------------------------------------------------------------------------------------------------------------------------------#



    #takes entryfield as argument
    class integersOnly(tk.Entry):
        
        #creates entry field
        def __init__(self, master=None, **kwargs):
            
            #takes the entry as a string
            self.var = tk.StringVar()
            
            #creates the field
            tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
            
            #empty string for characters other than integers to be replaced with
            self.old_value = ''
            
            #checks integers
            self.var.trace('w', self.check)
            
            #replaces characters other than integers
            self.get, self.set = self.var.get, self.var.set
            
        #function to check that only integers are left
        def check(self, *args):
            
            #check if it is a integer
            if self.get().isdigit():
                
                #the current value is only digits; allow this
                self.old_value = self.get()
                
            #no integer?
            else:
                
                # there's non-digit characters in the input; reject this 
                self.set(self.old_value)
        

    def Load_RLE_Window():

        #creates window
        mainWindow = tk.Tk()

        #canvas to show bg image        
        C = Canvas(mainWindow)
        backg = PhotoImage(file = "ERd.gif")

        #placing the bg image on window
        background_label = Label(mainWindow, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #reference back to bg image
        C.grid()
        C.img = backg


    #------------------------------#
        
        #second part of process (uer entering the rle encoded data)
        def parttwo():

            #getting the value from the entry field
            number = e.get()
            mainWindow.destroy()

            #the error to show when he user enters a number below 3
            
            def error():
                
                #creates window
                error_window=tk.Tk()

                #window's title
                error_window.title("ASCII art program by Faeq ")

                #window's icon
                try:
                    error_window.iconbitmap('Icon_for_windows.ico')

                # if using linux (eg. ubuntu or mac os), the process is
                #skipped as the os does not support icons in the title bar
                
                except:
                    time.sleep(0)



            #       -----------------------------------------------------
                    
                #function to not allow program to end before any processes are complete
            
                def on_closing():
                    
                    #close window
                    try:
                        error_window.destroy()
                        
                    except:
                        time.sleep(0)
                        
                    #create window
                    mainWindow = tk.Tk()
                    
                    
                    #image file for bg
                    fname = "NoClosing.gif.gif"
                    bg_image = tk.PhotoImage(file=fname)
                    
                    # get the width and height of the image
                    w = bg_image.width()
                    h = bg_image.height()
                    
                    # size the window so the image will fill it
                    mainWindow.geometry('724x592')
                    
                    #canvas to use bg image
                    cv = tk.Canvas(width=w, height=h)
                    cv.pack(side='top', fill='both', expand='yes')

                    #putting the image in the north west corner
                    cv.create_image(0, 0, image=bg_image, anchor='nw')
                    cv.create_text(15, 20, text="", fill="red", anchor='nw')
                    
                    #window's icon
                    try:
                        mainWindow.iconbitmap('Icon_for_windows.ico')
                    except:
                        time.sleep(0)

                    #user can't resize window
                    mainWindow.resizable(width=False, height=False)
                    
                    #creates enter rle button
                    backimage = tk.PhotoImage(file="Back.gif")

                    #puts the window in front of the menu
                    mainWindow.attributes('-topmost', True)
                    
                    #creates background
                    mainWindow["bg"] = "#FFFFFF"

                    
                    #does not allow window to be moved
                    mainWindow.overrideredirect(True)

                        
                    #does not allow it to be resized
                    mainWindow.resizable(width=False, height=False)

                    #back to prev. window
                    def noclose():

                        #close window
                        mainWindow.destroy()
                        
                        #back to prev. window
                        error()
                        

                    #resizes background image
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #placing button on window
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')
                    Button.image= backimagee

                    #running the window
                    center(mainWindow)
                    mainWindow.mainloop()

            #           -----------------------------------------------------
                   
                #overides the close button ( 'X' button) to run the function above
                error_window.protocol("WM_DELETE_WINDOW", on_closing)
                
                #puts the window in front of all other windows
                error_window.attributes('-topmost', True)
                
                #frame for the bg image
                F1=Frame(error_window)
                F1=Frame(error_window,width=400,height=450)

                #placing the frame on the window
                F1.place(height=7000, width=4000, x=100, y=100)
                F1.grid(columnspan=10,rowspan=10)

                #configuring the placement of the frame on the window
                F1.grid_rowconfigure(0,weight=1)
                F1.grid_columnconfigure(0,weight=1)

                #image for bg
                photo=PhotoImage(file="errorLines.gif")
                label = Label(error_window,image = photo)
                
                label.image = photo # keep a reference
                label.grid(row=0,column=0,columnspan=20,rowspan=20)

            #       -----------------------------------------------------
                
                #exits the error message
                def exit_the_error():
                    
                    #takes away the error window
                    error_window.destroy()
                    
                    #shows the previous window again
                    Load_RLE_Window()

            #       -----------------------------------------------------            

                 #creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                #resizes background image
                backimagee = backimage.subsample(3, 3)
                Button = tk.Button(error_window, relief='flat', image=backimagee, command =exit_the_error ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                #placing the button on the window
                Button.grid(row = 18, column = 4)
                Button.image= backimagee
                
                #size of window
                error_window.geometry("724x592")
                
                #can't resize window
                error_window.resizable(width=False, height=False)
                
                #centers window on the screen
                center(error_window)

            #checks if anything is inputted on the entry field
            if number == '':

                #if not it runs the error defined above
                error()

            #checks if the number put in was 3 or above
            elif float(number) < 3:

                #if not, it runs the error
                error()
                
            #if all requirements are met, it allows the user to enter their data
            else:

                #creates a checking variable to check the nuber of line inputted by the user
                check = 0

                #makes he number a integer
                number = int(number)

                #wipes the file
                open('NewDeCompressedData.txt', 'w').close()
                #------------------------------#
                
                #while loop to check the number of lines
                while number > check:

                    #creates trhe window
                    window=tk.Tk()

                    #size of window
                    window.geometry("750x592")

                    #centers the window
                    center(window)
                    
                    #can't resize window
                    window.resizable(width=False, height=False)
                    
                    #does not allow window to be moved
                    window.overrideredirect(True)

                    #canvas to show bg image
                    C = Canvas(window)
                    backg = PhotoImage(file = "input.gif")
                    
                    #places the bg image on the window
                    background_label = Label(window, image=backg)
                    background_label.place(x=0, y=0, relwidth=1, relheight=1)

                    #references the bg image
                    C.grid()
                    C.img = backg

                                    
                    #creates empty space between widgets
                    emptyspace = Label(window, text=" ",bg="#FFFFFF")
                    emptyspace.grid(sticky = tk.W)
                    
                    #text entry field
                    imag = tk.PhotoImage(file="entry.gif")
                    
                    # create a frame and pack it
                    frame2 = tk.Frame(window,bg='#FFFFFF',padx=15)
                    frame2.grid()

                    #makes the image smaller (by subsampling)
                    imagee = imag.subsample(3, 3)
                    s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')

                    #places the image behind the entry field
                    s.grid(column = 2, row = 20)
                    s.image = imagee

                    #creartes a entry field that only allows integers to be entered
                    #(uses a class that I defined above)
                    
                    entry = Entry(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
                    entry.grid(column = 2, row = 20)

                    #function to exit each window
                    def exitt():
                        
                        #save data
                        data_from_rle_inputter = entry.get()
                        
                        #saves data to new variable (easier to read what is going on)
                        encoded_string = data_from_rle_inputter
                        
                        #the string to be decoded
                        string = encoded_string


    #       -----------------------------------------------------

                        #function to split string into list
                        def split(str, num):
                            return [ str[start:start+num] for start in range(0, len(str), num) ]
                        
    #       -----------------------------------------------------                            

                        #splitting string into packets of 3
                        splitUpStringwiththree = split(string,3)
                        
                        #creating a new list to write to later
                        new_string = []
                        
                        #spliting the string again but this time in packets of 2
                        splitUpStringg = split(string,2)
                        
                        #loop to split the splitted string into a list with items of length 1
                        for item in splitUpStringwiththree:
                            
                            #splitting into packets
                            r = split(item,1)
                            
                            #saving to our new list made up of strings
                            new_string = new_string+r
                            
                        #another new list we will write to later
                        splitUpStringg = []
                        
                        #loop to split the list into the reoccurences of the characters without the actual character
                        for i in splitUpStringwiththree:
                            
                            #splitting into packets
                            rrt = split(i,2)
                            
                            #saving to our new list
                            splitUpStringg = splitUpStringg+rrt
                            
                        #assigning our old list to a new variable so that we have a copy of the list to refer to when the original is already in use
                        v = new_string

                        #deleting the third character in every item
                        k = 3
                        
                        #actually deleting the character
                        del new_string[k-1::k]
                        
                        #joining the characters for the number of occurences together
                        mmm = [''.join(x) for x in zip(new_string[0::2], new_string[1::2])]

    #       -----------------------------------------------------

                        
                        #replacing the 0 in any integer representing the number of occurrences
                        for w in mmm:
                            
                            if w[0] == '0':
                                
                                w.replace('0', '')

    #       -----------------------------------------------------

                        #turning every item in the list into a integer
                        mmm = list(map(int, mmm))

                        #loop to get rid of unwanted items in the list for occurences
                        for i in splitUpStringg:
                            
                            #checking if the length is equal to 2 (if so, this shows the number of occurences)
                            if len(i)==2:
                                
                                #finding the index of the item in its list
                                lop = splitUpStringg.index(i)
                                
                                #getting rid of the item using its index previously found
                                splitUpStringg.pop(lop)
                                
                        #loop to multiply the numbver to be shown by its actual bnumber of occurences
                        decodedString = [item for item, count in zip(splitUpStringg, mmm) for i in range(count)]

                        #making the list into a string without annoying commas or square brackets that should not be there
                        makeitastring = ''.join(map(str, decodedString))

                        #makes sure that the next line entered is on a new line in the file
                        decoded_string_to_write = makeitastring + "\n"
                        
                        #writes the data to the file
                        
                        #name of new file
                        textfile = "NewDeCompressedData.txt"
                        
                        #creates and writes to a new file
                        WriteToFile = open(textfile,"a")

                        #writes to the file and closes it
                        WriteToFile.write(decoded_string_to_write)
                        WriteToFile.close()

                        #closes the window
                        window.destroy()
             
                    #background colour
                    window["bg"] = "SteelBlue1"
                        
                    # create a frame and pack it
                    frame1 = tk.Frame(window,bg='#FFFFFF',padx=15)
                    frame1.grid(sticky=tk.W)

                    #creates empty space between widgets
                    emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
                    emptyspace.grid()
                    
                    #creates enter rle button
                    image = tk.PhotoImage(file="C.gif")
                    
                    #resizes background image
                    imagee = image.subsample(3, 3)
                    ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =exitt ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places image button
                    ButtonToEnter.grid(sticky=tk.W)
                    ButtonToEnter.image = imagee

                        
                    #creates empty space between widgets
                    emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
                    emptyspace.grid()

                    #runs the window
                    window.mainloop()
                    
                    #during the window being shown, itr checks if it is still
                    #active to stop more windows from going over them
                    while True:

                        #try and except is used as the user can close the window at any time,
                        #and when they do, I want to not get a defining error
                        try:

                            #'checks if the window is running
                            if 'normal' == window.state():
                                
                                #if it is, the program does nothing
                                time.sleep(0)

                        #if the window is no longer running, the check variable is updated and the loop is broken
                        except:

                            #check is updated
                            check = check + 1
                            break
                        
                #function to display the art
                def display():
                            
                    #opens text in window
                    ASCIIartONwindowThatIsDecompressed = Tk()
                    
                    #title for window
                    ASCIIartONwindowThatIsDecompressed.title("ASCII art program by Faeq ")
                    
                    #icon for window
                    try:
                        ASCIIartONwindowThatIsDecompressed.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)

            #       -----------------------------------------------------
                        
                                
                    #function to not allow program to end before any processes are complete

                    def on_closing():
                        
                        #close window
                        try:
                            ASCIIartONwindowThatIsDecompressed.destroy()
                        except:
                            time.sleep(0)

                        #creates window
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

                        #puts image on window
                        cv.pack(side='top', fill='both', expand='yes')
                        cv.create_image(0, 0, image=bg_image, anchor='nw')
                        
                        #configuring the image to be in the north west corner
                        cv.create_text(15, 20, text="", fill="red", anchor='nw')
                        
                        
                        #window's icon
                        try:
                            mainWindow.iconbitmap('Icon_for_windows.ico')
                            
                        except:
                            time.sleep(0)

                        #user can't resize window
                        mainWindow.resizable(width=False, height=False)
                        
                        #image for button
                        backimage = tk.PhotoImage(file="Back.gif")

                        #puts the window in front of the menu
                        mainWindow.attributes('-topmost', True)
                        
                        #creates background
                        mainWindow["bg"] = "#FFFFFF"

                        
                        #does not allow window to be moved
                        mainWindow.overrideredirect(True)

                            
                        #does not allow it to be resized
                        mainWindow.resizable(width=False, height=False)
                        
                        #back to prev. window
                        def noclose():

                            #close window
                            mainWindow.destroy()
                            
                            #back to prev. window
                            menu()
                            

                        #resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                        #placing the button on the window
                        Button.pack(side='left', padx = 3, pady=0, anchor='s')
                        Button.image= backimagee
                        
                        #runing the window
                        center(mainWindow)
                        mainWindow.mainloop()

            #       -----------------------------------------------------
                        
                       
                    #overides close button
                    ASCIIartONwindowThatIsDecompressed.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    #puts the window in front of the menu
                    ASCIIartONwindowThatIsDecompressed.attributes('-topmost', True)
                    
                    #background colour
                    ASCIIartONwindowThatIsDecompressed["bg"] = "SteelBlue1"

                    #frame to show bg image
                    F1=Frame(ASCIIartONwindowThatIsDecompressed)
                    F1=Frame(ASCIIartONwindowThatIsDecompressed,width=400,height=450)
                    F1.place(height=7000, width=4000, x=100, y=100)

                    #places frame on the window
                    F1.grid(columnspan=10,rowspan=10)

                    #configures for window
                    F1.grid_rowconfigure(0,weight=1)
                    F1.grid_columnconfigure(0,weight=1)

                    #image for bg
                    photo=PhotoImage(file="HIYA.gif")
                    label = Label(ASCIIartONwindowThatIsDecompressed,image = photo)
                    
                    label.image = photo # keep a reference
                    label.grid(row=0,column=0,columnspan=20,rowspan=20)

                    #opens file
                    ReadFile = open("NewDeCompressedData.txt",'r')

                    #reads file
                    data = ReadFile.read()


                    #closes file
                    ReadFile.close()

                    #message widget to show art
                    artishere = tk.Message(ASCIIartONwindowThatIsDecompressed, text=data, font=('Consolas',13), fg = 'SteelBlue1', bg = '#FFFFFF',width = 90000)
                    artishere.grid(row=8,column=8)

                    #function to go back to menu
                    def backtomenu():

                        #closes window
                        ASCIIartONwindowThatIsDecompressed.destroy()

                        #runs the menu
                        menu()

                    #creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    #resizes background image
                    backimagee = backimage.subsample(3, 3)
                    Button = tk.Button(ASCIIartONwindowThatIsDecompressed, relief='flat', image=backimagee, command =backtomenu ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on window
                    Button.grid(row=10,column=8)
                    Button.image= backimagee


                        
            #       -----------------------------------------------------
                        
                    
                    #window size
                    ASCIIartONwindowThatIsDecompressed.geometry("724x592")
                    
                    #centers window
                    center(ASCIIartONwindowThatIsDecompressed)

                #runs the function above
                display()
                
                #------------------------------#
                
    #------------------------------#

                #title for window
        mainWindow.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            mainWindow.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)

    #       -----------------------------------------------------
            
                #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
            try:
                mainWindow.destroy()
            except:
                time.sleep(0)

            #create window
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

            #canvas placed on window
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')
            
            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            
            
            #window's icon
            try:
                WinDow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

            #can't resize window
            WinDow.resizable(width=False, height=False)
            
            #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #puts the window in front of the menu
            WinDow.attributes('-topmost', True)
            
            #creates background
            WinDow["bg"] = "#FFFFFF"

            #does not allow window to be moved
            WinDow.overrideredirect(True)

                
            #does not allow it to be resized
            WinDow.resizable(width=False, height=False)

            #back to prev. window
            def noclose():

                #close window
                WinDow.destroy()
                
                #back to prev. window
                Load_RLE_Window()
                

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #places button on window
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            #runs window
            center(WinDow)
            WinDow.mainloop()

    #       -----------------------------------------------------
            
           
        #overide close window
        mainWindow.protocol("WM_DELETE_WINDOW", on_closing)
        
        #puts the window in front of the others
        mainWindow.attributes('-topmost', True)
        
        #creates empty space between widgets
        emptyspace = Label(mainWindow, text=" ",bg="#FFFFFF")
        emptyspace.grid(sticky = tk.W)
        
        #text entry field
        imag = tk.PhotoImage(file="entry.gif")
        
        # create a frame and pack it
        frame2 = tk.Frame(mainWindow,bg='#FFFFFF',padx=15)
        frame2.grid()

        #subsample image
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')

        #places image
        s.grid(column = 2, row = 20)
        s.image = imagee

        #entry field
        e = integersOnly(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
        e.grid(column = 2, row = 20)
            
        # create a frame and pack it
        frame1 = tk.Frame(mainWindow,bg='#FFFFFF',padx=15)
        frame1.grid(sticky=tk.W)

        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()
        
        #creates enter rle button
        image = tk.PhotoImage(file="C.gif")
        
        #resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =parttwo ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")
        
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

            
        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='grey')
        emptyspace.grid()
        
        
        #function to exit the window and run the menu again
        def exitAndDoMenu():
            
            #destroys the window
            mainWindow.destroy()
            
            #loads the menu again
            menu()

    #       -----------------------------------------------------
                
       #creates enter button
        image = tk.PhotoImage(file="Back.gif")
        
        #resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =exitAndDoMenu ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")
        
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee
        
        #size of window
        mainWindow.geometry("750x592")
        
        #cant resize window
        mainWindow.resizable(width=False, height=False)
        
        #centers window
        center(mainWindow)

        
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    #error for there not being a file saved which is entered
    def errorNoFile():
        
        #creates window
        error=tk.Tk()
        
        #title for window
        error.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            error.iconbitmap('Icon_for_windows.ico')
        except:
            time.sleep(0)

#       -----------------------------------------------------
            
               
                    #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
            try:
                error.destroy()
            except:
                time.sleep(0)

            #creates window
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

            #creates a canvas to show bg image
            cv = tk.Canvas(width=w, height=h)
            cv.pack(side='top', fill='both', expand='yes')
            
            cv.create_image(0, 0, image=bg_image, anchor='nw')
            # add canvas text at coordinates x=15, y=20
            
            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            
            
            #window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

            #can't resize window
            mainWindow.resizable(width=False, height=False)
            
            #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #puts the window in front of the menu
            mainWindow.attributes('-topmost', True)
            
            #creates background
            mainWindow["bg"] = "#FFFFFF"

            
            #does not allow window to be moved
            mainWindow.overrideredirect(True)

                
            #does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

                
            
            
            #back to prev. window
            def noclose():

                #close window
                mainWindow.destroy()
                
                #back to prev. window
                errorNoFile()
                

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #shows button
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            #runs window
            center(mainWindow)
            mainWindow.mainloop()

#       -----------------------------------------------------
           
        #overides the close button
        error.protocol("WM_DELETE_WINDOW", on_closing)
        
        #puts the window in front of all others
        error.attributes('-topmost', True)
            
        #creates a frame to show bg image
        F1=Frame(error)
        F1=Frame(error,width=400,height=450)
        F1.place(height=7000, width=4000, x=100, y=100)
        

        #displays frame (transparent)
        F1.grid(columnspan=10,rowspan=10)

        #configured to fit on window
        F1.grid_rowconfigure(0,weight=1)
        F1.grid_columnconfigure(0,weight=1)

        #file for bg
        photo=PhotoImage(file="errorNoFile.gif")
        label = Label(error,image = photo)
        
        label.image = photo # keep a reference
        label.grid(row=0,column=0,columnspan=20,rowspan=20)

#     -----------------------------------------------------
        
        #returns the user to the menu
        def exit_the_error():
            
            #takes away the error window
            error.destroy()
            
            #shows the previous window again
            Convert_Rle()
            
#     -----------------------------------------------------            
         #creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        #resizes background image
        backimagee = backimage.subsample(4, 4)
        Button = tk.Button(error, relief='flat', image=backimagee, command =exit_the_error ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #showing button
        Button.grid(row = 17, column = 1)
        Button.image= backimagee
        
        #size of window
        error.geometry("724x592")
        
        #cant resize window
        error.resizable(width=False, height=False)
        
        #centers window
        center(error)
        
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


    #error for there not being a file saved which is entered
    def errorNoFileForConverter():
        
        #creates window
        error=tk.Tk()
        
        #title for window
        error.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            error.iconbitmap('Icon_for_windows.ico')
        except:
            time.sleep(0)

#     -----------------------------------------------------
            
            
                    #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
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
            
            #window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                #can't resize window
            mainWindow.resizable(width=False, height=False)
            #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #puts the window in front of the menu
            mainWindow.attributes('-topmost', True)
            
            #creates background
            mainWindow["bg"] = "#FFFFFF"

            
            #does not allow window to be moved
            mainWindow.overrideredirect(True)

                
            #does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

                
            
            
            #back to prev. window
            def noclose():

                #close window
                mainWindow.destroy()
                
                #back to prev. window
                errorNoFileForConverter()
                

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #showing button
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            center(mainWindow)
            mainWindow.mainloop()
            
#     -----------------------------------------------------
           
        #overides the close button
        error.protocol("WM_DELETE_WINDOW", on_closing)
        
        #puts the window in front of all others
        error.attributes('-topmost', True)
        
       #frame to show bg
        F1=Frame(error)
        F1=Frame(error,width=400,height=450)
        F1.place(height=7000, width=4000, x=100, y=100)
        

        #placing frame on window
        F1.grid(columnspan=10,rowspan=10)

        #configuring to be on top of image
        F1.grid_rowconfigure(0,weight=1)
        F1.grid_columnconfigure(0,weight=1)

        # file for bg
        photo=PhotoImage(file="errorNoFile.gif")
        label = Label(error,image = photo)
        
        label.image = photo # keep a reference
        label.grid(row=0,column=0,columnspan=20,rowspan=20)



#     -----------------------------------------------------
        
        #returns the user to the menu
        def exit_the_error():
            
            #takes away the error window
            error.destroy()
            
            #shows the previous window again
            Convert_ASCII()

#     -----------------------------------------------------
            
        #creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        #resizes background image
        backimagee = backimage.subsample(4, 4)
        Button = tk.Button(error, relief='flat', image=backimagee, command =exit_the_error ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #showing button
        Button.grid(row = 17, column = 1)
        Button.image= backimagee

        #size of window
        error.geometry("724x592")
        
        #cant resize window
        error.resizable(width=False, height=False)
        
        #centers window
        center(error)
        
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

        
    #error for there not being a file saved which is entered
    def errorNoFileForDisplayer():
        
        #creates window
        error=tk.Tk()
        
        #title for window
        error.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            error.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)

#       -----------------------------------------------------            
            
                    #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
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
            
            #window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                #can't resize window
            mainWindow.resizable(width=False, height=False)
            

            #puts the window in front of the menu
            mainWindow.attributes('-topmost', True)
            
            #creates background
            mainWindow["bg"] = "#FFFFFF"

            
            #does not allow window to be moved
            mainWindow.overrideredirect(True)

                
            #does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

                
            
            
            #back to prev. window
            def noclose():

                #close window
                mainWindow.destroy()
                
                #back to prev. window
                errorNoFileForDisplayer()
                
                #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #places button on window
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            #runs window
            center(mainWindow)
            mainWindow.mainloop()
#       -----------------------------------------------------            
            
           
        #overide close button
        error.protocol("WM_DELETE_WINDOW", on_closing)
        
        #puts the window in front of all others
        error.attributes('-topmost', True)

       #frame for window
        F1=Frame(error)
        F1=Frame(error,width=400,height=450)

        #places frame on window
        F1.place(height=7000, width=4000, x=100, y=100)
        F1.grid(columnspan=10,rowspan=10)

        #reconfiguring frame for window size
        F1.grid_rowconfigure(0,weight=1)
        F1.grid_columnconfigure(0,weight=1)

        #image for bg
        photo=PhotoImage(file="errorNoFile.gif")
        label = Label(error,image = photo)
        
        label.image = photo # keep a reference
        label.grid(row=0,column=0,columnspan=20,rowspan=20)



#       -----------------------------------------------------            
        
        #returns the user to the menu
        def exit_the_error():
            
            #takes away the error window
            error.destroy()
            
            #shows the previous window again    
            ASCII_ART_DISPLAYER()

#       -----------------------------------------------------            
            
        #creates enter rle button
        backimage = PhotoImage(file="Back.gif")

        #resizes background image
        backimagee = backimage.subsample(4, 4)
        Button = tk.Button(error, relief='flat', image=backimagee, command =exit_the_error ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #place image button
        Button.grid(row = 17, column = 1)
        Button.image= backimagee

        #size of window
        error.geometry("724x592")
        
        #cant resize window
        error.resizable(width=False, height=False)
        
        #centers window
        center(error)
        
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


        

#                                           #---------------------------------------------------------------#
#                                           |       function to create a new window for converting RLE      |
#                                           #---------------------------------------------------------------#


    def Convert_Rle():
        
        #creates window
        Convert_rle=tk.Tk()

        #canvas for bg image
        C = Canvas(Convert_rle)
        backg = PhotoImage(file = "CtR.gif")

        #placing canvas
        background_label = Label(Convert_rle, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #reference
        C.grid()
        C.img = backg
 
        #title for window
        Convert_rle.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            Convert_rle.iconbitmap('Icon_for_windows.ico')
        except:
            time.sleep(0)

    #       -----------------------------------------------------            
            
        
                    #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
            try:
                Convert_rle.destroy()
            except:
                time.sleep(0)

            #creating window
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

            #placing canvas on window
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')
            
            
            # anchor='nw' implies upper left corner coordinates
            
            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            # now add some button widgets
            #window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                #can't resize window
            mainWindow.resizable(width=False, height=False)
            
            #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #puts the window in front of the menu
            mainWindow.attributes('-topmost', True)
            
            #creates background
            mainWindow["bg"] = "#FFFFFF"

            
            #does not allow window to be moved
            mainWindow.overrideredirect(True)

                
            #does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

                
            
            
            #back to prev. window
            def noclose():

                #close window
                mainWindow.destroy()
                
                #back to prev. window
                Convert_Rle()
                

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #places button on the window
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            #runs the window
            center(mainWindow)
            mainWindow.mainloop()

    #       -----------------------------------------------------            
            
           
        #overides close button
        Convert_rle.protocol("WM_DELETE_WINDOW", on_closing)
        
        #puts the window in front of the others
        Convert_rle.attributes('-topmost', True)
        
        #background colour of window
        Convert_rle["bg"] = "SteelBlue1"


        #creates empty space between widgets
        emptyspace = Label(Convert_rle, text=" ",bg="#FFFFFF")
        emptyspace.grid(sticky = tk.W)
        
        #text entry field
        imag = tk.PhotoImage(file="entry.gif")
        
        # create a frame and pack it
        frame2 = tk.Frame(Convert_rle,bg='#FFFFFF',padx=15)
        frame2.grid()

        #sizing image to window size
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')

        #reference
        s.grid(column = 2, row = 5)
        s.image = imagee

        #entry field
        Convert_rle.entry = tk.Entry(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
        Convert_rle.entry.grid(column = 2, row = 5)
          

    #       -----------------------------------------------------            
        
        #function to compress the data
        def CompressData():
        
        #adds file extension if there isnt one already
            if Convert_rle.entry.get().lower().endswith(('.txt')):

                #gets the end file name
                enterredfilename = Convert_rle.entry.get()

                #if trheree is not already a file extension...
            else:

                #a file extrension is added
                enterredfilename = Convert_rle.entry.get()+'.txt'
            
            #Checks if the file exists
            if os.path.exists(enterredfilename) == True:
                
                #saves the text in entry field to a variable
                file = enterredfilename

                #name of new file
                textfile = "NewEncodedData.txt"
                
                #opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
                open(textfile,"w+").close()
                
                #opens file
                openfile=open(file)

    #       -----------------------------------------------------            
                
                #creates a while loop so that i can check every line one at a time
                while True:
                    
                    #reads the line
                    line = openfile.readline()
                    
                    #takes away the part that would indicate a new line so that it can be decoded
                    decoded_string = line.replace("\n","")
                    
                    #string to be encoded
                    string = decoded_string
                    
                    #importing time for exception errors
                    import time
                    
                    #duplicating the variable so that i have 2 of the same thing
                    word=string
                    
                    #checking consecutive characters repeating
                    count=1
                    
                    #variable to store the final value after counting
                    length=""

    #       -----------------------------------------------------            
                    
                    #check the length of occurence
                    if len(word)>1:
                        
                        #loop for every character
                        for i in range(1,len(word)):


    #       -----------------------------------------------------            
                            
                            #check if the one after is the same
                           if word[i-1]==word[i]:
                               
                               #if so, add one to the counting variable
                              count+=1


    #       -----------------------------------------------------            
                              
                              #if not...
                           else :
                               
                               #write to the final variable (uses ':' to seperate occurence to character being repeated)
                               length += str(count)+":"+word[i-1]+":"
                               
                               #changing the count variable
                               count=1
                               
                               #write to the final variable (uses ':' to seperate occurence to character being repeated)
                        length += (""+str(count)+":"+word[i]+":")
                        
                        #if not...
                    else:

    #       -----------------------------------------------------            
                        
                        #change the item
                        i=0
                        
                        try:
                            #write to the final variable (uses ':' to seperate occurence to character being repeated)
                            length += (""+str(count)+":"+word[i]+":")
                            
                        except:
                            #I use sleep for 0 seconds because it practically makes the program  do nothing
                            time.sleep(0)

    #       -----------------------------------------------------            
                            
                    #creating another copy
                    same_one= length
                    
                    #taking out the colons and making sublists in list
                    New_String = same_one.split(":")
                    
                    #math used to make every first item in the sublist of length 2 (so if the sublist is [5,5], it will allow me to turn it into [05,5])
                    import math
                    
                    #actually doing what was described above
                    New_String = [New_String[2*i:2*i+2] for i in range(0,math.ceil(len(New_String)/2))]
                    
                    #writing to a new list (to make the end result clean)
                    Idea = []

    #       -----------------------------------------------------            
                    
                    #this method allows me to not need to remove the last sublist as it only has one argument instead of two (and this part looks for 2)
                    try:
                        
                        #checks for the first and second items in sublist
                        for start, end in New_String:

    #       -----------------------------------------------------            
                            
                            #checks length of the first item in sublist
                            if len(start) == 1:
                                
                                #adds 0 to the start of single digit numbers
                                start = '0'+start
                                
                                #adds the changed item to the new list
                                Idea.append(start)
                                
                                #adds the character being repeated to the new list
                                Idea.append(end)
                                #if not...

    #       -----------------------------------------------------            
                                
                            else:
                                ##adds the number of consective occurences to the new list
                                Idea.append(start)
                                
                                #adds the character being repeated to the new list
                                Idea.append(end)
                                #if there is not enough arguments...

    #       -----------------------------------------------------            
                                
                    except:
                        #wait 0 seconds (skips the last sublist and continues with the rest program)
                        time.sleep(0)

    #       -----------------------------------------------------            
                        
                    #making the list into a string without any annoying commas or square brackets
                    makeitastring = ''.join(map(str, Idea))
                    
                    #adds the new line indicator to the compressed data so that it can be saved correctly to the new file
                    encoded_string_with_new_line = makeitastring + "\n"
                    
                    #writes to the file
                    WriteToFile = open(textfile,"a")
                    
                    #writes the data to the file
                    WriteToFile.write(encoded_string_with_new_line)
                    
                    #closes the file
                    WriteToFile.close

    #       -----------------------------------------------------            
                    
                    #if there is not another line:
                    if len(line)<1:
                        
                        #ends loop
                        break

    #       -----------------------------------------------------            
                    
                #closes the file
                openfile.close()
                
                #opens old file
                with open(file) as f:
                    
                    #reads all parts of file for each line
                    text = f.read().splitlines()
                    
                    #reads the amount of lines in the file
                lines = len(text)
                
                #reads the amount of words in the file
                words = sum(len(line.split())for line in text)
                
                #uses the previous 2 variables to work out the character count of the file
                characters_in_original = sum(len(line)for line in text)


    #       -----------------------------------------------------            
                
                #opens new file
                with open(textfile) as f:
                    
                    #reads all parts of file for each line
                    text = f.read().splitlines()

    #       -----------------------------------------------------            
                    
                    #reads the amount of words in the file
                lines = len(text)
                
                #reads the amount of words in the file
                words = sum(len(line.split())for line in text)
                
                #uses the previous 2 variables to work out the character count of the file
                characters_in_new = sum(len(line)for line in text)
                
                #calculates the difference in characters
                difference = characters_in_original - characters_in_new
                
                #makes the difference a string so it can be concatenated with other strings
                difference = str(difference)
                
                #takes away the window
                Convert_rle.destroy()

    #       -----------------------------------------------------            
                
                #function to show the results of the compression
                def show_results():
                    
                    #creates the window
                    result = tk.Tk()

                    
                    #title for window
                    result.title("ASCII art program by Faeq ")
                    
                    #icon for window
                    try:
                        result.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)

    #       -----------------------------------------------------            
                                #function to not allow program to end before any processes are complete

                    def on_closing():
                        
                        #close window
                        try:
                            result.destroy()
                        except:
                            time.sleep(0)

                        #creates a window
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

                        #canvas to use bg image
                        cv.pack(side='top', fill='both', expand='yes')
                        cv.create_image(0, 0, image=bg_image, anchor='nw')
                        
                        # anchor='nw' implies upper left corner coordinates
                        cv.create_text(15, 20, text="", fill="red", anchor='nw')
                        
                        #window's icon
                        try:
                            mainWindow.iconbitmap('Icon_for_windows.ico')
                        except:
                            time.sleep(0)

                            #can't resize window
                        mainWindow.resizable(width=False, height=False)
                        
                        #creates enter rle button
                        backimage = tk.PhotoImage(file="Back.gif")

                        #puts the window in front of the menu
                        mainWindow.attributes('-topmost', True)
                        
                        #creates background
                        mainWindow["bg"] = "#FFFFFF"

                        
                        #does not allow window to be moved
                        mainWindow.overrideredirect(True)

                            
                        #does not allow it to be resized
                        mainWindow.resizable(width=False, height=False)

                            
                        
                        
                        #back to prev. window
                        def noclose():

                            #close window
                            mainWindow.destroy()
                            
                            #back to prev. window
                            show_results()
                            

                        #resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                        #places the button on the window
                        Button.pack(side='left', padx = 3, pady=0, anchor='s')
                        Button.image= backimagee

                        #runs the window
                        center(mainWindow)
                        mainWindow.mainloop()

    #       -----------------------------------------------------            
                        
                       
                    #overides close button
                    result.protocol("WM_DELETE_WINDOW", on_closing)

                    #puts the window in front of the others
                    result.attributes('-topmost', True)
                    
                    #background for window
                    result["bg"] = "SteelBlue1"

                    #frame for bg image
                    F1=Frame(result)
                    F1=Frame(result,width=400,height=450)

                    #places the frame on the window
                    F1.place(height=7000, width=4000, x=100, y=100)
                    F1.config()

                    #configures size of frame
                    F1.grid(columnspan=10,rowspan=10)
                    F1.grid_rowconfigure(0,weight=1)
                    F1.grid_columnconfigure(0,weight=1)

                    #bg image
                    photo=PhotoImage(file="Results.gif")
                    label = Label(result,image = photo)
                    
                    label.image = photo # keep a reference
                    label.grid(row=0,column=0,columnspan=20,rowspan=20)

                    #concatenates the strings together
                    text_to_show = str(characters_in_original)

                    #number of characters in the old file
                    ResulT = Label(result, text=text_to_show,bg="#FFFFFF",font=("Consolas",15),fg="SteelBlue1")
                    ResulT.grid(sticky = tk.W, row = 5, padx = 150)
                    
                    #concatenates the strings together
                    text_to_show = str(characters_in_new)
                    
                    #number of characters in the new file
                    ResulT = Label(result, text=text_to_show,bg="#FFFFFF",font=("Consolas",20),fg="SteelBlue1")
                    ResulT.grid(sticky = tk.W, row = 8, padx = 30)
                    
                    #concatenates the strings together
                    text_to_show = str(difference)
                    
                    #shows difference in characters
                    ResulT = Label(result, text=text_to_show,bg="#FFFFFF",font=("Consolas",20),fg="SteelBlue1")
                    ResulT.grid(sticky = tk.W, row = 15, padx = 30)

    #       -----------------------------------------------------            
                    
                    #ends this part of the program
                    def end_this_part():
                        
                        #takes away the window
                        result.destroy()
                        
                        #shows the menu again
                        menu()

    #       -----------------------------------------------------            
                              

                    #creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    #resizes background image
                    backimagee = backimage.subsample(5, 5)
                    Button = tk.Button(result, relief='flat', image=backimagee, command =end_this_part ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on the window
                    Button.grid(row=19)
                    Button.image= backimagee
                    
                    #size of window
                    result.geometry("775x592")
                    
                    #can't resize window
                    result.resizable(width=False, height=False)
                    
                    #centers window
                    center(result)
                    
                    #runs the function
                    
                show_results()
                #what will happen if the file does not exist
                
            else:

                #closes the window
                Convert_rle.destroy()
                
                #runs the error function
                errorNoFile()

    #       -----------------------------------------------------            
                
        def CcompressData():

            #gets the file name from the file dialog
            file = Convert_rle.filename
            
            #name of new file
            textfile = "NewEncodedData.txt"
            
            #opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
            open(textfile,"w+").close()
            
            #opens file
            openfile=open(file)


    #       -----------------------------------------------------            
            
            #creates a while loop so that i can check every line one at a time
            while True:
                
                #reads the line
                line = openfile.readline()
                
                #takes away the part that would indicate a new line so that it can be decoded
                decoded_string = line.replace("\n","")
                
                #string to be encoded
                string = decoded_string
                
                #importing time for exception errors
                import time
                
                #duplicating the variable so that i have 2 of the same thing
                word=string
                
                #checking consecutive characters repeating
                count=1
                
                #variable to store the final value after counting
                length=""

    #       -----------------------------------------------------            
                
                #check the length of occurence
                if len(word)>1:
                    
                    #loop for every character
                    for i in range(1,len(word)):
                        
                        #check if the one after is the same
                       if word[i-1]==word[i]:
                           
                           #if so, add one to the counting variable
                          count+=1
                          
                          #if not...
                       else :
                           
                           #write to the final variable (uses ':' to seperate occurence to character being repeated)
                           length += str(count)+":"+word[i-1]+":"
                           
                           #changing the count variable
                           count=1
                           
                           #write to the final variable (uses ':' to seperate occurence to character being repeated)
                    length += (""+str(count)+":"+word[i]+":")
                    
                    #if not...
                else:

    #       -----------------------------------------------------            
                    
                    #change the item
                    i=0
                    try:
                        
                        #write to the final variable (uses ':' to seperate occurence to character being repeated)
                        length += (""+str(count)+":"+word[i]+":")
                        
                    except:
                        #I use sleep for 0 seconds because it practically makes the program  do nothing
                        time.sleep(0)


                        #       -----------------------------------------------------            
                        
                #creating another copy
                same_one= length
                
                #taking out the colons and making sublists in list
                New_String = same_one.split(":")
                
                #math used to make every first item in the sublist of length 2 (so if the sublist is [5,5], it will allow me to turn it into [05,5])
                import math
                
                #actually doing what was described above
                New_String = [New_String[2*i:2*i+2] for i in range(0,math.ceil(len(New_String)/2))]
                
                #writing to a new list (to make the end result clean)
                Idea = []

    #       -----------------------------------------------------            
                
                #this method allows me to not need to remove the last sublist as it only has one argument instead of two (and this part looks for 2)
                try:
                    
                    #checks for the first and second items in sublist
                    for start, end in New_String:

    #       -----------------------------------------------------            
                        
                        
                        #checks length of the first item in sublist
                        if len(start) == 1:
                            
                            #adds 0 to the start of single digit numbers
                            start = '0'+start
                            
                            #adds the changed item to the new list
                            Idea.append(start)
                            
                            #adds the character being repeated to the new list
                            Idea.append(end)

    #       -----------------------------------------------------            
                            
                            
                            #if not...
                        else:
                            
                            ##adds the number of consective occurences to the new list
                            Idea.append(start)
                            
                            #adds the character being repeated to the new list
                            Idea.append(end)
                            
                            #if there is not enough arguments...

    #       -----------------------------------------------------            
                            
                except:
                    #wait 0 seconds (skips the last sublist and continues with the rest program)
                    time.sleep(0)
                    
                #making the list into a string without any annoying commas or square brackets
                makeitastring = ''.join(map(str, Idea))
                
                #adds the new line indicator to the compressed data so that it can be saved correctly to the new file
                encoded_string_with_new_line = makeitastring + "\n"
                
                #writes to the file
                WriteToFile = open(textfile,"a")
                
                #writes the data to the file
                WriteToFile.write(encoded_string_with_new_line)
                
                #closes the file
                WriteToFile.close

    #       -----------------------------------------------------            
                
                #if there is not another line:
                if not line:
                    
                    #ends loop
                    break


                #       -----------------------------------------------------            
                
            #closes the file
            openfile.close()
            
            #opens old file
            with open(file) as f:
                
                #reads all parts of file for each line
                text = f.read().splitlines()
                
                #reads the amount of lines in the file
            lines = len(text)
            
            #reads the amount of words in the file
            words = sum(len(line.split())for line in text)
            
            #uses the previous 2 variables to work out the character count of the file
            characters_in_original = sum(len(line)for line in text)

    #       -----------------------------------------------------            
            
            
            #opens new file
            with open(textfile) as f:
                
                #reads all parts of file for each line
                text = f.read().splitlines()
                
                #reads the amount of words in the file

    #       -----------------------------------------------------            
                
            lines = len(text)
            
            #reads the amount of words in the file
            words = sum(len(line.split())for line in text)
            
            #uses the previous 2 variables to work out the character count of the file
            characters_in_new = sum(len(line)for line in text)
            
            #calculates the difference in characters
            difference = characters_in_original - characters_in_new
            
            #makes the difference a string so it can be concatenated with other strings
            difference = str(difference)
            
            #takes away the window
            Convert_rle.destroy()

    #       -----------------------------------------------------            
            
            #function to show the results of the compression
            def show_results():
            
                #creates the window
                result = tk.Tk()

                
                #title for window
                result.title("ASCII art program by Faeq ")
                
                #icon for window
                try:
                    result.iconbitmap('Icon_for_windows.ico')
                    
                except:
                    time.sleep(0)

        #       -----------------------------------------------------            
                            #function to not allow program to end before any processes are complete

                def on_closing():
                    
                    #close window
                    try:
                        result.destroy()
                    except:
                        time.sleep(0)
                        
                    #creates a window
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

                    #canvas for bg image
                    cv.pack(side='top', fill='both', expand='yes')
                    cv.create_image(0, 0, image=bg_image, anchor='nw')
                    
                    
                    # anchor='nw' implies upper left corner coordinates
                    cv.create_text(15, 20, text="", fill="red", anchor='nw')
                    
                    
                    #window's icon
                    try:
                        mainWindow.iconbitmap('Icon_for_windows.ico')
                    except:
                        time.sleep(0)

                        #can't resize window
                    mainWindow.resizable(width=False, height=False)
                    
                    #creates enter rle button
                    backimage = tk.PhotoImage(file="Back.gif")

                    #puts the window in front of the menu
                    mainWindow.attributes('-topmost', True)
                    
                    #creates background
                    mainWindow["bg"] = "#FFFFFF"

                    
                    #does not allow window to be moved
                    mainWindow.overrideredirect(True)

                        
                    #does not allow it to be resized
                    mainWindow.resizable(width=False, height=False)

                    #back to prev. window
                    def noclose():

                        #close window
                        mainWindow.destroy()
                        
                        #back to prev. window
                        show_results()
                        

                    #resizes background image
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on window
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')
                    Button.image= backimagee

                    #runs window
                    center(mainWindow)
                    mainWindow.mainloop()

        #       -----------------------------------------------------            
                    
                   
                #overides close button
                result.protocol("WM_DELETE_WINDOW", on_closing)

                #puts the window in front of the others
                result.attributes('-topmost', True)
                
                #background for window
                result["bg"] = "SteelBlue1"

                #frame for bg image
                F1=Frame(result)
                F1=Frame(result,width=400,height=450)
                F1.place(height=7000, width=4000, x=100, y=100)

                
                #configures the frame
                F1.grid(columnspan=10,rowspan=10)
                F1.grid_rowconfigure(0,weight=1)
                F1.grid_columnconfigure(0,weight=1)

                #bg image
                photo=PhotoImage(file="Results.gif")
                label = Label(result,image = photo)
                
                label.image = photo # keep a reference
                label.grid(row=0,column=0,columnspan=20,rowspan=20)

                
                #concatenates the strings together
                text_to_show = str(characters_in_original)

                #number of characters in the old file
                ResulT = Label(result, text=text_to_show,bg="#FFFFFF",font=("Consolas",15),fg="SteelBlue1")
                ResulT.grid(sticky = tk.W, row = 5, padx = 150)
                
                #concatenates the strings together
                text_to_show = str(characters_in_new)
                
                #number of characters in the new file
                ResulT = Label(result, text=text_to_show,bg="#FFFFFF",font=("Consolas",20),fg="SteelBlue1")
                ResulT.grid(sticky = tk.W, row = 8, padx = 30)
                
                #concatenates the strings together
                text_to_show = str(difference)
                
                #shows difference in characters
                ResulT = Label(result, text=text_to_show,bg="#FFFFFF",font=("Consolas",20),fg="SteelBlue1")
                ResulT.grid(sticky = tk.W, row = 15, padx = 30)

        #       -----------------------------------------------------            
                
                #ends this part of the program
                def end_this_part():
                    
                    #takes away the window
                    result.destroy()
                    
                    #shows the menu again
                    menu()

        #       -----------------------------------------------------            
                          

                #creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                #resizes background image
                backimagee = backimage.subsample(5, 5)
                Button = tk.Button(result, relief='flat', image=backimagee, command =end_this_part ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                #places button on bg
                Button.grid(row=19)
                Button.image= backimagee
                
                #size of window
                result.geometry("775x592")
                    
                #can't resize window
                result.resizable(width=False, height=False)
                
                #centers window
                center(result)
                
                #runs the function
            show_results()

    #       -----------------------------------------------------            
            

    #       -----------------------------------------------------

         
        # create a frame and pack it
        frame1 = tk.Frame(Convert_rle,bg='#FFFFFF',padx=15)
        frame1.grid(sticky=tk.W)

        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()
        
        #creates enter rle button
        image = tk.PhotoImage(file="C.gif")
        
        #resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =CompressData,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")
        
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        #importing filedialog in local scope to make function work
        try:
            from tkinter import filedialog
            #python 2 is below
        except:
            from Tkinter import tkFileDialog

            #function to browse for file
        def browse():
            
            #opens file dialog and lets user to browse for file
            Convert_rle.filename =  filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
            
            # asigns the file location to the variable
            file = Convert_rle.filename
            
            #runs the function to load the art through the browse function
            CcompressData()

    #       -----------------------------------------------------            
        
        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()

        #creates enter button
        image = tk.PhotoImage(file="BfF.gif")
        
        #resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =browse,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='grey')
        emptyspace.grid()

    #       -----------------------------------------------------            
        
        #function to exit the window
        def exit_rle_converter():
            
            #takes away the window
            Convert_rle.destroy()
            
            #displays the menu again
            menu()

    #       -----------------------------------------------------            
        
       #creates enter button
        image = tk.PhotoImage(file="Back.gif")
        
        #resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =exit_rle_converter,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee
        
        #size of window
        Convert_rle.geometry("724x592")
        
        #can't resize window
        Convert_rle.resizable(width=False, height=False)
        
        #centers window
        center(Convert_rle)


 #    ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


    #                                           #-----------------------------------------------------------------------#
    #                                           |       function to create a new window for converting ascii art        |
    #                                           #-----------------------------------------------------------------------#

    def Convert_ASCII():
        
        #creates window
        ASCII_Converter=tk.Tk()

        #canvas for bg
        C = Canvas(ASCII_Converter)
        backg = PhotoImage(file = "CtAAa.gif")

        #places image on canvas
        background_label = Label(ASCII_Converter, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #reference
        C.grid()
        C.img = backg
        
        #title for window
        ASCII_Converter.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            ASCII_Converter.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)

    #       -----------------------------------------------------            
            
        #function to not allow program to end before any processes are complete
                    #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
            try:
                ASCII_Converter.destroy()
            except:
                time.sleep(0)

            #creates window
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

            #canvas for bg image
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')
            
            
            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            
            
            #window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                #can't resize window
            mainWindow.resizable(width=False, height=False)
            #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #puts the window in front of the menu
            mainWindow.attributes('-topmost', True)
            
            #creates background
            mainWindow["bg"] = "#FFFFFF"

            
            #does not allow window to be moved
            mainWindow.overrideredirect(True)

                
            #does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

            #back to prev. window
            def noclose():

                #close window
                mainWindow.destroy()
                
                #back to prev. window
                Convert_ASCII()
                

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #plces button on bg
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            #runs window
            center(mainWindow)
            mainWindow.mainloop()

    #       -----------------------------------------------------            
           
        #overide close button
        ASCII_Converter.protocol("WM_DELETE_WINDOW", on_closing)

        #puts the window in front of the others
        ASCII_Converter.attributes('-topmost', True)
        
        #background colour
        ASCII_Converter["bg"] = "SteelBlue1"
        
        #creates empty space between widgets
        emptyspace = Label(ASCII_Converter, text=" ",bg="#FFFFFF")
        emptyspace.grid(sticky = tk.W)
        
        #text entry field
        imag = tk.PhotoImage(file="entry.gif")
        
        # create a frame and pack it
        frame2 = tk.Frame(ASCII_Converter,bg='#FFFFFF',padx=15)
        frame2.grid()

        #resiuzes bg for canvas
        imagee = imag.subsample(3, 3)
        s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')

        #reference
        s.grid(column = 2, row = 5)
        s.image = imagee

        #entry field
        ASCII_Converter.entry = tk.Entry(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')
        ASCII_Converter.entry.grid(column = 2, row = 5)
          

    #       -----------------------------------------------------            
        
        #function to load and decode the data
        def load_data():
            
        #adds file extension if there isnt one already
            if ASCII_Converter.entry.get().lower().endswith(('.txt')):
                
                enterredfilename = ASCII_Converter.entry.get()
            else:
                
                enterredfilename = ASCII_Converter.entry.get()+'.txt'
            
            #Checks if the file exists
            if os.path.exists(enterredfilename) == True:
                
                #saves the text in entry field to a variable
                filename = enterredfilename
                
                #adds file extension to name of file so it can open
                file=enterredfilename
                
                #name of new file
                textfile = "NewDecodedArt.txt"
                
                #opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
                open(textfile,"w").close()
                
                #opens file
                openfile=open(file)

    #       -----------------------------------------------------            
                
                #creates a while loop so that i can check every line one at a time
                while True:
                    
                    #reads the line
                    line = openfile.readline()
                    
                    #takes away the part that would indicate a new line so that it can be decoded
                    encoded_string = line.replace("\n","")
                    
                    #the string to be decoded
                    string = encoded_string

    #       -----------------------------------------------------            
                    

                    #function to split string into list
                    def split(str, num):
                        return [ str[start:start+num] for start in range(0, len(str), num) ]

    #       -----------------------------------------------------            
                    
                    #splitting string into packets of 3
                    splitUpStringwiththree = split(string,3)
                    
                    #creating a new list to write to later
                    new_string = []
                    
                    #spliting the string again but this time in packets of 2
                    splitUpStringg = split(string,2)
                    
                    #loop to split the splitted string into a list with items of length 1
                    for item in splitUpStringwiththree:
                        
                        #splitting into packets
                        r = split(item,1)
                        
                        #saving to our new list made up of strings
                        new_string = new_string+r
                        
                    #another new list we will write to later
                    splitUpStringg = []
                    
                    #loop to split the list into the reoccurences of the characters without the actual character
                    for i in splitUpStringwiththree:
                        
                        #splitting into packets
                        rrt = split(i,2)
                        
                        #saving to our new list
                        splitUpStringg = splitUpStringg+rrt
                        
                    #assigning our old list to a new variable so that we have a copy of the list to refer to when the original is already in use
                    v = new_string

                    #deleting the third character in every item
                    k = 3
                    
                    #actually deleting the character
                    del new_string[k-1::k]
                    
                    #joining the characters for the number of occurences together
                    mmm = [''.join(x) for x in zip(new_string[0::2], new_string[1::2])]

    #       -----------------------------------------------------            
                    
                    #replacing the 0 in any integer representing the number of occurrences
                    for w in mmm:
                        if w[0] == '0':
                            w.replace('0', '')

    #       -----------------------------------------------------            
                    
                    #turning every item in the list into a integer
                    mmm = list(map(int, mmm))

                    #loop to get rid of unwanted items in the list for occurences
                    for i in splitUpStringg:
                        
                        #checking if the length is equal to 2 (if so, this shows the number of occurences)
                        if len(i)==2:
                            
                            #finding the index of the item in its list
                            lop = splitUpStringg.index(i)
                            
                            #getting rid of the item using its index previously found
                            splitUpStringg.pop(lop)
                            
                    #loop to multiply the numbver to be shown by its actual bnumber of occurences
                    decodedString = [item for item, count in zip(splitUpStringg, mmm) for i in range(count)]

                    #making the list into a string without annoying commas or square brackets that should not be there
                    makeitastring = ''.join(map(str, decodedString))

                    #adds the \n so that the next line can be put in when the loop goes again
                    decoded_string_with_new_line = makeitastring + "\n"
                    
                    #creates and writes to a new file
                    WriteToFile = open(textfile,"a")

                    
                    #writes the data to the file
                    WriteToFile.write(decoded_string_with_new_line)
                    WriteToFile.close

                    
                    #if there is not another line:
                    if not line:
                        
                        #ends loop
                        break

                    
                #closes the file
                openfile.close()
                
                #opens file
                ReadFile = open(textfile,'r')
                
                #reads file
                data = ReadFile.read()
                
                #closes file
                ReadFile.close()

                
                #creates a new window
                def WindowToDisplayArt():
                    try:
                        ASCII_Converter.destroy()
                    except:
                        time.sleep(0)
                    
                    #opens text in window
                    ASCIIartONwindow = Tk()
                    
                    #title for window
                    ASCIIartONwindow.title("ASCII art program by Faeq ")
                    
                    #icon for window
                    try:
                        ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)

    #       -----------------------------------------------------
                                
                      #function to not allow program to end before any processes are complete

                    def on_closing():
                        
                        #close window
                        try:
                            ASCIIartONwindow.destroy()
                        except:
                            time.sleep(0)

                        #creates window
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

                        #canvas for bg image
                        cv.pack(side='top', fill='both', expand='yes')
                        cv.create_image(0, 0, image=bg_image, anchor='nw')
                        
                        # anchor='nw' implies upper left corner coordinates
                        cv.create_text(15, 20, text="", fill="red", anchor='nw')
                        
                        #window's icon
                        try:
                            mainWindow.iconbitmap('Icon_for_windows.ico')
                        except:
                            time.sleep(0)

                            #can't resize window
                        mainWindow.resizable(width=False, height=False)
                        #creates enter rle button
                        backimage = tk.PhotoImage(file="Back.gif")

                        #puts the window in front of the menu
                        mainWindow.attributes('-topmost', True)
                        
                        #creates background
                        mainWindow["bg"] = "#FFFFFF"

                        
                        #does not allow window to be moved
                        mainWindow.overrideredirect(True)

                            
                        #does not allow it to be resized
                        mainWindow.resizable(width=False, height=False)

                        
                        #back to prev. window
                        def noclose():

                            #close window
                            mainWindow.destroy()
                            
                            #back to prev. window
                            WindowToDisplayArt()
                            

                        #resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                        #places button on bg
                        Button.pack(side='left', padx = 3, pady=0, anchor='s')
                        Button.image= backimagee

                        #runs window
                        center(mainWindow)
                        mainWindow.mainloop()
                       
                    #overide close button
                    ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    #puts the window in front of the others
                    ASCIIartONwindow.attributes('-topmost', True)
                    
                    #background colour
                    ASCIIartONwindow["bg"] = "SteelBlue1"
                    
                    #frame for bg
                    F1=Frame(ASCIIartONwindow)
                    F1=Frame(ASCIIartONwindow,width=400,height=450)
                    F1.place(height=7000, width=4000, x=100, y=100)

                    #configuring frame to size
                    F1.grid(columnspan=10,rowspan=10)
                    F1.grid_rowconfigure(0,weight=1)
                    F1.grid_columnconfigure(0,weight=1)

                    #bg image
                    photo=PhotoImage(file="HIYA.gif")
                    label = Label(ASCIIartONwindow,image = photo)
                    
                    label.image = photo # keep a reference!
                    label.grid(row=0,column=0,columnspan=20,rowspan=20)


                    #opens file
                    ReadFile = open(textfile,'r')

                    #reads file
                    data = ReadFile.read()


                    #closes file
                    ReadFile.close()
                    artishere = tk.Message(ASCIIartONwindow, text=data, font=('Consolas',13), fg = 'SteelBlue1', bg = '#FFFFFF',width = 90000)
                    artishere.grid(row=8,column=8)

                    #function to get mack to the menu
                    def backtomenu():
                        ASCIIartONwindow.destroy()
                        menu()

                    #creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    #resizes background image
                    backimagee = backimage.subsample(3, 3)
                    Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee, command =backtomenu ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on bg
                    Button.grid(row=10,column=8)
                    Button.image= backimagee

                    #window size
                    ASCIIartONwindow.geometry("724x592")
                    
                    #centers window
                    center(ASCIIartONwindow)
                    
                WindowToDisplayArt()

    #       -----------------------------------------------------
                
                #if the file does not exist:
            else:
                
                #closes window
                ASCII_Converter.destroy()
                
                #runs the error
                errorNoFileForConverter()

    #       -----------------------------------------------------
                
        def Load_data():

            #gets file name from file dilog
            file = ASCII_Converter.filename
            
            #name of new file
            textfile = "NewDecodedArt.txt"
            
            #opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
            open(textfile,"w").close()
            
            #opens file
            openfile=open(file)

    #       -----------------------------------------------------
            
            #creates a while loop so that i can check every line one at a time
            while True:
                
                #reads the line
                line = openfile.readline()
                
                #takes away the part that would indicate a new line so that it can be decoded
                encoded_string = line.replace("\n","")
                
                #the string to be decoded
                string = encoded_string

    #       -----------------------------------------------------

                #function to split string into list
                def split(str, num):
                    return [ str[start:start+num] for start in range(0, len(str), num) ]

    #       -----------------------------------------------------
                
                #splitting string into packets of 3
                splitUpStringwiththree = split(string,3)
                
                #creating a new list to write to later
                new_string = []
                
                #spliting the string again but this time in packets of 2
                splitUpStringg = split(string,2)
                
                #loop to split the splitted string into a list with items of length 1
                for item in splitUpStringwiththree:
                    
                    #splitting into packets
                    r = split(item,1)
                    
                    #saving to our new list made up of strings
                    new_string = new_string+r
                    
                #another new list we will write to later
                splitUpStringg = []
                
                #loop to split the list into the reoccurences of the characters without the actual character
                for i in splitUpStringwiththree:
                    
                    #splitting into packets
                    rrt = split(i,2)
                    
                    #saving to our new list
                    splitUpStringg = splitUpStringg+rrt
                    
                #assigning our old list to a new variable so that we have a copy of the list to refer to when the original is already in use
                v = new_string

                #deleting the third character in every item
                k = 3
                
                #actually deleting the character
                del new_string[k-1::k]
                
                #joining the characters for the number of occurences together
                mmm = [''.join(x) for x in zip(new_string[0::2], new_string[1::2])]

    #       -----------------------------------------------------
                
                #replacing the 0 in any integer representing the number of occurrences
                for w in mmm:
                    if w[0] == '0':
                        w.replace('0', '')

    #       -----------------------------------------------------
                
                #turning every item in the list into a integer
                mmm = list(map(int, mmm))

                #loop to get rid of unwanted items in the list for occurences
                for i in splitUpStringg:
                    
                    #checking if the length is equal to 2 (if so, this shows the number of occurences)
                    if len(i)==2:
                        
                        #finding the index of the item in its list
                        lop = splitUpStringg.index(i)
                        
                        #getting rid of the item using its index previously found
                        splitUpStringg.pop(lop)
                        
                #loop to multiply the numbver to be shown by its actual bnumber of occurences
                decodedString = [item for item, count in zip(splitUpStringg, mmm) for i in range(count)]

                #making the list into a string without annoying commas or square brackets that should not be there
                makeitastring = ''.join(map(str, decodedString))
                
                #adds the \n so that the next line can be put in when the loop goes again
                decoded_string_with_new_line = makeitastring + "\n"
                
                #creates and writes to a new file
                WriteToFile = open(textfile,"a")
                
                #writes the data to the file
                WriteToFile.write(decoded_string_with_new_line)
                WriteToFile.close
                
                #if there is not another line:
                if not line:
                    
                    #ends loop
                    break

    #       -----------------------------------------------------
                
            #closes the file
            openfile.close()
            
            #opens file
            ReadFile = open(textfile,'r')
            
            #reads file
            data = ReadFile.read()
            
            #closes file
            ReadFile.close()
            
            #creates a new window
            def WindowToDisplayArt():
                
                try:
                    ASCII_Converter.destroy()
                except:
                    time.sleep(0)
                
                #opens text in window
                ASCIIartONwindow = Tk()
                
                #title for window
                ASCIIartONwindow.title("ASCII art program by Faeq ")
                
                #icon for window
                try:
                    ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')
                except:
                    time.sleep(0)

    #       -----------------------------------------------------
                    
                            #function to not allow program to end before any processes are complete

                def on_closing():
                    
                    #close window
                    try:
                        ASCIIartONwindow.destroy()
                    except:
                        time.sleep(0)

                    #creates a window
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

                    #canvas for bg
                    cv.pack(side='top', fill='both', expand='yes')
                    cv.create_image(0, 0, image=bg_image, anchor='nw')
                    
                    
                    # anchor='nw' implies upper left corner coordinates
                    cv.create_text(15, 20, text="", fill="red", anchor='nw')
                    
                    
                    #window's icon
                    try:
                        mainWindow.iconbitmap('Icon_for_windows.ico')
                    except:
                        time.sleep(0)

                        #can't resize window
                    mainWindow.resizable(width=False, height=False)
                    
                    #creates enter rle button
                    backimage = tk.PhotoImage(file="Back.gif")

                    #puts the window in front of the menu
                    mainWindow.attributes('-topmost', True)
                    
                    #creates background
                    mainWindow["bg"] = "#FFFFFF"

                    
                    #does not allow window to be moved
                    mainWindow.overrideredirect(True)

                        
                    #does not allow it to be resized
                    mainWindow.resizable(width=False, height=False)

                    
                    #back to prev. window
                    def noclose():

                        #close window
                        mainWindow.destroy()
                        
                        #back to prev. window
                        WindowToDisplayArt()
                        

                    #resizes background image
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on bg
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')
                    Button.image= backimagee

                    #runs window
                    center(mainWindow)
                    mainWindow.mainloop()

    #       -----------------------------------------------------
                    
                   
                #overide close button
                ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)
                
                #puts the window in front of the others
                ASCIIartONwindow.attributes('-topmost', True)
                
                #background colour
                ASCIIartONwindow["bg"] = "SteelBlue1"
        
                #frame for bg
                F1=Frame(ASCIIartONwindow)
                F1=Frame(ASCIIartONwindow,width=400,height=450)
                F1.place(height=7000, width=4000, x=100, y=100)

                #configures freame for size
                F1.grid(columnspan=10,rowspan=10)
                F1.grid_rowconfigure(0,weight=1)
                F1.grid_columnconfigure(0,weight=1)

                #bg image
                photo=PhotoImage(file="HIYA.gif")
                label = Label(ASCIIartONwindow,image = photo)
                
                label.image = photo # keep a reference
                label.grid(row=0,column=0,columnspan=20,rowspan=20)


                #opens file
                ReadFile = open(textfile,'r')

                #reads file
                data = ReadFile.read()


                #closes file
                ReadFile.close()
                artishere = tk.Message(ASCIIartONwindow, text=data, font=('Consolas',13), fg = 'SteelBlue1', bg = '#FFFFFF',width = 90000)
                artishere.grid(row=8,column=8)

                #function to get back to menu
                def backtomenu():
                    ASCIIartONwindow.destroy()
                    menu()

                #creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                #resizes background image
                backimagee = backimage.subsample(3, 3)
                Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee, command =backtomenu ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                #places buytton on window
                Button.grid(row=10,column=8)
                Button.image= backimagee
                
                #centers window
                center(ASCIIartONwindow)

            #runs function above
            WindowToDisplayArt()

    #       -----------------------------------------------------
            
         
        # create a frame and pack it
        frame1 = tk.Frame(ASCII_Converter,bg='#FFFFFF',padx=15)
        frame1.grid(sticky=tk.W)

        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()
        
        #creates enter rle button
        image = tk.PhotoImage(file="C.gif")
        
        #resizes background image
        imagee = image.subsample(3, 3)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =load_data,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee

        
        
        #allows user to browse for file
        try:
            from tkinter import filedialog
            
        except:
            from Tkinter import tkFileDialog

    #       -----------------------------------------------------
        
        def browse():
            
            #opens file dialog and lets user to browse for file
            ASCII_Converter.filename =  filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
            
            # asigns the file location to the variable
            file = ASCII_Converter.filename
            
            #runs the function to load the art through the browse function
            Load_data()

    #       -----------------------------------------------------
            
        

        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()

        #creates enter button
        image = tk.PhotoImage(file="BfF.gif")
        
        #resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =browse,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee


        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='grey')
        emptyspace.grid()


    #       -----------------------------------------------------
        
        #function to exit the window
        def exit_converter():
            
            #takes away the window
            ASCII_Converter.destroy()
            
            #shows the menu again
            menu()

    #       -----------------------------------------------------
        
       #creates enter button
        image = tk.PhotoImage(file="Back.gif")
        
        #resizes background image
        imagee = image.subsample(5, 5)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =exit_converter,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee
        
        #size of window
        ASCII_Converter.geometry("775x592")
        
        #cant resize window
        ASCII_Converter.resizable(width=False, height=False)
        
        #centers window
        center(ASCII_Converter)
        


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


        
#                                               #-------------------------------------------------------------------#
#                                               |       function to create a new window for loading ascii art       |
#                                               #-------------------------------------------------------------------#


    def ASCII_ART_DISPLAYER():
        
        #creates window
        display=tk.Tk()

        #canvas for bg
        C = Canvas(display)
        backg = PhotoImage(file = "LYAA.gif")

        #bg image
        background_label = Label(display, image=backg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #reference
        C.grid()
        C.img = backg
        
        #title for window
        display.title("ASCII art program by Faeq ")
        
        #icon for window
        try:
            display.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)

    #       -----------------------------------------------------
            
        #function to not allow program to end before any processes are complete

        def on_closing():
            
            #close window
            try:
                display.destroy()
            except:
                time.sleep(0)

            #window created
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

            #canvas for bg
            cv.pack(side='top', fill='both', expand='yes')
            cv.create_image(0, 0, image=bg_image, anchor='nw')
            
            # anchor='nw' implies upper left corner coordinates
            cv.create_text(15, 20, text="", fill="red", anchor='nw')
            
            #window's icon
            try:
                mainWindow.iconbitmap('Icon_for_windows.ico')
            except:
                time.sleep(0)

                #can't resize window
            mainWindow.resizable(width=False, height=False)
            
            #creates enter rle button
            backimage = tk.PhotoImage(file="Back.gif")

            #puts the window in front of the menu
            mainWindow.attributes('-topmost', True)
            
            #creates background
            mainWindow["bg"] = "#FFFFFF"

            
            #does not allow window to be moved
            mainWindow.overrideredirect(True)

                
            #does not allow it to be resized
            mainWindow.resizable(width=False, height=False)

                
            
            
            #back to prev. window
            def noclose():

                #close window
                mainWindow.destroy()
                
                #back to prev. window
                ASCII_ART_DISPLAYER()
                

            #resizes background image
            backimagee = backimage.subsample(2, 2)
            Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #places button on bg
            Button.pack(side='left', padx = 3, pady=0, anchor='s')
            Button.image= backimagee

            #runs window
            center(mainWindow)
            mainWindow.mainloop()


    #       -----------------------------------------------------
           
        #overides the close button
        display.protocol("WM_DELETE_WINDOW", on_closing)
        
        #puts the window in front of the menu
        display.attributes('-topmost', True)
        
        #background colour
        display["bg"] = "SteelBlue1"
        
        #creates empty space between widgets
        emptyspace = Label(display, text=" ",bg="#FFFFFF")
        emptyspace.grid()

    #       -----------------------------------------------------
        
        #what happens when you press the button
        def displayArt():


            #adds file extension if there isnt one already
            if e.get().lower().endswith(('.txt')):
                
                enterredfilename = e.get()
            else:
                
                enterredfilename = e.get()+'.txt'
            
            #Checks if the file exists
            if os.path.exists(enterredfilename) == True:
                
                #saves the text in entry field to a variable
                filename = enterredfilename
                
                #adds file extension to name of file so it can open
                file=enterredfilename
                
                #opens file
                ReadFile = open(file,'r')
                
                #reads file
                data = ReadFile.read()
                
                #closes file
                ReadFile.close()

    #       -----------------------------------------------------
                
                #creates a new window
                def WindowToDisplayArt():
                    
                    display.destroy()
                    
                    #opens text in window
                    ASCIIartONwindow = Tk()
                    
                    #title for window
                    ASCIIartONwindow.title("ASCII art program by Faeq ")
                    
                    #icon for window
                    try:
                        ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)

    #       -----------------------------------------------------
                        
                    #function to not allow program to end before any processes are complete

                    def on_closing():
                        
                        #close window
                        try:
                            ASCIIartONwindow.destroy()
                        except:
                            time.sleep(0)

                        #creates window
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

                        #canvas for bg
                        cv.pack(side='top', fill='both', expand='yes')
                        cv.create_image(0, 0, image=bg_image, anchor='nw')
                        
                        # anchor='nw' implies upper left corner coordinates
                        cv.create_text(15, 20, text="", fill="red", anchor='nw')
                    
                        #window's icon
                        try:
                            mainWindow.iconbitmap('Icon_for_windows.ico')
                        except:
                            time.sleep(0)

                        #can't resize window
                        mainWindow.resizable(width=False, height=False)
                        #creates enter rle button
                        backimage = tk.PhotoImage(file="Back.gif")

                        #puts the window in front of the menu
                        mainWindow.attributes('-topmost', True)
                        
                        #creates background
                        mainWindow["bg"] = "#FFFFFF"

                        #does not allow window to be moved
                        mainWindow.overrideredirect(True)
                            
                        #does not allow it to be resized
                        mainWindow.resizable(width=False, height=False)
                        
                        #back to prev. window
                        def noclose():

                            #close window
                            mainWindow.destroy()
                            
                            #back to prev. window
                            ASCII_ART_DISPLAYER()
                            

                        #resizes background image
                        backimagee = backimage.subsample(2, 2)
                        Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                        #places button on bg
                        Button.pack(side='left', padx = 3, pady=0, anchor='s')
                        Button.image= backimagee

                        #runs window
                        center(mainWindow)
                        mainWindow.mainloop()


    #       -----------------------------------------------------

                    #overides the close button
                    ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)
                    
                    #puts the window in front of the menu
                    ASCIIartONwindow.attributes('-topmost', True)

                    #does not allow it to be resized
                    ASCIIartONwindow.resizable(width=False, height=False)
                    
                    #background colour
                    ASCIIartONwindow["bg"] = "SteelBlue1"

                    #frame for bg
                    F1=Frame(ASCIIartONwindow)
                    F1=Frame(ASCIIartONwindow,width=400,height=450)
                    F1.place(height=7000, width=4000, x=100, y=100)

                    #confiugres frame for size
                    F1.grid(columnspan=10,rowspan=10)
                    F1.grid_rowconfigure(0,weight=1)
                    F1.grid_columnconfigure(0,weight=1)

                    #bg image
                    photo=PhotoImage(file="HIYA.gif")
                    label = Label(ASCIIartONwindow,image = photo)
                    
                    label.image = photo # keep a reference
                    label.grid(row=0,column=0,columnspan=20,rowspan=20)


                    #opens file
                    ReadFile = open(file,'r')

                    #reads file
                    data = ReadFile.read()


                    #closes file
                    ReadFile.close()
                    artishere = tk.Message(ASCIIartONwindow, text=data, font=('Consolas',13), fg = 'SteelBlue1', bg = '#FFFFFF',width = 90000)
                    artishere.grid(row=8,column=8)

                    #funtion to back to menu
                    def backtomenu():
                        ASCIIartONwindow.destroy()
                        menu()

                    #creates enter rle button
                    backimage = PhotoImage(file="Back.gif")

                    #resizes background image
                    backimagee = backimage.subsample(3, 3)
                    Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee, command =backtomenu ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on bg
                    Button.grid(row=10,column=8)
                    Button.image= backimagee
                    
                    #centers window
                    center(ASCIIartONwindow)
                    
                    #runs function
                WindowToDisplayArt()
                
                #if the file does not exist:
            else:
                display.destroy()
                
                #runs the error
                errorNoFileForDisplayer()

    #       -----------------------------------------------------

        
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
        
        #what happens when you press the button
        def displayArtt():
            
            #gets file location
            file = display.filename
            
            #opens file
            ReadFile = open(file,'r')
            
            #reads file
            data = ReadFile.read()
            
            #closes file
            ReadFile.close()

    #       -----------------------------------------------------
            
            #creates a new window
            def WindowToDisplayArt():
                try:
                    display.destroy()
                except:
                    time.sleep(0)
                
                #opens text in window
                ASCIIartONwindow = Tk()
                
                #title for window
                ASCIIartONwindow.title("ASCII art program by Faeq ")
                
                #icon for window
                try:
                    ASCIIartONwindow.iconbitmap('Icon_for_windows.ico')
                    
                except:
                    time.sleep(0)

    #       -----------------------------------------------------
                    
                #function to not allow program to end before any processes are complete

                def on_closing():
                    
                    #close window
                    try:
                        ASCIIartONwindow.destroy()
                    except:
                        time.sleep(0)

                    #creates window
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

                    #canvas for bg
                    cv.pack(side='top', fill='both', expand='yes')
                    cv.create_image(0, 0, image=bg_image, anchor='nw')
                    
                    # anchor='nw' implies upper left corner coordinates
                    cv.create_text(15, 20, text="", fill="red", anchor='nw')
                    
                    #window's icon
                    try:
                        mainWindow.iconbitmap('Icon_for_windows.ico')
                    except:
                        time.sleep(0)

                        #can't resize window
                    mainWindow.resizable(width=False, height=False)
                    
                    #creates enter rle button
                    backimage = tk.PhotoImage(file="Back.gif")

                    #puts the window in front of the menu
                    mainWindow.attributes('-topmost', True)
                    
                    #creates background
                    mainWindow["bg"] = "#FFFFFF"

                    
                    #does not allow window to be moved
                    mainWindow.overrideredirect(True)

                        
                    #does not allow it to be resized
                    mainWindow.resizable(width=False, height=False)

                        
                    
                    
                    #back to prev. window
                    def noclose():

                        #close window
                        mainWindow.destroy()
                        
                        #back to prev. window
                        displayArtt()
                        

                    #resizes background image
                    backimagee = backimage.subsample(2, 2)
                    Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                    #places button on bg
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')
                    Button.image= backimagee

                    #runs the window
                    center(mainWindow)
                    mainWindow.mainloop()


    #       -----------------------------------------------------                    

                #overides the close button
                ASCIIartONwindow.protocol("WM_DELETE_WINDOW", on_closing)
                
                #puts the window in front of the menu
                ASCIIartONwindow.attributes('-topmost', True)

                #does not allow it to be resized
                ASCIIartONwindow.resizable(width=False, height=False)
                
                #background colour
                ASCIIartONwindow["bg"] = "SteelBlue1"

                #frame for bg
                F1=Frame(ASCIIartONwindow)
                F1=Frame(ASCIIartONwindow,width=400,height=450)
                F1.place(height=7000, width=4000, x=100, y=100)
                

                #configures frame to window size
                F1.grid(columnspan=10,rowspan=10)
                F1.grid_rowconfigure(0,weight=1)
                F1.grid_columnconfigure(0,weight=1)

                #image for bg
                photo=PhotoImage(file="HIYA.gif")
                label = Label(ASCIIartONwindow,image = photo)
                
                label.image = photo # keep a reference
                label.grid(row=0,column=0,columnspan=20,rowspan=20)


                #opens file
                ReadFile = open('logoart.txt','r')

                #reads file
                data = ReadFile.read()


                #closes file
                ReadFile.close()
                artishere = tk.Message(ASCIIartONwindow, text=data, font=('Consolas',13), fg = 'SteelBlue1', bg = '#FFFFFF',width = 90000)
                artishere.grid(row=8,column=8)

                #function to go back to menu
                def backtomenu():
                    ASCIIartONwindow.destroy()
                    menu()

                #creates enter rle button
                backimage = PhotoImage(file="Back.gif")

                #resizes background image
                backimagee = backimage.subsample(3, 3)
                Button = tk.Button(ASCIIartONwindow, relief='flat', image=backimagee, command =backtomenu ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                #places button on bg
                Button.grid(row=10,column=8)
                Button.image= backimagee
                
                #centers window
                center(ASCIIartONwindow)
                
                #runs function
            WindowToDisplayArt()
        
    #       -----------------------------------------------------


        #allows user to browse for file
        def browse():
            
            #opens file dialog and lets user to browse for file
            display.filename =  filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
            
            # asigns the file location to the variable
            file = display.filename
            
            #runs the function to load the art through the browse function
            displayArtt()

            
    #       -----------------------------------------------------


        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='SteelBlue1')
        emptyspace.grid()

        #creates enter button
        image = tk.PhotoImage(file="BfF.gif")
        
        #resizes background image
        imagee = image.subsample(2, 2)
        ButtonToEnter = tk.Button(frame1, relief=FLAT, image=imagee, command =browse,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")
        
        ButtonToEnter.grid(sticky=tk.W)
        ButtonToEnter.image = imagee


        #creates empty space between widgets
        emptyspace = Label(frame1, text="_____________________________________________________________________",bg="#FFFFFF",fg='grey')
        emptyspace.grid()




    #       -----------------------------------------------------
        
        #function to exit the window
        def exit_this_displayer():
            
            #destroys the window
            display.destroy()
            
            #shows the menu again
            menu()

    #       -----------------------------------------------------
            
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
        
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

     

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


        
#                             #------------------------------------------------------------------------------------------#
#                             |                                 menu's code starts here                                  |
#                             #------------------------------------------------------------------------------------------#

#function to not allow program to end before any processes are complete

    def on_closing():
        
        #close window
        try:
            window_for_menu.destroy()
        except:
            time.sleep(0)

        #new window created
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

        #new canvas for bg
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(0, 0, image=bg_image, anchor='nw')
        
        # anchor='nw' implies upper left corner coordinates
        cv.create_text(15, 20, text="", fill="red", anchor='nw')
        
        #window's icon
        try:
            mainWindow.iconbitmap('Icon_for_windows.ico')
        except:
            time.sleep(0)

            #can't resize window
        mainWindow.resizable(width=False, height=False)
        #creates enter rle button
        backimage = tk.PhotoImage(file="Back.gif")

        #puts the window in front of the menu
        mainWindow.attributes('-topmost', True)
        
        #creates background
        mainWindow["bg"] = "#FFFFFF"

        
        #does not allow window to be moved
        mainWindow.overrideredirect(True)

            
        #does not allow it to be resized
        mainWindow.resizable(width=False, height=False)

            
        
        
        #back to prev. window
        def noclose():

            #close window
            mainWindow.destroy()
            
            #back to prev. window
            menu()
            

        #resizes background image
        backimagee = backimage.subsample(2, 2)
        Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        Button.pack(side='left', padx = 3, pady=0, anchor='s')
        Button.image= backimagee

        #runs window
        center(mainWindow)
        mainWindow.mainloop()

#       -----------------------------------------------------

    #overides the close button
    window_for_menu.protocol("WM_DELETE_WINDOW", on_closing)
    
    #puts the window in front of the others
    window_for_menu.attributes('-topmost', False)
    
    #creates a canvas to put the image on
    PutImageForBackground=Canvas(window_for_menu)
    
    #displays canvas
    PutImageForBackground.grid()
    
    #puts image for background onto canvas
    image1=PhotoImage(file="new.gif")
    
    #keep a link to the image to stop the image being garbage collected
    PutImageForBackground.img=image1
    
    #resizes background image
    displayimage = image1.subsample(1, 1)
    
    #displays image in background
    PutImageForBackground.create_image(400, 300, image=displayimage)

    
#       -----------------------------------------------------


    # creating the class, Window, and the Frame
    class Window(Frame):
        
        # Define settings
        def __init__(self, master=None):
            
            # parameters that are sent through the Frame class. 
            Frame.__init__(self, master)   

            #reference to the window                 
            self.master = master

            #runs the settings
            self.init_window()
    
        #Creation of init_window
        def init_window(self):
            
#       -----------------------------------------------------

            #icon for the window
            try:
                self.master.iconbitmap('Icon_for_windows.ico')
                
            except:
                time.sleep(0)
                
            #changing the title of the window      
            self.master.title("ASCII art program by Faeq ")
            
            # window size created
#       -----------------------------------------------------

            self.master.geometry("724x592")
            
            self.master.resizable(width=False, height=False)
            
#       -----------------------------------------------------

            #allowing the text to take the full space of the window
            self.grid()

            
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            
            #creating a menu
            menu = Menu(self.master)
            self.master.config(menu=menu)

            #create the file object
            file = Menu(menu)

            #adds a command to the menu option
            def exit_program():

                #closes window
                self.master.destroy()

                #creates new window
                mainWindow = tk.Tk()
                mainWindow.title('Bye!')
                
                # pick a .gif image file you have in the working directory
                fname = "Bye.gif"
                bg_image = tk.PhotoImage(file=fname)
                
                # get the width and height of the image
                w = bg_image.width()
                h = bg_image.height()
                
                # size the window so the image will fill it
                mainWindow.geometry('200x100')
                cv = tk.Canvas(width=w, height=h)

                #canvas for bg
                cv.pack(side='top', fill='both', expand='yes')
                cv.create_image(0, 0, image=bg_image, anchor='nw')
                
                # anchor='nw' implies upper left corner coordinates
                cv.create_text(15, 20, text="", fill="red", anchor='nw')
                
                #window's icon
                try:
                    mainWindow.iconbitmap('Icon_for_windows.ico')
                except:
                    time.sleep(0)

                    #can't resize window
                mainWindow.resizable(width=False, height=False)
                
                #creates enter rle button
                backimage = tk.PhotoImage(file="goodBYE.gif")

                #resizes background image
                backimagee = backimage.subsample(8, 8)
                Button = tk.Button(cv, relief='flat', image=backimagee, command =mainWindow.destroy,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                #places button on bg
                Button.pack(side='left', padx=30, pady=5, anchor='sw')
                Button.image= backimagee
                
                #centers window on the screen
                center(mainWindow)

                #runs window
                mainWindow.mainloop()
                
                


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

                
            #function to load the next functions
            def Load_RLE_window():
                
                #destroys the window for the menu
                window_for_menu.destroy()
                
                #loads the option that was selected by the user
                Load_RLE_Window()

            


            #function to load the next functions
            def ASCII_ART_DISPLAYER_window():
                
                #destroys the window for the menu
                window_for_menu.destroy()
                
                #loads the option that was selected by the user
                ASCII_ART_DISPLAYER()




            #function to load the next functions
            def Convert_ASCII_window():
                
                #destroys the window for the menu
                window_for_menu.destroy()
                
                #loads the option that was selected by the user
                Convert_ASCII()





            #function to load the next functions
            def Convert_rle_window():
                
                #destroys the window for the menu
                window_for_menu.destroy()
                
                #loads the option that was selected by the user
                Convert_Rle()

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
                

            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12), justify=LEFT)
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12), justify=LEFT)
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12),cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")

            
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            #checks if buttons are pressed
            button_flag = True

            # create frame
            frame1 = tk.Frame(PutImageForBackground,bg='#FFFFFF',padx=109)
            frame1.grid(sticky=tk.W)

#       -----------------------------------------------------

            #creates enter rle button
            imagetobeused = tk.PhotoImage(file="1.gif")

            #resizes background image
            imagetobeusede = imagetobeused.subsample(3, 3)
            Button = tk.Button(frame1, relief=FLAT, image=imagetobeusede, command =Load_RLE_window,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #places button on bg
            Button.grid()
            Button.image = imagetobeusede

            
#       -----------------------------------------------------

            
            #creates enter rle button
            Displayimage = tk.PhotoImage(file="2.gif")

            #resizes background image
            Displayimagee = Displayimage.subsample(3, 3)

            #creates display ascii art button
            ButtonToDisplayArt = tk.Button(frame1, command=ASCII_ART_DISPLAYER_window, image=Displayimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target")
            
            ButtonToDisplayArt.grid()
            ButtonToDisplayArt.image = Displayimagee

            
#       -----------------------------------------------------

            #creates enter rle button
            ConvertAimage = tk.PhotoImage(file="3.gif")

            #resizes background image
            ConvertAimagee = ConvertAimage.subsample(3, 3)

            #creates convert ascii art button
            ButtonToConvertArt = tk.Button(frame1, image=ConvertAimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target", command=Convert_ASCII_window)

            #places button on bg
            ButtonToConvertArt.grid(sticky="w")
            ButtonToConvertArt.image = ConvertAimagee

            
#       -----------------------------------------------------


            #creates enter rle button
            ConvertRimage = tk.PhotoImage(file="4.gif")
            
            #resizes background image
            ConvertRimagee = ConvertRimage.subsample(3, 3)
            
            #creates convert to rle button
            ButtonToConvertRLE = tk.Button(frame1, image=ConvertRimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=Convert_rle_window)
            
            ButtonToConvertRLE.grid(sticky="w")
            ButtonToConvertRLE.image = ConvertRimagee
            
#       -----------------------------------------------------

            #creates enter rle button
            Quitimage = tk.PhotoImage(file="5.gif")
            
            #resizes background image
            Quitimagee = Quitimage.subsample(3, 3)
            
            #creates quit button
            QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=exit_program)
            
            QuitButton.grid(sticky="w")
            QuitButton.image = Quitimagee

#       -----------------------------------------------------

            #creates enter rle button
            AQAimage = tk.PhotoImage(file="AQA.gif")
            
            #resizes background image
            AQAimagee = AQAimage.subsample(2, 2)
            
            
#       -----------------------------------------------------


            #puts my name on the program
            Name = tk.Button(PutImageForBackground,image = AQAimagee, text="Program By Faeq  ",bg='#81D3E0',fg="#FFFFFF",font=("Segoe UI Emoji",10),relief=FLAT,cursor = "trek")
            Name.grid(sticky="e")
            Name.image = AQAimagee

            
#       -----------------------------------------------------


            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")


            #image for text
            image = tk.PhotoImage(file="r.gif")
            read = tk.Label(PutImageForBackground, image=image,background='white')

            
            #showing image
            read.grid(sticky="w")
            read.image = image
            
#       -----------------------------------------------------

            #asks the user to read my read-me note
            labelspace = tk.Label(PutImageForBackground, text="   ",background='#FFFFFF',fg='SteelBlue1', font=("Calibri", 9),cursor = "arrow")
            labelspace.grid(sticky='w')

            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")

            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text=".                                                                                                                                                                                                                                              .", background='white',cursor = "trek")
            labelspace.grid(sticky="w")

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#                                                             creates canvas with size and positioning


            PutImageForBackground.create_window(900,900)


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            
#                                      makes sure that the python interpreter does not close as soon as the program is read
#                                            also makes sure that the interpreter only closes when the program is done
#
            edit = Menu(menu)
                    
        def client_exit(self):
            exit()


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________            


    #creation
    app = Window(window_for_menu)

    
    #centers window
    center(window_for_menu)

    
    #runs window
    window_for_menu.mainloop()


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                                                                    #---------------------------#
#                                                                    |       End of the code     |
#                                                                    #---------------------------#
#
#                                                                    running all of the code above




menu()




#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

