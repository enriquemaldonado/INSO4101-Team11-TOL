from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Launcher')
#root.iconbitmap('c:/')
root.geometry("600x400")


def open_program():
    program = filedialog.askopenfilename()
    label.config(text=program)
    os.system('"%s"' % program)


button = Button(root, text="Launch Program", command=open_program)
button.pack(pady=20)


def open_dictionary():
    program = filedialog.askopenfilename()
    label.config(text=dictionary)
    os.system(dictionary)


button2 = Button(root, text="Launch Dictionary", command=open_dictionary)
button2.pack(pady=20)


label = Label(root, text= "")
label.pack(pady=20)

root.mainloop()