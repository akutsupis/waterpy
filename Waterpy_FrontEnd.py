import os
path = r"E:\Desktop\code\waterpy"
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
    
def open_foler():
    open('\\outputs\Temp Outputs\\')
    
def run_model():
    os.chdir(r'E:\Desktop\code\waterpy\data')
    os.system("waterpy run modelconfig.ini")
    tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
    os.startfile(r'E:\Desktop\code\waterpy\TempOutputs')  # what's this line do?


frame = tkinter.Frame(window)
frame.configure(bg ="#216720")
frame.grid(row=0, column=0, sticky='nswe')
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


    
##Define File Explorer and Add Input Parameter Function    
fb1 = Button(frame, text= "Add Input Parameter", width = 17, command = fileopen)
fb1.grid(row = 2, column = 0, sticky = 'n')


    
#Define ListBox
list1=Listbox(frame)
list1.grid(row=5, column=0, rowspan=5, columnspan=4, sticky = 'we')


#Add scrollbar to the List
sb1=Scrollbar(frame)
sb1.grid(row=6, column=4, rowspan=3, columnspan = 2, sticky = 'NS')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Define Buttons: Remove Selected, Clear All, Run
b1=Button(frame, text= "Remove Selected", width = 13, command = rem_from_list)
b1.grid(row=2, column=1)

#b2=Button(window, text= "Clear All", width = 12, command = list1.It
#b2.grid(row=5, column=4)

b3=Button(frame, text = "Run", width = 12, command = run_model)
b3.grid(row=2, column=4, sticky = 'n')


window.mainloop()