import os
from subprocess import call
import customtkinter
import sys

try:
    from tkinter import *
    from PIL import ImageTk, Image
except ImportError:
    from tkinter import *
    from PIL import ImageTk, Image
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_checkinn():
    call(["python", "checkin_gui_and_program.py"])
def click_list():
    call(["python", "listgui.py"])
def click_checkout():
    call(["python", "checkoutgui.py"])
def click_get_info_of_guest():
    call(["python","get_info_of_guest.py"])


class HOTEL_MANAGEMENT:
    def __init__(self):
        call(["python", "login.py"])

        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#A9A9A9'
        _fgcolor = '#000000'
        _compcolor = '#ffffff'
        _ana1color = '#ffffff'
        _ana2color = '#ffffff'
        font14 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        

        root.geometry("1011x750")
        root.title("HOTEL MANAGEMENT") 
        root.configure(background="#000000")
        root.configure(highlightbackground="#A9A9A9")
        root.configure(highlightcolor="black")
        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)
        root.attributes('-fullscreen', True)
        root. bind('<Escape>',lambda e: root. destroy())

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)
        '''self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#CD3333")
        self.Frame1.configure(highlightbackground="#CD3333")
        self.Frame1.configure(highlightcolor="black")'''
        self.Frame1.configure(width=925)
        self.Frame1.pack()

        img = ImageTk.PhotoImage(Image.open("image.jpg"))

        self.label = Label(self.Frame1, image = img)
        self.label.pack()

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.07, rely=0.01, relheight=0.10, relwidth=0.86)
        self.Message6.configure(relief="raised")
        self.Message6.configure(borderwidth=8)
        self.Message6.configure(background="#000000")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#FFFFFF")
        self.Message6.configure(highlightbackground="#308014")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''WELCOME''')
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.07, rely=0.13, height=50, width=300)
        self.Button2.configure(relief="raised")
        self.Button2.configure(borderwidth=8)
        self.Button2.configure(activebackground="#000000")
        self.Button2.configure(activeforeground="#FFFFFF")
        self.Button2.configure(background="#838B8B")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#FFEBCD")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''CHECK INN''')
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.734, rely=0.13, height=50, width=300)
        self.Button3.configure(relief="raised")
        self.Button3.configure(borderwidth=8)
        self.Button3.configure(activebackground="#000000")
        self.Button3.configure(activeforeground="#FFFFFF")
        self.Button3.configure(background="#838B8B")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#FFEBCD")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''GUEST LIST''')
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.07, rely=0.23, height=50, width=300)
        self.Button4.configure(relief="raised")
        self.Button4.configure(borderwidth=8)
        self.Button4.configure(activebackground="#000000")
        self.Button4.configure(activeforeground="#FFFFFF")
        self.Button4.configure(background="#838B8B")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#FFEBCD")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''CHECK OUT''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.734, rely=0.23, height=50, width=300)
        self.Button5.configure(relief="raised")
        self.Button5.configure(borderwidth=8)
        self.Button5.configure(activebackground="#000000")
        self.Button5.configure(activeforeground="#FFFFFF")
        self.Button5.configure(background="#838B8B")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#FFEBCD")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''GUEST INFO''')
        self.Button5.configure(command=click_get_info_of_guest)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.455, rely=0.90, height=50, width=150)
        self.Button6.configure(relief="raised")
        self.Button6.configure(borderwidth=8)
        self.Button6.configure(activebackground="#000000")
        self.Button6.configure(activeforeground="#FFFFFF")
        self.Button6.configure(background="#FFFFFF")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#FFEBCD")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''EXIT''')
        self.Button6.configure(command=quit)

        root.mainloop()


if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT()


