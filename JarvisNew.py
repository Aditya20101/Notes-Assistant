
import tkinter as tk
from tkinter import Listbox, Scrollbar, ttk
from tkinter.constants import END
import speech_recognition as sr              # recognise speech

win = tk.Tk()                 # win / window / root / app
win.title("Jarvis")


f = open('file.txt' , 'a')          # file is created if does not exist to store notes
f.close()


#create label

welcome_label = ttk.Label(win, text= "Welcome! This is your personal assistant Jarvis" , font=('bold',14))
welcome_label.grid(row=0 , column=0 , sticky=tk.W)
welcome_label.configure(foreground='Blue')

store_label = ttk.Label(win, text= "What do you want me to remember :  ")  
store_label.grid(row=2 , column=0 , sticky=tk.W)

search_label = ttk.Label(win, text= "Search by word :  ")
search_label.grid(row=3 , column=0 , sticky=tk.W)



# create entry box

# this is an entry box just for show. Input is done through speak button by speech
audio_entrybox = ttk.Entry(win , width=10 , state='readonly')
audio_entrybox.grid(row=2 , column= 1)


# here , the user enters the word to be searched in the file for related notes
s = tk.StringVar()
search_entrybox = ttk.Entry(win , width=10 , textvariable = s)
search_entrybox.grid(row=3 , column= 1)


# Create Listbox to show notes

snotes = Listbox(win, height=15, width=100, border=0)
snotes.grid(row=5, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar

scrollbar = Scrollbar(win)
scrollbar.grid(row=5, column=3)

# Set scroll to listbox

snotes.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=snotes.yview)

def action():
    
# with the help of speechrecognition library , this function takes input from the user in the 
# form of speech and converts it to text . 
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
    
        audio = r.listen(source)
        voice_data = r.recognize_google(audio)   # Google Application Programming Interface
        

        snotes.insert( END ,"You just said: ")
        snotes.insert( END , voice_data )
        
        f = open('file.txt' , 'a')
        f.write( f"{voice_data}\n")
        f.close()
        input_button.configure(foreground='Red')

def searchf():
    
    
#   search the entered word in the file and print it if found.
#   word = word entered by the user
#   comparing the value stored in variable "word" with the file content and 
#   return the list  of sentences if matched otherwise null
#   returned value appended in the listbox 

    
    
    f = open('file.txt' , 'r' )
    word = s.get()                           # s is the string entered by the user
    
    list1=[]
    linesList=f.readlines()
    for line in linesList:
        words=line.split()
        for i in words:
            if i.lower()==word.lower():
                list1.append(line.lower())
                break
    
    l=len(list1)
    print()
    snotes.insert( END ,"\n I found : \n")
    for j in range(0,l):
        
        snotes.insert( END ,list1[j] )
    input_button1.configure(foreground='Green')
    f.close()


def sfun():
    
#   print all saved notes in the text file in the listbox    
# readlines() function creates list of strings from a text file. 
# The strings are separated into different elements of the list by "\n" in the text file.


    f = open('file.txt' , 'r' )
    linesList=f.readlines()
    
    l=len(linesList)
    s1="\nYour notes : \n"
    snotes.insert( END , s1)   # insert() function prints the entered string in the listbox
    for k in range(0,l):
        
        snotes.insert( END , linesList[k] )
    f.close()
    print_button.configure(foreground='#b388ff')

    
# define buttons

# every button has a defined functioned associated with it .
# these specific functions are performed when respective buttons are pressed
#    action() , searchf() , sfun() - all three functions are defined above.

input_button = tk.Button(win , text = "Speak" , command = action)
input_button.grid(row=2 , column=2)

input_button1 = tk.Button(win , text = "Search" , command = searchf)
input_button1.grid(row=3 , column=2)

print_button = tk.Button(win , text = "Show all notes" , command = sfun )
print_button.grid(row=4 , column=0)





win.geometry('700x400')
win.mainloop()












