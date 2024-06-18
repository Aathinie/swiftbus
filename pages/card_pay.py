import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk


def PayCard(win):
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

        nav.grid(row=1, column=1, padx=20, pady=20, columnspan=3)

        ##

        title = ctk.CTkLabel(
            master=page, text="Card Information", font=("Roboto", 18, "bold")
        )
        title.grid(row=2, column=1, columnspan=3)

        info_frame = ctk.CTkFrame(master=page, fg_color="#EDEDED")

        name_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")
        name_label = ctk.CTkLabel(
            master=name_frame, text="Name On Card", font=("Roboto", 15)
        )
        name_entry = ctk.CTkEntry(master=name_frame, width=250, height=40)
        name_label.grid(row=1, column=1)
        name_entry.grid(row=2, column=1)

        date_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")
        date_label = ctk.CTkLabel(
            master=date_frame, text="Valid Thru", font=("Roboto", 15)
        )
        date_entry = ctk.CTkEntry(master=date_frame, width=250, height=40)
        date_label.grid(row=1, column=1)
        date_entry.grid(row=2, column=1)

        cvv_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")
        cvv_label = ctk.CTkLabel(master=cvv_frame, text="CVV", font=("Roboto", 15))
        cvv_entry = ctk.CTkEntry(master=cvv_frame, width=250, height=40)
        cvv_label.grid(row=1, column=1)
        cvv_entry.grid(row=2, column=1)

        name_frame.grid(row=1, column=1, padx=20)
        date_frame.grid(row=1, column=2, padx=20)
        cvv_frame.grid(row=1, column=3, padx=20)

        info_frame.grid(row=3, column=1, columnspan=3, pady=20)

        done = ctk.CTkButton(
            master=page,
            text="Done",
            width=100,
            height=40,
            command=lambda: win.navigator.navigate_to("success"),
        )

        done.grid(row=4, column=2, pady=20)

    return "pay_card", page, on_mount, lambda: None
