import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk

adults_data = []
children_data = []


def PassengerInfo(win):
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
            command=lambda: win.navigator.navigate_to("seat_select"),
        )
        back.grid(row=1, column=3, padx=40, sticky="ne")
        nav.columnconfigure(2, minsize=700)

        nav.grid(row=1, column=1, padx=20, pady=20, columnspan=3)

        ##
        header_row = ctk.CTkFrame(
            master=page, width=1200, fg_color="#EDEDED", height=40
        )
        header_row.grid_propagate(0)

        title = ctk.CTkLabel(
            master=header_row,
            text="Passenger Information",
            font=("Roboto", 18, "bold"),
            width=1000,
        )
        title.grid(row=1, column=1, columnspan=2, sticky="w")

        def handle_continue():
            def validate(data):
                for name, age, aadhaar in data:
                    if not name.get() or not age.get() or not aadhaar.get():
                        return False

                return True

            if not (validate(adults_data) and validate(children_data)):
                return

            win.navigator.navigate_to("confirm_ticket")

        continue_btn = ctk.CTkButton(
            master=header_row, text="Continue >", command=handle_continue
        )
        continue_btn.grid(row=1, column=3, sticky="e")

        header_row.grid(row=2, column=1, columnspan=3)

        row_index = 3

        center = ctk.CTkFrame(master=page, fg_color="#EDEDED")

        for i in range(int(adults)):
            info = ctk.CTkFrame(master=center, fg_color="#EDEDED")
            passenger_title = ctk.CTkLabel(
                master=info,
                text=f"Adult {i + 1}",
                font=("Roboto", 14, "bold"),
            )
            passenger_title.grid(row=1, column=1, sticky="w")

            name_frame = ctk.CTkFrame(master=info, fg_color="#EDEDED")
            name_title = ctk.CTkLabel(
                master=name_frame, text="Name", font=("Roboto", 14)
            )

            name_strvar = ctk.StringVar(master=info)
            name_entry = ctk.CTkEntry(
                master=name_frame, width=320, height=40, textvariable=name_strvar
            )
            name_title.grid(row=1, column=1, sticky="w")
            name_entry.grid(row=2, column=1, sticky="w")

            name_frame.grid(row=2, column=1)

            age_strvar = ctk.StringVar(master=info)
            age_frame = ctk.CTkFrame(master=info, fg_color="#EDEDED")
            age_title = ctk.CTkLabel(master=age_frame, text="Age", font=("Roboto", 14))
            age_entry = ctk.CTkEntry(
                master=age_frame, width=320, height=40, textvariable=age_strvar
            )
            age_title.grid(row=1, column=1, sticky="w")
            age_entry.grid(row=2, column=1, sticky="w")
            age_frame.grid(row=2, column=2, padx=10)

            aadhaar_strvar = ctk.StringVar(master=info)
            aadhaar_frame = ctk.CTkFrame(master=info, fg_color="#EDEDED")
            aadhaar_title = ctk.CTkLabel(
                master=aadhaar_frame,
                text="Aadhaar Number",
                font=("Roboto", 14),
            )
            aadhaar_entry = ctk.CTkEntry(
                master=aadhaar_frame,
                width=320,
                height=40,
                textvariable=aadhaar_strvar,
            )
            aadhaar_title.grid(row=1, column=1, sticky="w")
            aadhaar_entry.grid(row=2, column=1, sticky="w")

            aadhaar_frame.grid(row=2, column=3, padx=10)

            adults_data.append((name_strvar, age_strvar, aadhaar_strvar))
            info.grid(row=row_index, column=1, pady=10)
            row_index += 1

        for j in range(int(children)):
            info = ctk.CTkFrame(master=center, fg_color="#EDEDED")
            passenger_title = ctk.CTkLabel(
                master=info,
                text=f"Child {j + 1}",
                font=("Roboto", 14, "bold"),
            )
            passenger_title.grid(row=1, column=1, sticky="w")

            name_frame = ctk.CTkFrame(master=info, fg_color="#EDEDED")
            name_title = ctk.CTkLabel(
                master=name_frame, text="Name", font=("Roboto", 14)
            )

            name_strvar = ctk.StringVar(master=info)
            name_entry = ctk.CTkEntry(
                master=name_frame, width=320, height=40, textvariable=name_strvar
            )
            name_title.grid(row=1, column=1, sticky="w")
            name_entry.grid(row=2, column=1, sticky="w")

            name_frame.grid(row=2, column=1)

            age_strvar = ctk.StringVar(master=info)
            age_frame = ctk.CTkFrame(master=info, fg_color="#EDEDED")
            age_title = ctk.CTkLabel(master=age_frame, text="Age", font=("Roboto", 14))
            age_entry = ctk.CTkEntry(
                master=age_frame, width=320, height=40, textvariable=age_strvar
            )
            age_title.grid(row=1, column=1, sticky="w")
            age_entry.grid(row=2, column=1, sticky="w")
            age_frame.grid(row=2, column=2, padx=10)

            aadhaar_strvar = ctk.StringVar(master=info)
            aadhaar_frame = ctk.CTkFrame(master=info, fg_color="#EDEDED")
            aadhaar_title = ctk.CTkLabel(
                master=aadhaar_frame,
                text="Aadhaar Number",
                font=("Roboto", 14),
            )
            aadhaar_entry = ctk.CTkEntry(
                master=aadhaar_frame,
                width=320,
                height=40,
                textvariable=aadhaar_strvar,
            )
            aadhaar_title.grid(row=1, column=1, sticky="w")
            aadhaar_entry.grid(row=2, column=1, sticky="w")

            aadhaar_frame.grid(row=2, column=3, padx=10)

            adults_data.append((name_strvar, age_strvar, aadhaar_strvar))
            info.grid(row=row_index, column=1, pady=10)
            row_index += 1

        center.place(relx=0.5, rely=0.5, anchor="center")

    return "passenger_info", page, on_mount, lambda: None
