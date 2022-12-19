
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


# ---------------------------------------------------------------Forgot Function --------------------------------------
def forgot():

    if email.get() == "":
        messagebox.showerror("Error", "Please fill all the details!", parent=win_1)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="Dishit@2141", database="FaceFilter")
            cur = con.cursor()
            cur.execute("select * from user_details where email=%s",
                        (email.get()
                         ))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Details! ", parent=win_1)

            else:
                messagebox.showinfo("Success", "Successfully verify email...!", parent=win_1)
                mail = email.get()
                reset()
                close()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win_1)


def clear():
    email.delete(0, END)


def close():
    win_1.destroy()


# ---------------------------------------------------------------End Forgot Function ---------------------------------


# ----------------------------------------------------------- Reset Window --------------------------------------------------

def reset():
    # reset database connect
    def action():
        if  password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!", parent=winreset)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "New Password & Confirm Password Should Be Same", parent=winreset)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Dishit@2141", database="FaceFilter")
                cur = con.cursor()
                cur.execute("select * from user_details where password=%s", password.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Password Already Exits!", parent=winreset)
                else:
                    cur.execute(
                        "update user_details set password=%s where email=%s",
                        (	
                            password.get(),
                            email.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Reset password Successfully...!", parent=winreset)
                    clear()
                    import main
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=winreset)

    # close reset function
    def switch():
        winreset.destroy()

    # clear data function
    def clear():
        password.delete(0, END)
        very_pass.delete(0, END)

    # start Reset Window

    winreset = Tk()
    winreset.title("Face filter App")
    winreset.maxsize(width=500, height=400)
    winreset.minsize(width=500, height=400)

    # heading label
    heading = Label(winreset, text="Reset Password", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label

    password = Label(winreset, text="New Password :", font='Verdana 10 bold')
    password.place(x=80, y=130)

    very_pass = Label(winreset, text="Verify Password:", font='Verdana 10 bold')
    very_pass.place(x=80, y=160)

    # Entry Box ------------------------------------------------------------------


    password = StringVar()
    very_pass = StringVar()

    password = Entry(winreset, width=30, textvariable=password)
    password.place(x=210, y=133)

    very_pass = Entry(winreset, width=30, show="*", textvariable=very_pass)
    very_pass.place(x=210, y=163)

    # button reset password and clear

    btn_reset = Button(winreset, text="Reset", font='Verdana 10 bold', command=action)
    btn_reset.place(x=200, y=293)

    btn_forgot = Button(winreset, text="Clear", font='Verdana 10 bold', command=clear)
    btn_forgot.place(x=280, y=293)

    reset_pass_btn = Button(winreset, text="Switch To Forgot Page", command=switch)
    reset_pass_btn.place(x=310, y=20)

    winreset.mainloop()


# ---------------------------------------------------------------------------End Reset Window-----------------------------------


# ------------------------------------------------------------ Forgot Window -----------------------------------------

win_1 = Tk()

# app title
win_1.title("Face Filter App")

# window size
win_1.maxsize(width=500, height=500)
win_1.minsize(width=500, height=500)

# heading label
heading = Label(win_1, text="Forgot password", font='Verdana 25 bold')
heading.place(x=80, y=150)

email = Label(win_1, text="Enter Email :", font='Verdana 10 bold')
email.place(x=80, y=220)

# Entry Box
email = StringVar()


email = Entry(win_1, width=30, textvariable=email)
email.focus()
email.place(x=200, y=223)

# button Verify email and clear

btn_forgot = Button(win_1, text="Verify", font='Verdana 10 bold', command=forgot)
btn_forgot.place(x=200, y=293)

btn_forgot = Button(win_1, text="Clear", font='Verdana 10 bold', command=clear)
btn_forgot.place(x=280, y=293)

# reset button

#reset_pass_btn = Button(win_1, text="Switch To Reset Page", command=reset)
#reset_pass_btn.place(x=350, y=20)

win_1.mainloop()
# -------------------------------------------------------------------------- End Forgot Window ---------------------------------------------------
