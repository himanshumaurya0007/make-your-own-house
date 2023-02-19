from PIL import Image, ImageTk
import tkinter as tk

cd_login_window = tk.Tk()
cd_login_window.geometry('1280x720')
cd_login_window.resizable(0,0)
cd_login_window.title('Login')
cd_login_window.iconbitmap('')


# Open image using PIL
image = Image.open("images/login.jpg")

# Convert image to PhotoImage using ImageTk
bg_image = ImageTk.PhotoImage(image)

# Use PhotoImage as background
bg_label = tk.Label(cd_login_window, image=bg_image)
bg_label.place(x=0, y=0)

cd_login_window.mainloop()
#
#
# from tkinter import *
# from tkinter import messagebox
# from PIL import ImageTk
#
# # Functionality
# def username_enter(event):
#     if username_entry.get() == 'Username':
#         username_entry.delete(0, END)
#
# def password_enter(event):
#     if password_entry.get() == 'Password':
#         password_entry.delete(0, END)
#
# def hide(event):
#     cd_open_eye.config(file='closeye.png')
#     password_entry.config(show='*')
#     cd_eye_btn.config(command=show)
#
# def show():
#     cd_open_eye.config(file='openeye.png')
#     password_entry.config(show='')
#     cd_eye_btn.config(command=hide)
#
# # MySQL Connectivity Code
# # def login_fun():
# #     db_username = username_entry.get()
# #     db_password = password_entry.get()
# #     if db_username == "" and db_password == "":
# #         messagebox.showinfo("", "Invalid username or password!")
# #     elif db_username == "Admin" and db_password == "123":
# #         messagebox.showinfo("", "Login Success")
# #         cd_login_window.destroy()
# #     else:
# #         messagebox.showinfo("", "Incorrent Username and Password")
#
# # GUI
# cd_login_window = Tk()
# cd_login_window.geometry('1280x720+50+50')
# cd_login_window.resizable(0, 0)
# cd_login_window.title('Login')
# cd_login_window.iconbitmap('')
#
# # Defining Background Image
# cd_bg_image = PhotoImage(file='/images/bg.png')
#
# # Background Image Label
# cd_bg_lbl = Label(cd_login_window, image=cd_bg_image)
# cd_bg_lbl.place(x=0, y=0)
#
# # Heading Label
# cd_head_lbl = Label(cd_login_window, text='USER LOGIN', font=('Times New Roman', 23, 'bold'), bg='white', fg='firebrick1')
# cd_head_lbl.place(x=605, y=120)
#
# # Username input TextField
# username_entry = Entry(cd_login_window, width=25, font=('Times New Roman', 11, 'bold'), bd=0, fg='firebrick1')
# username_entry.place(x=580, y=200)
# username_entry.insert(0, 'Username')
# username_entry.bind('<FocusIn>', username_enter)
#
# # Username line for TextField
# Frame(cd_login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)
#
# # Password input TextField
# password_entry = Entry(cd_login_window, width=25, font=('Times New Roman', 11, 'bold'), bd=0, fg='firebrick1')
# password_entry.place(x=580, y=260)
# password_entry.insert(0, 'Password')
# password_entry.bind('<FocusIn>', password_enter)
#
# # Password line for TextField
# Frame(cd_login_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)
#
# cd_open_eye = PhotoImage(file='images/openeye.png')
# cd_eye_btn = Button(cd_login_window, image=cd_open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
# cd_eye_btn.place(x=800, y=255)
#
# cd_forget_pass_btn = Button(cd_login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Times New Roman', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1')
# cd_forget_pass_btn.place(x=715, y=295)
#
# cd_login_btn = Button(cd_login_window, text='LOGIN', font=('Open Sans', 16, 'bold'), fg='white', bg='
