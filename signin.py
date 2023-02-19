from tkinter import *
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Picsart-main-login.jpg')
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
cd_login_window = Tk()
app = App(cd_login_window)
cd_login_window.geometry('1366x768')

# set the window state to maximized
cd_login_window.state('zoomed')

# Functionality
def username_enter(event):
    if username_entry.get()=='Username':
        username_entry.delete(0,END)
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
cd_head_lbl = Label(cd_login_window, text='USER LOGIN', font=('Times New Roman', 30, 'bold'), bg='white', fg='firebrick1')
cd_head_lbl.place(x=875, y=120)

# Username input TextField
username_entry = Entry(cd_login_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
username_entry.place(x=780, y=240)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', username_enter)

# Username line for TextField
Frame(cd_login_window, width=430, height=2, bg='firebrick1').place(x=780, y=285)

# Password input TextField
password_entry = Entry(cd_login_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
password_entry.place(x=780, y=335)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', password_enter)

# Password line for TextField
Frame(cd_login_window, width=430, height=2, bg='firebrick1').place(x=780, y=380)

# Eye
cd_open_eye = PhotoImage(file='images/openeye.png')
cd_eye_btn = Button(cd_login_window, image=cd_open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
cd_eye_btn.place(x=1170, y=340)

# Forgot Password
cd_forget_pass_btn = Button(cd_login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Times New Roman', 13, 'bold'), fg='firebrick1', activeforeground='firebrick1')
cd_forget_pass_btn.place(x=1080, y=390)

# Button
cd_login_btn = Button(cd_login_window, text='LOGIN', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=25, height=1)
cd_login_btn.place(x=780, y=450)

# Signup
cd_sign_up_lbl = Label(cd_login_window, text="Don't have an account?", font=('Open sans', 15, 'bold'), fg='firebrick1', bg='white')
cd_sign_up_lbl.place(x=800, y=550)
cd_new_acc_btn = Button(cd_login_window, text='Create One Now', font=('Open Sans', 15, 'bold underline'), fg='blue', bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0)
cd_new_acc_btn.place(x=1030, y=545)


cd_login_window.mainloop()
