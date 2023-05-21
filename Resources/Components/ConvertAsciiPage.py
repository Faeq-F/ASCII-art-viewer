
"""
def Convert_Rle():

    #       -----------------------------------------------------

        # function to compress the data

        def CompressData():

            # adds file extension if there isnt one already
            if Convert_rle.entry.get().lower().endswith(('.txt')):

                # gets the end file name
                enterredfilename = Convert_rle.entry.get()

                # if trheree is not already a file extension...
            else:

                # a file extrension is added
                enterredfilename = Convert_rle.entry.get()+'.txt'

            # Checks if the file exists
            if os.path.exists(enterredfilename) == True:

                # saves the text in entry field to a variable
                file = enterredfilename

                # name of new file
                textfile = "NewEncodedData.txt"

                # opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content
                open(textfile, "w+").close()

                # opens file
                openfile = open(file)

    #       -----------------------------------------------------

                # creates a while loop so that i can check every line one at a time
                while True:

                    # reads the line
                    line = openfile.readline()

                    # takes away the part that would indicate a new line so that it can be decoded
                    decoded_string = line.replace("\n", "")

                    # string to be encoded
                    string = decoded_string

                    # importing time for exception errors
                    import time

                    # duplicating the variable so that i have 2 of the same thing
                    word = string

                    # checking consecutive characters repeating
                    count = 1

                    # variable to store the final value after counting
                    length = ""

    #       -----------------------------------------------------

                    # check the length of occurence
                    if len(word) > 1:

                        # loop for every character
                        for i in range(1, len(word)):

                            #       -----------------------------------------------------

                            # check if the one after is the same
                            if word[i-1] == word[i]:

                                # if so, add one to the counting variable
                                count += 1

    #       -----------------------------------------------------

                                # if not...
                            else:

                                # write to the final variable (uses ':' to seperate occurence to character being repeated)
                                length += str(count)+":"+word[i-1]+":"

                                # changing the count variable
                                count = 1

                                # write to the final variable (uses ':' to seperate occurence to character being repeated)
                        length += (""+str(count)+":"+word[i]+":")

                        # if not...
                    else:

                        #       -----------------------------------------------------

                        # change the item
                        i = 0

                        try:
                            # write to the final variable (uses ':' to seperate occurence to character being repeated)
                            length += (""+str(count)+":"+word[i]+":")

                        except:
                            # I use sleep for 0 seconds because it practically makes the program  do nothing
                            time.sleep(0)

    #       -----------------------------------------------------

                    # creating another copy
                    same_one = length

                    # taking out the colons and making sublists in list
                    New_String = same_one.split(":")

                    # math used to make every first item in the sublist of length 2 (so if the sublist is [5,5], it will allow me to turn it into [05,5])
                    import math

                    # actually doing what was described above
                    New_String = [New_String[2*i:2*i+2]
                                  for i in range(0, math.ceil(len(New_String)/2))]

                    # writing to a new list (to make the end result clean)
                    Idea = []

    #       -----------------------------------------------------

                    # this method allows me to not need to remove the last sublist as it only has one argument instead of two (and this part looks for 2)
                    try:

                        # checks for the first and second items in sublist
                        for start, end in New_String:

                            #       -----------------------------------------------------

                            # checks length of the first item in sublist
                            if len(start) == 1:

                                # adds 0 to the start of single digit numbers
                                start = '0'+start

                                # adds the changed item to the new list
                                Idea.append(start)

                                # adds the character being repeated to the new list
                                Idea.append(end)
                                # if not...

    #       -----------------------------------------------------

                            else:
                                # adds the number of consective occurences to the new list
                                Idea.append(start)

                                # adds the character being repeated to the new list
                                Idea.append(end)
                                # if there is not enough arguments...

    #       -----------------------------------------------------

                    except:
                        # wait 0 seconds (skips the last sublist and continues with the rest program)
                        time.sleep(0)

    #       -----------------------------------------------------

                    # making the list into a string without any annoying commas or square brackets
                    makeitastring = ''.join(map(str, Idea))

                    # adds the new line indicator to the compressed data so that it can be saved correctly to the new file
                    encoded_string_with_new_line = makeitastring + "\n"

                    # writes to the file
                    WriteToFile = open(textfile, "a")

                    # writes the data to the file
                    WriteToFile.write(encoded_string_with_new_line)

                    # closes the file
                    WriteToFile.close

    #       -----------------------------------------------------

                    # if there is not another line:
                    if len(line) < 1:

                        # ends loop
                        break

    #       -----------------------------------------------------

                # closes the file
                openfile.close()

                # opens old file
                with open(file) as f:

                    # reads all parts of file for each line
                    text = f.read().splitlines()

                    # reads the amount of lines in the file
                lines = len(text)

                # reads the amount of words in the file
                words = sum(len(line.split())for line in text)

                # uses the previous 2 variables to work out the character count of the file
                characters_in_original = sum(len(line)for line in text)

    #       -----------------------------------------------------

                # opens new file
                with open(textfile) as f:

                    # reads all parts of file for each line
                    text = f.read().splitlines()

    #       -----------------------------------------------------

                    # reads the amount of words in the file
                lines = len(text)

                # reads the amount of words in the file
                words = sum(len(line.split())for line in text)

                # uses the previous 2 variables to work out the character count of the file
                characters_in_new = sum(len(line)for line in text)

                # calculates the difference in characters
                difference = characters_in_original - characters_in_new

                # makes the difference a string so it can be concatenated with other strings
                difference = str(difference)

                # takes away the window
                Convert_rle.destroy()
"""
try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    from Tkinter import *
    import Tkinter as tk

from Components import window, canvas, frame, button, center, Page

class ConvertAsciiPage(Page):
    def __init__(self, *args):
        Page.__init__(self)

        C = Canvas(self.window)
        background = PhotoImage(file="./Resources/Images/pConvertR.gif")
        background_label = Label(self.window, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        C.img = background

        F = frame(self.window)

        # text entry field
        imag = tk.PhotoImage(file="./Resources/Images/EntryField.gif")
        # sizing image to window size
        imagee = imag.subsample(3, 3)
        s = tk.Label(F, borderwidth=1, image=imagee, bg='#FFFFFF')
        s.place(relx=0.5, rely=0.5, anchor=CENTER)
        s.image = imagee

        # entry field
        entry = tk.Entry(F, width=20, bg='#FFFFFF', relief='flat', font=(
            'Consolas', 18), fg='SteelBlue1')
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creates enter rle button
        backimage = PhotoImage(file=self.ImageDir+"\\bBack.gif")

        # resizes background image
        backimagee = backimage.subsample(3, 3)
        Button = tk.Button(F, relief='flat', image=backimagee,command=self.BackToMenu, bg="#FFFFFF", fg='#FFFFFF', cursor="target")

        # places button on window
        Button.place(relx=0.5, rely=0.9, anchor=CENTER)
        Button.image = backimagee

if __name__ == "__main__":
    test = ConvertAsciiPage()
    test.window.mainloop()