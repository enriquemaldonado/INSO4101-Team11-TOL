import tkinter as tk

root = tk.Tk()
root.geometry("990x660+50+50")
root.title('Home Page')
root.tk_setPalette('black')


def extend_menu():
    extend_frame.pack_propagate(False)

    extend_frame.configure(height=300, width=200, bg='grey')

    menu_btn = tk.Button(extend_frame, text='X', font=('Bold', 20), bd=0, fg='grey', command=fold_menu)

    menu_btn.place(x=10, y=10)

    b1 = tk.Button(extend_frame, text='Library', font=('Bold', 20), bd=0, fg='grey')

    b1.place(x=30, y=130)

    b2 = tk.Button(extend_frame, text='Settings', font=('Bold', 20), bd=0, bg='white', fg='grey')

    b2.place(x=30, y=230)

    b3 = tk.Button(extend_frame, text='About', font=('Bold', 20), bd=0, fg='grey')

    b3.place(x=30, y=330)

    b4 = tk.Button(extend_frame, text='Log Out', font=('Bold', 20), bd=0, fg='grey')

    b4.place(x=30, y=430)


def fold_menu():
    global extend_frame
    extend_frame.destroy()

    extend_frame = tk.Frame(root)

    extend_frame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True)


menu_btn = tk.Button(root, text='☰', font=('Bold', 20), bd=0, command=extend_menu)

menu_btn.place(x=10, y=10)

extend_frame = tk.Frame(root, bg='gray')

extend_frame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True)

root.mainloop()