import customtkinter as ctk
from backend import cursor
import datetime


def ResultsPage(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="white")
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

        showing_label.configure(
            text=f"Showing busses from {source} to {destination} on {date}"
        )

        for (
            uid,
            _src,
            _dest,
            dist,
            bus,
            days,
            timings,
            jounreyTimeHrs,
        ) in search_results:
            timings = timings.split(";")

            for timing in timings:
                detail_frame = ctk.CTkFrame(
                    master=page,
                    width=1000,
                    bg_color="#e0e0e0",
                )
                source_frame = ctk.CTkFrame(master=detail_frame)
                ctk.CTkLabel(
                    master=source_frame, text="Source", font=("Roboto", 16, "bold")
                ).grid(row=1, column=1, sticky="w")
                ctk.CTkLabel(
                    master=source_frame,
                    text=source.strip(),
                    font=("Roboto", 24, "bold"),
                ).grid(row=2, column=1, sticky="w")

                dest_frame = ctk.CTkFrame(master=detail_frame)
                ctk.CTkLabel(
                    master=dest_frame, text="Destination", font=("Roboto", 16, "bold")
                ).grid(row=1, column=1, sticky="w")
                ctk.CTkLabel(
                    master=dest_frame,
                    text=destination.strip(),
                    font=("Roboto", 24, "bold"),
                ).grid(row=2, column=1, sticky="w")

                distance_frame = ctk.CTkFrame(master=detail_frame)
                ctk.CTkLabel(
                    master=distance_frame, text="Distance", font=("Roboto", 16, "bold")
                ).grid(row=1, column=1, sticky="w")
                ctk.CTkLabel(
                    master=distance_frame, text=dist, font=("Roboto", 24, "bold")
                ).grid(row=2, column=1, sticky="w")

                timing_frame = ctk.CTkFrame(master=detail_frame)
                ctk.CTkLabel(
                    master=timing_frame, text="Timing", font=("Roboto", 16, "bold")
                ).grid(row=1, column=1, sticky="w")
                ctk.CTkLabel(
                    master=timing_frame,
                    text=timing.strip(),
                    font=("Roboto", 24, "bold"),
                ).grid(row=2, column=1, sticky="w")

                source_frame.grid(row=1, column=1, padx=20)
                dest_frame.grid(row=1, column=2, padx=20)
                distance_frame.grid(row=1, column=3, padx=20)
                timing_frame.grid(row=1, column=4, padx=20)

                detail_frame.pack(pady=10)

    showing_label = ctk.CTkLabel(master=page, text="", font=("Roboto", 20))
    showing_label.pack(anchor="n", pady=30)

    return "results", page, on_mount, lambda: None
