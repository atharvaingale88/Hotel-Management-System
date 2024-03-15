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

font10 = "-family {Georgia} -size 30 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0 "

t='''
TOKEN NO.:-  %s
ROOM NO.:-   %s
'''%(list1[0],list1[4])

class token:
    def __init__(self):

        root=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'

        root.geometry("500x190+500+200")
        root.title("TOKEN")
        root.configure(background="#FFEFDB")

        self.Label1 = Label(root)
        self.Label1.configure(background="#FFEFDB")
        self.Label1.place(relx=0.01, rely=0, height=700, width=800)#relx=0.25
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(font=font10)
        self.Label1.configure(text=t)
        self.Label1.configure(anchor=NW)
        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify =LEFT)
        self.Label1.configure(width=582)

        root.mainloop()

if __name__ == '__main__':
    token1=token()