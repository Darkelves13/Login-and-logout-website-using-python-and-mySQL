from tkinter import *
from PIL import ImageTk

#Functionality 
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def hide_password():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show_password)

def show_password():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide_password)

#GUI 
login_window = Tk()
login_window.geometry('990x660')
login_window.resizable(0,0)
login_window.title('LOGIN PAGE')
bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=bgImage)

bgLabel.place(x=0,y=0)

heading = Label(login_window, text='USER LOGIN', font=('Comic Sans MS', 15, 'bold'), bg='white', fg='firebrick1')
heading.place(x=640, y=120)

usernameEntry = Entry(login_window, width=25, font=('Comic Sans MS', 10), bd=0, fg='firebrick1')
usernameEntry.place(x=605, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=200, height=2, bg='firebrick1')
frame1.place(x=605,y=222)

passwordEntry = Entry(login_window, width=25, font=('Comic Sans MS', 10), bd=0, fg='firebrick1')
passwordEntry.place(x=605, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=200, height=2, bg='firebrick1')
frame2.place(x=605,y=280)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide_password)
eyeButton.place(x=780, y=250)

forgotButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Comic Sans MS', 10), fg='firebrick1', activeforeground='firebrick1')
forgotButton.place(x=695, y=290)

loginButton = Button(login_window, text='Login', bg='firebrick1', font=('Comic Sans MS', 10, 'bold'), fg='white', activebackground='firebrick1', activeforeground='white', bd=0, width=25, height=2, cursor='hand2')
loginButton.place(x=605, y=350)

orLable = Label(login_window, text='------------- OR ------------', font=('Comic Sans MS', 16), fg='firebrick1', width=15, bg='white')
orLable.place(x=605, y=400)

facebook_logo = PhotoImage(file='facebook.png')
fbLable = Label(login_window, image=facebook_logo, bg='white', cursor='hand2')
fbLable.place(x=630, y=450)

google_logo = PhotoImage(file='google.png')
googleLable = Label(login_window, image=google_logo, bg='white', cursor='hand2')
googleLable.place(x=690, y=450)

twitter_logo = PhotoImage(file='twitter.png')
twitterLable = Label(login_window, image=twitter_logo, bg='white', cursor='hand2')
twitterLable.place(x=750, y=450)

signupLable = Label(login_window, text="Don't have an account?", font=('Comic Sans MS', 8, 'bold'), fg='firebrick1', bg='white')
signupLable.place(x=605, y=500)

newaccountButton = Button(login_window, text='Create new one', bg='white', font=('Comic Sans MS', 8, 'bold underline'), fg='blue', activebackground='white', activeforeground='blue', bd=0, cursor='hand2')
newaccountButton.place(x=730, y=500)

login_window.mainloop()
