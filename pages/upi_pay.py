import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk


def PayUPI(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="#EDEDED")
    page.grid_propagate(0)

    source = destination = date = adults = children = None

    def on_mount():
        nav = ctk.CTkFrame(master=page, width=900, fg_color="#EDEDED")

        logo = ctk.CTkLabel(
            master=nav, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
        )
        logo.grid(row=1, column=1, padx=40)

        back = ctk.CTkButton(
            master=nav,
            text="< Back",
            command=lambda: win.navigator.navigate_to("pay_select"),
        )

        nav.columnconfigure(2, minsize=700)

        nav.pack()

        ##

        title = ctk.CTkLabel(
            master=page, text="Select Payment Method", font=("Roboto", 18, "bold")
        )
        title.pack(pady=10)

        qr = ctk.CTkLabel(
            master=page, text="", image=load_image_ctk("./assets/qr.png", (200, 0))
        )
        qr.pack(pady=10)

        done = ctk.CTkButton(
            master=page,
            text="Done",
            width=100,
            height=40,
            command=lambda: win.navigator.navigate_to("success"),
        )
        done.pack(
            pady=20,
        )

    return "pay_upi", page, on_mount, lambda: None
