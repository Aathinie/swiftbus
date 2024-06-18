import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk

adults_data = []
children_data = []


def ConfirmTicket(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="#EDEDED")
    page.grid_propagate(0)
    source = destination = date = adults = children = None

    def on_mount():
        nonlocal source, destination, date, adults, children
        sourceid, source, destinationid, destination, date, adults, children = tuple(
            open("data", "r").readlines()
        )

        ##
        nav = ctk.CTkFrame(master=page, width=900, fg_color="#EDEDED")

        logo = ctk.CTkLabel(
            master=nav, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
        )
        logo.grid(row=1, column=1, padx=40)

        back = ctk.CTkButton(
            master=nav,
            text="< Back",
            command=lambda: win.navigator.navigate_to("passenger_info"),
        )
        back.grid(row=1, column=3, padx=40, sticky="ne")
        nav.columnconfigure(2, minsize=700)

        nav.grid(row=1, column=1, padx=20, pady=20)

        ## get information
        title = ctk.CTkLabel(
            master=page, text="Confirm Booking", font=("Roboto", 18, "bold")
        )
        title.grid(row=2, column=1, pady=10)

        main_frame = ctk.CTkFrame(master=page, fg_color="#EDEDED")

        # fetch bus image
        cursor.execute(f"select name, image from bus where uid='{win.busid}'")
        busname, image = cursor.fetchone()

        image = ctk.CTkLabel(
            master=main_frame, text="", image=load_image_ctk(image, (0, 300))
        )
        image.grid(row=1, column=1, rowspan=4, padx=40)

        info_frame = ctk.CTkFrame(master=main_frame, fg_color="#EDEDED")

        name = ctk.CTkLabel(master=info_frame, text=busname, font=("Roboto", 18))
        name.grid(row=1, column=1, sticky="w", pady=10)

        dept = ctk.CTkLabel(
            master=info_frame,
            text=f"Departs at {win.depttime} on {date.strip()}",
            font=("Roboto", 18),
        )
        dept.grid(row=2, column=1, sticky="w", pady=10)

        seats = ctk.CTkLabel(
            master=info_frame,
            text="Seats: " + (", ".join(win.selected_seats)),
            font=("Roboto", 18),
        )
        seats.grid(row=3, column=1, sticky="w", pady=10)

        count = ctk.CTkLabel(
            master=info_frame,
            text=f"{int(adults)} Adult{'s' if int(adults) > 1 else ''} and {int(children)} {'Children' if int(children) > 1 else 'Child'}",
            font=("Roboto", 18),
        )
        count.grid(row=4, column=1, sticky="w", pady=10)

        info_frame.grid(row=1, column=2, rowspan=4)

        main_frame.grid(row=3, column=1)

        ## payment

        payment_btn = ctk.CTkButton(
            master=page,
            text="Proceed To Payment",
            height=40,
            font=("Roboto", 15),
            width=200,
            command=lambda:win.navigator.navigate_to("pay_select")
        )
        payment_btn.grid(row=4, column=1, columnspan=2, pady=30)

    return "confirm_ticket", page, on_mount, lambda: None
