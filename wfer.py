#Output file directory will need to be changed, including "path", os.startfile, 
#and the input file location parameter within each modelconfig.ini file
#
#
#
#

import os
path = r"C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy"
os.path.basename(path)
from waterpy.main import waterpy
import PIL
from PIL import Image, ImageTk

#import everything from tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox


#Create Window object
window=Tk()
window.title("WaterPy")
window.iconbitmap('usgs-logo-green.ico')
w = 675 # width for the Tk root
h = 225 # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))


#Define Functions

    
def open_folder():
    open('\\outputs\Temp Outputs\\')
    

#
def run_model():
    os.chdir(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data')

    if CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig7.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
   
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar4.get() == 1 and CheckVar5 == 1 and CheckVar3.get() == 0:
        os.system("waterpy run modelconfig.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 1 and CheckVar5.get() == 1:
        os.system("waterpy run modelconfig3.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
   
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 1 and CheckVar4.get() == 1 and CheckVar5.get() == 1:
        os.system("waterpy run modelconfig4.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 1 and CheckVar5.get() == 1:
        os.system("waterpy run modelconfig2.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
   
    elif CheckVar1.get()==0 and CheckVar2.get() ==0 and CheckVar3.get() ==0 and CheckVar4.get() == 1 and CheckVar5.get() == 1:
        os.system("waterpy run modelconfig5.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar4.get() == 1 and CheckVar3.get() == 1 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig6.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
   
    elif CheckVar1.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 1 and CheckVar5 == 1 and CheckVar2.get() == 0:
        os.system("waterpy run modelconfig8.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==1 and CheckVar2.get() ==0 and CheckVar3.get() ==1 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig10.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
        
    elif CheckVar1.get()==1 and CheckVar2.get() ==0 and CheckVar3.get() ==1 and CheckVar4.get() == 0 and CheckVar5.get() == 1:
        os.system("waterpy run modelconfig11.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==1 and CheckVar2.get() ==0 and CheckVar3.get() ==0 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig12.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==1 and CheckVar2.get() ==0 and CheckVar3.get() ==0 and CheckVar4.get() == 0 and CheckVar5.get() == 1:
        os.system("waterpy run modelconfig13.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==0 and CheckVar2.get() ==0 and CheckVar3.get() ==1 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig14.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==0 and CheckVar2.get() ==1 and CheckVar3.get() ==1 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig15.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==1 and CheckVar2.get() ==1 and CheckVar3.get() ==0 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig16.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
    
    elif CheckVar1.get()==1 and CheckVar2.get() ==1 and CheckVar3.get() ==1 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig17.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')
     
    else:
        os.system("waterpy run modelconfig.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        os.startfile(r'C:\Users\mgerzan\Documents\MNG\2018-programming-waterpy\code\waterpy\data\outputs\Temp Outputs')        


frame = tkinter.Frame(window)
frame.configure(bg ="#216720")
frame.grid(row=0, column=0, sticky='nswe')
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame.grid_rowconfigure(9, minsize = 20)
frame.grid_rowconfigure(0, minsize = 10)
frame.grid_rowconfigure(2, minsize =20)
frame.grid_columnconfigure(0, minsize = 20)
frame.grid_columnconfigure(3, minsize = 20)
frame.grid_columnconfigure(5, minsize = 20)



#Define Checkbox Items  

CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
CheckVar3 = tkinter.IntVar()
CheckVar4 = tkinter.IntVar()
CheckVar5 = tkinter.IntVar()


L1 = tkinter.Label(frame, text = "WATERPY RAINFALL-RUNOFF MODEL", width = 35, height = 1, relief= 'raised', font= 'comicsans')
L1.place(x=330, y=20, anchor = 'center')

CBL = tkinter.Label(frame, text = "Choose Optional Parameters:", width = 25, relief= 'raised',)
CBL.place(x=455, y=65, anchor = 'center')
#CBL.grid(row=3, column =2, sticky = 'n') 
    
C1 = tkinter.Checkbutton(frame, text = "Snowmelt", variable = CheckVar1, anchor = 'w', onvalue= 1, offvalue = 0, height=1, width= 30)
C1.place(x=455, y=95, anchor = 'center')
#C1.grid(row=4, column=2)

C2 = tkinter.Checkbutton(frame, text = "Channel Routing", variable = CheckVar2, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30)
C2.place(x=455, y=120, anchor = 'center')
#C2.grid(row=5, column=2)

C3 = tkinter.Checkbutton(frame, text = "Karst", variable = CheckVar3, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30)
C3.place(x=455, y=145, anchor = 'center')
#C3.grid(row=6, column=2)

C4 = tkinter.Checkbutton(frame, text = "Randomize", variable = CheckVar4, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30)
C4.place(x=455, y=170, anchor = 'center')
#C4.grid(row=7, column=2)

C5 = tkinter.Checkbutton(frame, text = "Output Matrices", variable = CheckVar5, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30)
C5.place(x=455, y=195, anchor = 'center')
#C5.grid(row=8, column=2)

CBL2 = tkinter.Label(frame, text = "Required Input Parameters:", width = 25, relief= 'raised',)
CBL2.place(x=175, y=65, anchor = 'center')
#CBL2.grid(row=3, column =1, sticky = 'n') 
    
D1 = tkinter.Checkbutton(frame, text = "Basin Parameters",anchor = 'w', state = 'disabled', height=1, width= 30)
D1.place(x=175, y=105, anchor = 'center')
#D1.grid(row=4, column=1)

D2 = tkinter.Checkbutton(frame, text = "HRU Parameters", anchor = 'w', state = 'disabled', height=1, width= 30)
D2.place(x=175, y=130, anchor = 'center')
#D2.grid(row=5, column=1)

D3 = tkinter.Checkbutton(frame, text = "Climate Timeseries", anchor = 'w', state = 'disabled', height=1, width= 30)
D3.place(x=175, y=155, anchor = 'center')
#D3.grid(row=6, column=1)

D4 = tkinter.Checkbutton(frame, text = "TWI", anchor = 'w', state = 'disabled', height=1, width= 30)
D4.place(x=175, y=180, anchor = 'center')
#D4.grid(row=7, column=1)


#Define Run Button

b3=tkinter.Button(frame, text = "Run", width = 8, height=1, command = run_model)
b3.place(x=630, y=150, anchor = 'center')

#USGS Logo

PILFile = PIL.Image.open("usgslogo.jpg")
PILFile = PILFile.resize((65, 40), PIL.Image.ANTIALIAS)
Image = ImageTk.PhotoImage(PILFile) # <---
ImageLabel = Label(frame, image=Image)
ImageLabel.image = Image
ImageLabel.place(x=40, y= 25, anchor = 'center')



window.mainloop()