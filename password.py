from tkinter import *
import random, string

root = Tk()
root.geometry("700x400")
root.title("Password Generator")

bg_color = "#00BFFF"
fg_color = "black"
font_title = ('Lucida Handwriting', 25, 'bold')
font_label = ('Footlight MT Light', 12, 'bold')
font_button = ('Century', 12, 'bold')
font_result = ('Bookman Old Style', 20, 'bold')
root.config(bg=bg_color)

title = StringVar()
label = Label(root, textvariable=title, font=font_title, bg=bg_color, fg=fg_color)
label.pack(pady=10)
title.set("Generate Flexible Password")

choice = IntVar()

def selection():
    selection = choice.get()

R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection, font=font_label, bg=bg_color, fg=fg_color, selectcolor=bg_color)
R1.pack(anchor=CENTER, pady=5)

R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection, font=font_label, bg=bg_color, fg=fg_color, selectcolor=bg_color)
R2.pack(anchor=CENTER, pady=5)

R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection, font=font_label, bg=bg_color, fg=fg_color, selectcolor=bg_color)
R3.pack(anchor=CENTER, pady=5)

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel, font=font_label, bg=bg_color, fg=fg_color)
lentitle.pack(pady=5)

val = IntVar()
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=13, font=font_label)
spinlength.pack(pady=5)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

def callback():
    password = passgen()
    lsum.config(text=password, font=font_result, fg="darkblue")

passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, font=font_button)
passgenButton.pack(pady=10)

lsum = Label(root, text="", bg=bg_color, fg=fg_color, font=font_result)
lsum.pack(side=BOTTOM, pady=20)

root.mainloop()
