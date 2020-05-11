
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

def run_model():
    os.chdir(r'C:\Users\mgerzan\Documents\WaterPY-master (2)\WaterPY-master\data')

    if CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 0 and CheckVar5.get() == 0:
        os.system("waterpy run modelconfig.ini")
        tkinter.messagebox.showinfo('Waterpy', 'Model Run Sucessful')   
        output = my_var.get
#        print(output)
        os.startfile(r'C:\Users\mgerzan\Documents\WaterPY-master (1)\WaterPY-master\data\outputs\Temp Outputs')
          


frame = tkinter.Frame(window)
frame.configure(bg ="#A4C1A4")
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

CBL = tkinter.Label(frame, text = "Choose Basin Type:", width = 20)
CBL.place(x=455, y=65, anchor = 'center')
#CBL.grid(row=3, column =2, sticky = 'n') 
    
C1 = tkinter.Checkbutton(frame, text = "2009 Standard", variable = CheckVar1, anchor = 'w', onvalue= 1, state = 'active', offvalue = 0, height=1, width= 30)
C1.place(x=455, y=95, anchor = 'center')
#C1.grid(row=4, column=2)

C2 = tkinter.Checkbutton(frame, text = "Mixed", variable = CheckVar2, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30, state = 'disabled')
C2.place(x=455, y=120, anchor = 'center')
#C2.grid(row=5, column=2)

C3 = tkinter.Checkbutton(frame, text = "Forest", variable = CheckVar3, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30, state = 'disabled')
C3.place(x=455, y=145, anchor = 'center')
#C3.grid(row=6, column=2)

C4 = tkinter.Checkbutton(frame, text = "Agriculture", variable = CheckVar4, anchor = 'w', onvalue=1, offvalue = 0, height=1, width= 30, state = 'disabled')
C4.place(x=455, y=170, anchor = 'center')
#C4.grid(row=7, column=2)

C5 = tkinter.Checkbutton(frame, text = "Developed", variable = CheckVar5, anchor = 'w', onvalue=1, state = 'disabled', offvalue = 0, height=1, width= 30)
C5.place(x=455, y=195, anchor = 'center')
#C5.grid(row=8, column=2)

my_var = StringVar()

def browse(var):
    dirname = tkinter.filedialog.askdirectory()
    if dirname:
        var.set(dirname)
    DirLabel= tkinter.Label(frame, text = dirname)
#    DirLabel.place(x=100, y=200, anchor = 'center')
def browse2():
    fname = tkinter.filedialog.askopenfilename()
    
    FLabel = tkinter.Label(frame, text = fname)
#    FLabel.place (x=100, y=92, anchor = 'center')
        


#Define Lables, Buttons, etc etc
    
T = tkinter.Label(frame, text = "Choose shp file of area to be modeled", height=1, bg = "#A4C1A4")
T.place(x=0, y =75, anchor = 'w')

T2 = tkinter.Label(frame, text = "Choose characteristics (.csv) file (optional)", height=1, bg = "#A4C1A4")
T2.place(x=0, y =120, anchor = 'w')

T3 = tkinter.Label(frame, text = "Choose twi file (optional)", height=1, bg = "#A4C1A4")
T3.place(x=0, y =160, anchor = 'w')

T4 = tkinter.Label(frame, text = "Choose Folder for Outputs", height=1, bg = "#A4C1A4")
T4.place(x=0, y =200, anchor = 'w')
    
b3=tkinter.Button(frame, text = "Run", width = 8, height=1, command = run_model)
b3.place(x=630, y=130, anchor = 'center')

shp = tkinter.Button(frame, text = "Browse",command = browse2)
shp.place(x=265, y = 120, anchor = 'center')

br = tkinter.Button(frame, text = "Browse", command = lambda: browse(my_var))
br.place(x=265, y=160, anchor = 'center')    

g = tkinter.Button(frame, text = "Select Input SHP File", command = browse2)
g.place(x=265, y=75, anchor = 'center')

g2 = tkinter.Button(frame, text = "Select Output Directory",command= lambda: browse(my_var))
g2.place(x=265, y=200, anchor = 'center')



#USGS Logo

PILFile = PIL.Image.open("usgslogo.jpg")
PILFile = PILFile.resize((65, 40), PIL.Image.ANTIALIAS)
Image = ImageTk.PhotoImage(PILFile) # <---
ImageLabel = Label(frame, image=Image)
ImageLabel.image = Image
ImageLabel.place(x=40, y= 25, anchor = 'center')



window.mainloop()