
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

a = tk.StringVar()
audio_entrybox = ttk.Entry(win , width=10 , textvariable = a,  state='readonly')
audio_entrybox.grid(row=2 , column= 1)

s = tk.StringVar()
search_entrybox = ttk.Entry(win , width=10 , textvariable = s)
search_entrybox.grid(row=3 , column= 1)


snotes = Listbox(win, height=15, width=100, border=0)
snotes.grid(row=5, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(win)
scrollbar.grid(row=5, column=3)
# Set scroll to listbox
snotes.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=snotes.yview)

def action():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
    
        audio = r.listen(source)
        voice_data = r.recognize_google(audio)
        snotes.insert( END ,"You just said: ")
        snotes.insert( END , voice_data )
        print()
        f = open('file.txt' , 'a')
        f.write( f"{voice_data}\n")
        f.close()
        input_button.configure(foreground='Red')

def searchf():
    f = open('file.txt' , 'r' )
    word=s.get()
    
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
    f = open('file.txt' , 'r' )
    linesList=f.readlines()
    
    l=len(linesList)
    s1="\nYour notes : \n"
    snotes.insert( END , s1)
    for k in range(0,l):
        
        snotes.insert( END , linesList[k] )
    f.close()
    print_button.configure(foreground='#b388ff')

    
# define buttons

input_button = tk.Button(win , text = "Speak" , command = action)
input_button.grid(row=2 , column=2)

input_button1 = tk.Button(win , text = "Search" , command = searchf)
input_button1.grid(row=3 , column=2)

print_button = tk.Button(win , text = "Show all notes" , command = sfun )
print_button.grid(row=4 , column=0)


# Create Listbox to show notes


win.geometry('700x400')
win.mainloop()












