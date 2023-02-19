from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Picsart-main-signup.jpg')
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the background label and pack it
        self.background_label = Label(self, image=self.photo)
        self.background_label.pack(fill=BOTH, expand=YES)

        # Allow the user to fit the image to the window size
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # Resize the image
        self.image = self.image.resize((event.width, event.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label.config(image=self.photo)

# Create the Tkinter window and run the application
cd_signup_window = Tk()
app = App(cd_signup_window)
cd_signup_window.geometry('1366x768')
cd_signup_window.title('Registration')
cd_signup_window.iconbitmap('')

# set the window state to maximized
cd_signup_window.state('zoomed')

# Functionality
def name_enter(event):
    if name_entry.get()=='Name':
        name_entry.delete(0,END)
def username_enter(event):
    if username_entry.get()=='Username':
        username_entry.delete(0,END)
def answer_enter(event):
    if answer_entry.get()=='Answer':
        answer_entry.delete(0,END)
def password_enter(event):
    if password_entry.get()=='Password':
        password_entry.delete(0,END)
def hide(event):
    cd_open_eye.config(file='closeye.png')
    password_entry.config(show='*')
    cd_eye_btn.config(command=show)
def show():
    cd_open_eye.config(file='openeye.png')
    password_entry.config(show='')
    cd_eye_btn.config(command=hide)

# Heading Label
cd_head_lbl = Label(cd_signup_window, text='REGISTRATION', font=('Times New Roman', 30, 'bold'), bg='white', fg='firebrick1')
cd_head_lbl.place(x=190, y=105)

# Name input TextField
name_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
name_entry.place(x=127, y=180)
name_entry.insert(0, 'Name')
name_entry.bind('<FocusIn>', name_enter)

# Name line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=215)

# Username input TextField
username_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
username_entry.place(x=127, y=250)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', username_enter)

# Username line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=285)

# list of options in dropdown-menu
cd_options = ["What is your mother's name?", "What is your nick name?", "Who is your first childhood friend?", "What is your first school name?"]

# create a combobox
selected_option = tk.StringVar()
cd_combobox = ttk.Combobox(cd_signup_window, textvariable=selected_option, values=cd_options, width=29, font=('Times New Roman', 20, 'bold'), )
cd_combobox.current(0)
cd_combobox.place(x=127 , y=330)

# create a style and set the foreground color
cd_style = ttk.Style()
cd_style.map('TCombobox', fieldforeground=[('readonly', 'red')])

# Answer input TextField
answer_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
answer_entry.place(x=127, y=400)
answer_entry.insert(0, 'Answer')
answer_entry.bind('<FocusIn>', answer_enter)

# Answer line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=435)

# Password input TextField
password_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
password_entry.place(x=127, y=475)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', password_enter)

# Password line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=510)

# Eye
cd_open_eye = PhotoImage(file='images/openeye.png')
cd_eye_btn = Button(cd_signup_window, image=cd_open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
cd_eye_btn.place(x=1170, y=340)

# Button
cd_login_btn = Button(cd_signup_window, text='SIGNUP', font=('Open Sans', 17, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=30, height=1)
cd_login_btn.place(x=127, y=550)

cd_signup_window.mainloop()