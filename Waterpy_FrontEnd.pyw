import os
path = r"C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy"
os.path.basename(path)
from waterpy.main import waterpy
import subprocess

#import everything from tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox


#Create Window object
window=Tk()
window.title("WaterPy")
window.configure(bg ="#216720")
window.geometry("500x200")

#Define Functions

def fileopen():
    file = filedialog.askopenfilename()
    add_to_list(file)
    
def add_to_list(f):
    f = os.path.basename(f)
    index = 0
    list1.insert(index,f)
    index += 1
    
def rem_from_list():
    selected_song = list1.curselection()
    selected_song = int(selected_song[0])
    list1.delete(selected_song)
    
def run_model():
    os.chdir(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data')
    os.system("waterpy run modelconfig.ini")
    tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')
    
    

    
    
##Define File Explorer and Add Input Parameter Function    
fb1=Button(window, text= "Add Input Parameter", width = 17, command = fileopen)
fb1.grid(row = 1, column = 0)


    
#Define ListBox
list1=Listbox(window, height=6, width=35)
list1.grid(row=3, column=0, rowspan=5, columnspan=3)


#Add scrollbar to the List
sb1=Scrollbar(window)
sb1.grid(row=3, column=3, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Define Buttons: Remove Selected, Clear All, Run
b1=Button(window, text= "Remove Selected", width = 13, command = rem_from_list)
b1.grid(row=4, column=5)

#b2=Button(window, text= "Clear All", width = 12, command = list1.It
#b2.grid(row=5, column=4)

b3=Button(window, text = "Run", width = 12, command = run_model)
b3.grid(row=6, column=5)







window.mainloop()