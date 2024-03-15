from __main__ import *
import sys
from tkinter import filedialog
import tempfile
import os
import tkinter as tkinter

try:
    from tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

fo1=open("recipt.txt","r")
list1=fo1.readlines()

del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
del list1[6]
del list1[7]
del list1[8]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]
list1[5]=list1[5][:-1]
list1[6]=list1[6][:-1]
list1[7]=list1[7][:-1]
list1[8]=list1[8][:-1]


font10 = "-family {Georgia} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
'''font17 = "-family {Segoe UI} -size 20 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"'''

o = '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@  @        FAIRMONT DUBAI        @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @        DUBAI SEA VIEW           @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @  SERVING GUEST SINCE     @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @    #######2015#######    @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @         TOKEN:-  %s        @  @@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@
@              NAME:-                        %s
@    
@              ADDRESS:-                  %s
@    
@              MOBILE NO:-             %s
@    
@              ROOM NUMBER:-     %s
@
@              NO. OF PEOPLE:-       %s
@
@              ROOM TYPE:-             %s
@
@              NO. OF DAYS:-            %s
@    
@              TOTAL BILL Rs:-        %s
@
@@@@@@@@@@@@@   @    THANKS FOR VISITING    @   @@@@@@@@@@@@@

'''%(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8])


p = '''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @        FAIRMONT DUBAI       @  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @        DUBAI SEA VIEW       @  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @     SERVING GUEST SINCE     @  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @      #######2015#######     @  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @       TOKEN:-  %s      @  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                                  @
@                                                                  @
@                NAME:-                  %s                              
@                                                                  @      
@                ADDRESS:-               %s                                 
@                                                                  @      
@                MOBILE NO:-             %s                                    
@                                                                  @    
@                ROOM NUMBER:-           %s 
@                                                                  @  
@                NO. OF PEOPLE:-         %s          
@                                                                  @
@                ROOM TYPE:-             %s
@                                                                  @
@                NO. OF DAYS:-           %s               
@                                                                  @
@                TOTAL BILL Rs:-         %s       
@                                                                  @
@                                                                  @
@                      THANKS FOR VISITING                         @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
     
     
'''%(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8])

class recipt:
    def __init__(self):

        def print_recipt(pointless=None):
            f = open("recipt.rtf", "w+")
            f.write(p)
            f.close()
            temp_file = tempfile.mktemp('recipt.rtf')
            os.startfile('recipt.rtf', 'print')


        root=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'

        root.geometry("800x800")
        root.title("recipt")
        root.configure(background="#FFEFDB")
        #root.state('zoomed')


        self.Label1 = Label(root)
        self.Label1.configure(background="#FFEFDB")
        self.Label1.place(relx=0, rely=0, height=700, width=800)#relx=0.25
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(font=font10)
        self.Label1.configure(text=o)
        self.Label1.configure(anchor=N)
        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify =LEFT)
        self.Label1.configure(width=582)

        self.Button1 = Button(root)
        self.Button1.place(relx=0.3, rely=0.83, height=92, width=300)
        click_btn= PhotoImage(file='Print.png')
        self.Button1.configure(relief="raised")
        self.Button1.configure(borderwidth=8)
        self.Button1.configure(activebackground="#000000")
        self.Button1.configure(activeforeground="#FFFFFF")
        '''self.Button1.configure(background="#FFC1C1")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")'''
        self.Button1.configure(image=click_btn)
        '''self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(font=font17)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''#PRINT''')
        self.Button1.configure(command=print_recipt)
        root.bind('<Return>', print_recipt)

        root.mainloop()

if __name__ == '__main__':
    recipt1=recipt()