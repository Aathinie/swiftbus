import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk


def SelectPaymentMethod(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="#EDEDED")
    page.grid_propagate(0)

    source = destination = date = adults = children = None

    def on_mount():
        nav = ctk.CTkFrame(master=page, width=1200, fg_color="#EDEDED")

        logo = ctk.CTkLabel(
            master=nav, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
        )
        logo.grid(row=1, column=1, padx=40)

        back = ctk.CTkButton(
            master=nav,
            text="< Back",
            command=lambda: win.navigator.navigate_to("confirm_ticket"),
        )

        nav.columnconfigure(2, minsize=700)

        nav.grid(row=1, column=1, padx=20, pady=20, columnspan=2)

        ##

        title = ctk.CTkLabel(
            master=page, text="Select Payment Method", font=("Roboto", 18, "bold")
        )
        title.grid(row=2, column=1, columnspan=2, pady=10)

        center = ctk.CTkFrame(master=page, fg_color="#EDEDED")

        card_frame = ctk.CTkFrame(
            master=center, height=300, width=300, fg_color="#ffffff"
        )
        card_frame.bind(
            "<Button-1>", command=lambda _: win.navigator.navigate_to("pay_card")
        )
        card_frame.pack_propagate(0)

        card_frame.grid(row=3, column=1, padx=20)

        card_logo = ctk.CTkLabel(
            master=card_frame,
            image=load_image_ctk("./assets/credit_card.png", (0, 200)),
            text="",
        )
        card_logo.bind(
            "<Button-1>", command=lambda _: win.navigator.navigate_to("pay_card")
        )
        card_txt = ctk.CTkLabel(master=card_frame, text="Card", font=("Roboto", 15))

        card_logo.pack()
        card_txt.pack(pady=10)

        upi_frame = ctk.CTkFrame(
            master=center, height=300, width=300, fg_color="#ffffff"
        )
        upi_frame.bind(
            "<Button-1>", command=lambda _: win.navigator.navigate_to("pay_upi")
        )
        upi_frame.pack_propagate(0)

        upi_frame.grid(row=3, column=2, padx=20)

        upi_logo = ctk.CTkLabel(
            master=upi_frame,
            image=load_image_ctk("./assets/upi.jpg", (0, 200)),
            text="",
        )
        upi_logo.bind(
            "<Button-1>", command=lambda _: win.navigator.navigate_to("pay_upi")
        )
        upi_txt = ctk.CTkLabel(master=upi_frame, text="UPI", font=("Roboto", 15))

        upi_logo.pack()
        upi_txt.pack(pady=10)

        center.place(relx=0.5, rely=0.5, anchor="center")

    return "pay_select", page, on_mount, lambda: None
