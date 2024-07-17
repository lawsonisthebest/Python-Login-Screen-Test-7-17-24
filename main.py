import ttkbootstrap as tk
from tkinter import *
from ttkbootstrap.constants import *
import customtkinter
import os

root = tk.Window(themename="superhero")

style = tk.Style()

root.geometry('300x425')
root.title('Login Screen Test')

titleFont = ('Gill Sans', 40, 'bold')
label = tk.Label(root, text="Login:", font=titleFont)
label.pack(pady=(5,0))

seperator = tk.Separator(bootstyle="info")
seperator.pack(pady=(10,15), fill="x", padx=60)

labelFont = ('Gill Sans', 20, 'bold')
label = tk.Label(root, text="Username:", font=labelFont)
label.pack(pady=(0,3))

entryFont = ('Gill Sans', 15, 'bold')
usernameEntry = tk.Entry(root, bootstyle="primary", font=entryFont)
usernameEntry.pack(pady=(0,20))

labelFont = ('Gill Sans', 20, 'bold')
label = tk.Label(root, text="Password:", font=labelFont)
label.pack(pady=(0,3))

passwordEntry = tk.Entry(root, bootstyle="primary", font=entryFont)
passwordEntry.pack(pady=(0,20))

seperator = tk.Separator(bootstyle="info")
seperator.pack(pady=(5,25), fill="x", padx=60)

def submit():
    if usernameEntry.get() != "" and passwordEntry.get() != "":
        style.configure('default.TLabel', font=labelFont)
        welcomeLabel.configure(text="Welcome " + usernameEntry.get() + "!\nNice To Meet\nYou!", style='default.TLabel')
    if usernameEntry.get() == "" and passwordEntry.get() == "":
        style.configure('danger.TLabel', font=labelFont)
        welcomeLabel.configure(text="Username Or\nPassword Is\nEmpty!", style='danger.TLabel')

buttonFont = ('Gill Sans', 17, 'bold')
style.configure('primary.Outline.TButton', font=buttonFont)
submitButton = tk.Button(root, text='Submit', style="primary.Outline.TButton", width=11, command=submit)
submitButton.pack(pady=(0,20))

labelFont = ('Gill Sans', 20, 'bold')
style.configure('default.TLabel', font=labelFont)
welcomeLabel = tk.Label(root, text="", style='default.TLabel', justify="center")
welcomeLabel.pack(pady=0)

root.mainloop()