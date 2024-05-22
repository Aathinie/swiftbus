import customtkinter as ctk
from widgets.image import load_image_ctk

from backend import signup_user


def SingupPage(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="white")

    def onmount():
        win.title("SwiftBus - Sign Up")

    def ondestroy():
        email_entry.delete(0, len(email_entry.get()))
        pwd_entry.delete(0, len(pwd_entry.get()))
        name_entry.delete(0, len(name_entry.get()))

    ####

    logo = ctk.CTkLabel(
        master=page, image=load_image_ctk("./assets/logo.png", (212, 47)), text=""
    )
    logo.place(relx=0.5, rely=0.1, anchor="center")

    ####

    title = ctk.CTkLabel(master=page, text="Sign Up", font=("Roboto", 30))
    title.place(relx=0.5, rely=0.2, anchor="center")

    ####

    form_frame = ctk.CTkFrame(master=page, fg_color="white", width=500, height=300)
    
    ####

    name_label = ctk.CTkLabel(master=form_frame, text="Name", font=("Roboto", 16))
    name_entry = ctk.CTkEntry(master=form_frame, height=50, width=500)
    name_entry.cget("font").configure(size=16)
    name_label.grid(row=1, column=1, sticky="w")
    name_entry.grid(row=2, column=1, sticky="w")
    
    ####

    email_label = ctk.CTkLabel(master=form_frame, text="Email", font=("Roboto", 16))
    email_entry = ctk.CTkEntry(master=form_frame, height=50, width=500)
    email_entry.cget("font").configure(size=16)
    email_label.grid(row=4, column=1, sticky="w")
    email_entry.grid(row=5, column=1, sticky="w")

    ####

    pwd_label = ctk.CTkLabel(master=form_frame, text="Password", font=("Roboto", 16))
    pwd_entry = ctk.CTkEntry(master=form_frame, height=50, width=500)
    pwd_entry.cget("font").configure(size=16)
    pwd_label.grid(row=7, column=1, sticky="w")
    pwd_entry.grid(row=8, column=1, sticky="w")

    ####

    def onsubmit():
        name, email, pwd = name_entry.get(), email_entry.get(), pwd_entry.get()
        if 0 in (len(name), len(email), len(pwd)):
            err_label.configure(text="Make sure to fill all the fields!")
            return 
        
        signup_status = signup_user(name, email, pwd)

        if signup_status is None:
            err_label.configure(text="User already exists!")


    submit = ctk.CTkButton(
        master=form_frame,
        text="Sign Up",
        font=("Roboto", 16),
        height=50,
        command=onsubmit,
    )
    submit.grid(row=10, column=1, sticky="we")

    signup = ctk.CTkLabel(master=form_frame, text="Already have an account? Sign In", font=("Roboto", 16, "underline"))
    signup.bind("<Button-1>", command=lambda _:win.nav.navigate_to("login"))
    signup.grid(row=11, column=1, sticky="we")

    err_label = ctk.CTkLabel(
        master=form_frame, text="", font=("Roboto", 16), text_color="red"
    )
    err_label.grid(row=13, column=1, sticky="we")

    ####

    for i in [3, 6, 9, 12]:
        form_frame.rowconfigure(i, minsize=20)

    form_frame.place(relx=0.5, rely=0.3, anchor="n")

    return "signup", page, onmount, ondestroy
