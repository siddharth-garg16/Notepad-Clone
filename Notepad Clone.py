from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def about():
    tmsg.showinfo("About","This is a Notepad Clone made using Tkinter.")

def newFile():
    global file
    root.title("Untitled - Notepad Clone")
    file = None
    textwindow.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad Clone")
        textwindow.delete(1.0, END)
        f = open(file, "r")
        textwindow.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "a")
            f.write(textwindow.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad Clone")
    else:
        f = open(file, "a")
        f.write(textwindow.get(1.0, END))
        f.close()

def exitapp():
    root.destroy()

def cut():
    textwindow.event_generate(("<<Cut>>"))

def copy():
    textwindow.event_generate(("<<Copy>>"))

def paste():
    textwindow.event_generate(("<<Paste>>"))

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad Clone")
    root.geometry("1150x650")
    root.minsize(700,500)

    #text area and scrollbar for the notepad
    scrlbr = Scrollbar(root)
    scrlbr.pack(side=RIGHT, fill=Y)

    textwindow = Text(root, font="consolas 11", yscrollcommand=scrlbr.set)
    file = None
    textwindow.pack(side=LEFT, expand=True, fill=BOTH)

    scrlbr.config(command=textwindow.yview)

    #notepad's menubar
    menuBar = Menu(root)

    file1 = Menu(menuBar, tearoff=0)
    file1.add_command(label="New", command=newFile)
    file1.add_command(label="Open", command=openfile)
    file1.add_separator()
    file1.add_command(label="Save", command=save)
    file1.add_separator()
    file1.add_command(label="Exit", command=exitapp)
    menuBar.add_cascade(label="File", menu=file1)

    edit1 = Menu(menuBar, tearoff=0)
    edit1.add_command(label="Cut", command=cut)
    edit1.add_separator()
    edit1.add_command(label="Copy", command=copy)
    edit1.add_separator()
    edit1.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=edit1)

    menuBar.add_command(label="About", command=about)

    root.config(menu=menuBar)  

    root.mainloop()
