import customtkinter as ctk
from backend import cursor
from widgets.image import load_image_ctk
import datetime
from widgets.bus_card import BusCard


def ResultsPage(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="#EDEDED")
    page.pack_propagate(0)

    source = destination = date = adults = children = None
    search_results = []

    def on_mount():
        nonlocal source, destination, date, adults, children, search_results
        sourceid, source, destinationid, destination, date, adults, children = tuple(
            open("data", "r").readlines()
        )

        d, m, y = tuple(date.split("/"))
        day = ["M", "Tu", "W", "Th", "F", "Sa", "Su"][
            datetime.datetime(int(y), int(m), int(d)).weekday()
        ]

        cursor.execute(
            f"select * from routes where source='{sourceid.strip()}' and destination='{destinationid.strip()}' and days like '%{day.strip()};%' "
        )

        search_results = cursor.fetchall()

        ###
        nav = ctk.CTkFrame(master=page, width=900, fg_color="#EDEDED")

        logo = ctk.CTkLabel(
            master=nav, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
        )
        logo.grid(row=1, column=1, padx=40)
        
        back = ctk.CTkButton(master=nav, text="< Back", command=lambda:win.navigator.navigate_to("home"))
        back.grid(row=1, column=3, padx=40, sticky="ne")

        nav.columnconfigure(2, minsize=700)
        nav.grid(row=1, column=1, padx=20, pady=20)
        ###

        data = []

        for result in search_results:
            uid, _, _, dist, bus, _, timings, jounreyTimeHrs = result
            data.append((uid, dist, bus, timings, jounreyTimeHrs))

        n = 1

        results = ctk.CTkFrame(
            master=page,
        )

        for (
            uid,
            dist,
            bus,
            timings,
            jounreyTimeHrs,
        ) in data:
            timings = timings.split(";")

            for timing in timings:
                card = BusCard(
                    cursor, results, uid, source, destination, dist, timing, bus, win
                )
                card.grid(row=n, column=1, sticky="we", pady=10)
                n += 1

        results.grid(row=2, column=1)

    return "results", page, on_mount, lambda: None
