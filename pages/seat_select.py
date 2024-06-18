import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk

selected_seats = []
booked_seats = []
seats_ref = []
seats_remaining = 0
total_seats = 0


def SeatSelect(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="#EDEDED")
    page.grid_propagate(0)

    source = destination = date = adults = children = None
    route_data = []

    def on_mount():
        global seats_remaining, total_seats, selected_seats
        selected_seats = win.selected_seats or []
        
        nonlocal source, destination, date, adults, children, route_data
        sourceid, source, destinationid, destination, date, adults, children = tuple(
            open("data", "r").readlines()
        )

        seats_remaining = int(adults) + int(children)
        total_seats = int(adults) + int(children)

        cursor.execute(f"select * from routes where uid='{win.routeid}'")

        route_data = cursor.fetchall()
        print(route_data)

        def get_booked_seats():
            global booked_seats
            cursor.execute(
                f"select seats from bookings where journeyDate={date} and routeId={win.routeid}"
            )
            booked = cursor.fetchall()
            booked_seats = ""

            for seat in booked:
                booked_seats += seat + ";"

            booked_seats = booked_seats.split(";")

        ###
        nav = ctk.CTkFrame(master=page, width=900, fg_color="#EDEDED")

        logo = ctk.CTkLabel(
            master=nav, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
        )
        logo.grid(row=1, column=1, padx=40)

        back = ctk.CTkButton(
            master=nav,
            text="< Back",
            command=lambda: win.navigator.navigate_to("results"),
        )
        back.grid(row=1, column=3, padx=40, sticky="ne")
        nav.columnconfigure(2, minsize=700)

        nav.grid(row=1, column=1, padx=20, pady=20, columnspan=3)
        ###

        businfo = ctk.CTkFrame(master=page, fg_color="#EDEDED")
        busname = ctk.CTkLabel(
            master=businfo, text=f"{win.busname}", font=("Roboto", 16)
        )
        dept = ctk.CTkLabel(
            master=businfo, text=f"Departs {win.depttime}", font=("Roboto", 16)
        )

        busname.grid(row=1, column=1)
        dept.grid(row=2, column=1)

        businfo.grid(row=2, column=1, rowspan=2, sticky="nw", padx=40)

        ##

        seats = ctk.CTkFrame(
            master=page,
            fg_color="#EDEDED",
            border_color="#000000",
            border_width=1,
            corner_radius=5,
        )

        for posy in range(8):
            seats_ref.append([])
            for posx in range(4):
                seat = ctk.CTkFrame(
                    master=seats,
                    fg_color="#E1E1E1",
                    width=40,
                    height=40,
                    corner_radius=2,
                )
                seat.grid(row=posy + 1, column=posx + 1, padx=10, pady=10, sticky="ne")
                seat.pack_propagate(0)

                seat.posx = posx
                seat.posy = posy

                seatnum = ctk.CTkLabel(
                    master=seat,
                    text=f"{posy + 1}{'ABCD'[posx]}",
                    font=("Roboto", 14),
                    text_color="grey",
                )
                seatnum.posx = posx
                seatnum.posy = posy

                seatnum.pack()

                def onclick(e):
                    global seats_remaining, total_seats
                    seat_id = f"{e.posy}{'ABCD'[e.posx]}"

                    if seat_id in booked_seats:
                        e.configure(fg_color="#A6D1A5")
                        return

                    if seat_id in selected_seats:
                        seats_remaining += 1
                        selected_seats.pop(selected_seats.index(seat_id))
                        e.configure(fg_color="#E1E1E1")
                        selected_txt.configure(
                            text=f"Selected {total_seats - seats_remaining} out of {total_seats} seats"
                        )
                        return

                    if seats_remaining > 0:
                        seats_remaining -= 1
                        selected_seats.append(f"{e.posy}{'ABCD'[e.posx]}")
                        e.configure(fg_color="#70DFF8")
                        selected_txt.configure(
                            text=f"Selected {total_seats - seats_remaining} out of {total_seats} seats"
                        )

                seat.bind("<Button-1>", lambda _, w=seat: onclick(w))
                seatnum.bind("<Button-1>", lambda _, w=seat: onclick(w))

                seats_ref[posy].append(seat)

        seats.columnconfigure(3, minsize=100)

        # seats.grid(row=2, column=2, rowspan=2)
        seats.place(relx=0.5, rely=0.5, anchor="center")

        selected_txt = ctk.CTkLabel(
            master=page,
            text=f"Selected 0 out of {seats_remaining} seats",
            font=("Roboto", 16),
        )
        selected_txt.place(relx=0.5, rely=0.95, anchor="center")
        ##

        rt_col = ctk.CTkFrame(master=page, fg_color="#EDEDED", height=600, width=200)
        rt_col.grid_propagate(0)

        passenger_cnt = ctk.CTkFrame(master=rt_col, fg_color="#EDEDED")
        adults_cnt = ctk.CTkLabel(
            master=passenger_cnt, text=f"Adults: {adults}", font=("Roboto", 16)
        )
        children_cnt = ctk.CTkLabel(
            master=passenger_cnt, text=f"Children: {children}", font=("Roboto", 16)
        )
        adults_cnt.grid(row=1, column=1)
        children_cnt.grid(row=2, column=1)
        passenger_cnt.grid(row=1, column=3, sticky="ne")

        ##

        key = ctk.CTkFrame(master=rt_col, fg_color="#EDEDED")

        avail = ctk.CTkFrame(master=key, fg_color="#EDEDED")
        avail_key = ctk.CTkFrame(
            master=avail, fg_color="#E1E1E1", width=30, height=30, corner_radius=3
        )
        avail_txt = ctk.CTkLabel(master=avail, text="Available", font=("Roboto", 16))
        avail_key.grid(row=1, column=1)
        avail_txt.grid(row=1, column=2, padx=4)
        avail.grid(row=1, column=1, sticky="w", pady=10)

        booked = ctk.CTkFrame(master=key, fg_color="#EDEDED")
        booked_key = ctk.CTkFrame(
            master=booked, fg_color="#A6D1A5", width=30, height=30, corner_radius=3
        )
        booked_txt = ctk.CTkLabel(master=booked, text="Booked", font=("Roboto", 16))
        booked_key.grid(row=1, column=1)
        booked_txt.grid(row=1, column=2, padx=4)
        booked.grid(row=2, column=1, sticky="w", pady=10)

        selected = ctk.CTkFrame(master=key, fg_color="#EDEDED")
        slcted_key = ctk.CTkFrame(
            master=selected, fg_color="#70DFF8", width=30, height=30, corner_radius=3
        )
        slcted_txt = ctk.CTkLabel(master=selected, text="Selected", font=("Roboto", 16))
        slcted_key.grid(row=1, column=1)
        slcted_txt.grid(row=1, column=2, padx=4)
        selected.grid(row=3, column=1, sticky="w", pady=10)

        key.grid(row=2, column=3, sticky="se")

        page.columnconfigure(2, minsize=700)

        def continue_func():
            if seats_remaining != 0:
                return

            win.selected_seats = selected_seats
            win.navigator.navigate_to("passenger_info")

        continue_btn = ctk.CTkButton(
            master=rt_col, text="Continue  >", height=40, command=continue_func
        )
        continue_btn.grid(row=3, column=3, pady=10)

        rt_col.grid(row=2, column=3, sticky="ne", rowspan=2)

    return "seat_select", page, on_mount, lambda: None
