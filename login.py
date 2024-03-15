import os
import pickle
import sys
from subprocess import call
from openpyxl import load_workbook
from datetime import datetime
import sqlite3
import os.path
from __main__ import *
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

class save:
    def __init__(self,USERNAME,PASSWARD):
        self.username = USERNAME
        self.passward = PASSWARD
        print(self.username,self.passward)
    
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)



font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
font10 = "-family {Helvetica Neue Light} -size 15 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
font18 = "-family {Segoe UI} -size 16 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"

class login:
    def __init__(self):
        self.USERNAME = ""
        self.PASSWARD = ""

        root1=Tk()

        crd = []
        U = []
        P = []
        def file_save():
            u = str(crd[0])
            p = str(crd[1])
            fo = open("login.dat","rb")
            try:
                while True:
                    s = pickle.load(fo)

                    k = s.username
                    U.clear()
                    U.append(k)
                    l = s.passward
                    P.clear()
                    P.append(l)
                    continue

            except EOFError:
                pass
            fo.close()
            if u in U and p in P:
                root1.destroy()
            else:
                self.Text1.insert(INSERT, "invalid username or passward""\n")

        def show_pass():
            if self.Entry2["show"] == "":
                self.Entry2["show"] = "#"
                self.Button = Button(root1)
                self.Button.place(relx=0.9, rely=0.32, height=30, width=30)
                click_btn= PhotoImage(file="Show_pass-1.PNG")
                self.Button.configure(image=click_btn)
                self.Button.configure(relief="raised")
                self.Button.configure(borderwidth=3)
                self.Button.configure(activebackground="#000000")
                self.Button.configure(activeforeground="#FFFFFF")
                self.Button.configure(command=show_pass)
            else:
                self.Entry2["show"] = ""
                self.Button = Button(root1)
                self.Button.place(relx=0.9, rely=0.32, height=30, width=30)
                click_btn= PhotoImage(file="Show_pass-2.PNG")
                self.Button.configure(image=click_btn)
                self.Button.configure(relief="raised")
                self.Button.configure(borderwidth=3)
                self.Button.configure(activebackground="#000000")
                self.Button.configure(activeforeground="#FFFFFF")
                self.Button.configure(command=show_pass)
            root1.mainloop()

        def chk_username(pointless=None):
            while True:
                self.k = str(self.username.get())
                if len(self.k) != 0:
                    self.USERNAME=self.k
                    chk_pass()
                    break
                else:
                    self.Text1.insert(INSERT, "Username cannot be enpty""\n")
                    chk_pass()
                    break

        def chk_pass():
            while True:
                self.pas = str(self.passward.get())
                if len(self.pas) != 0:
                    self.PASSWARD = self.pas
                    submit_clicked()
                    break
                else:
                    self.Text1.insert(INSERT, "Passward cannot be empty""\n")
                    break
    
        def submit_clicked():
            crd.clear()
            crd.append(self.USERNAME)
            crd.append(self.PASSWARD)
            file_save()
        
         
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'

        root1.geometry("500x300+500+200")
        root1.title("LogIN")
        root1.configure(background="#C1CDCD")

        self.Label1 = Label(root1)
        self.Label1.place(relx=0.13, rely=0.1, height=100, width=200)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(background="#C1CDCD")
        self.Label1.configure(font=font12)
        self.Label1.configure(anchor=NW)
        self.Label1.configure(width=582)
        self.Label1.configure(text='''Username    :''')

        self.Entry1 = Entry(root1)
        self.username=StringVar()
        self.Entry1.place(relx=0.47, rely=0.13, height=30, width=200)
        self.Entry1.configure(background="#F0FFFF")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.username)

        self.Label2 = Label(root1)
        self.Label2.place(relx=0.13, rely=0.3, height=100, width=200)
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(background="#C1CDCD")
        self.Label2.configure(font=font12)
        self.Label2.configure(anchor=NW)
        self.Label2.configure(width=582)
        self.Label2.configure(text='''Passward     :''')

        self.Entry2 = Entry(root1)
        self.passward=StringVar()
        self.Entry2.place(relx=0.47, rely=0.32, height=30, width=200)
        self.Entry2.configure(background="#F0FFFF")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(show="#")
        self.Entry2.configure(highlightbackground="#ffffff")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#e6e6e6")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=self.passward)

        self.Text1 = Text(root1)
        self.Text1.place(relx=0.1, rely=0.6, height= 110, width=400)
        self.Text1.configure(background="#C1CDCD")
        self.Text1.configure(font=font10)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Button = Button(root1)
        self.Button.place(relx=0.9, rely=0.32, height=30, width=30)
        click_btn= PhotoImage(file="Show_pass-1.PNG")
        self.Button.configure(image=click_btn)
        self.Button.configure(relief="raised")
        self.Button.configure(borderwidth=3)
        self.Button.configure(activebackground="#000000")
        self.Button.configure(activeforeground="#FFFFFF")
        self.Button.configure(command=show_pass)

        self.Button1 = Button(root1)
        self.Button1.place(relx=0.75, rely=0.45, height=40, width=100)
        self.Button1.configure(relief="raised")
        self.Button1.configure(borderwidth=8)
        self.Button1.configure(activebackground="#000000")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font18)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SUBMIT''')
        self.Button1.configure(command=chk_username)
        root1.bind('<Return>', chk_username)

        root1.mainloop()

if __name__ == '__main__':
    login=login()