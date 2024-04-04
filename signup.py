from tkinter import *
from PIL import ImageTk

def login_page():
    signup_window.destroy()
    import signin

signup_window = Tk()
signup_window.title('SIGNUP PAGE')
signup_window.resizable(False,False)

background = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='Create New Account', font=('Comic Sans MS', 15, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=45, pady=10)

emailLabel = Label(frame, text='Email', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1', activeforeground='white')
emailLabel.grid(row=2, column=0, sticky='w', padx=25)

emailEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='firebrick1')
emailEntry.grid(row=3, column=0, sticky='w', padx=27)

usernameLabel = Label(frame, text='Username', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1', activeforeground='white')
usernameLabel.grid(row=4, column=0, sticky='w', padx=25)

usernameEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='firebrick1')
usernameEntry.grid(row=5, column=0, sticky='w', padx=27)

passwordLabel = Label(frame, text='Password', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1', activeforeground='white')
passwordLabel.grid(row=6, column=0, sticky='w', padx=25)

passwordEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='firebrick1')
passwordEntry.grid(row=7, column=0, sticky='w', padx=27)

confirmpasswordLabel = Label(frame, text='Confirm Password', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1', activeforeground='white')
confirmpasswordLabel.grid(row=8, column=0, sticky='w', padx=25)

confirmpasswordEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='firebrick1')
confirmpasswordEntry.grid(row=9, column=0, sticky='w', padx=27)

termandcondition = Checkbutton(frame, text='I agree to the terms and condiitons', font=('Comic Sans MS', 10, 'bold'), fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1')
termandcondition.grid(row=10, column=0)

signupButton = Button(frame, text='Signup', font=('Comic Sans MS', 10, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=30, height=2)
signupButton.grid(row=12, column=0, pady=20)

alreadyaccount = Label(frame, text="Don't have an account?", font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
alreadyaccount.grid(row=13, column=0, sticky='w', padx=25, pady=20)

loginButton = Button(frame, text='Log in', font=('Comic Sans MS', 10, 'bold underline'), bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white', activeforeground='blue', command=login_page)
loginButton.place(x=195, y=383)

signup_window.mainloop()