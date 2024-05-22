import customtkinter as ctk

from widgets.image import load_image_ctk, ImageButton
from widgets.search import SearchBox
from widgets.ctkcalendar import DateSelectWidget


def HomePage(win):
    page = ctk.CTkFrame(master=win, width=1200, height=600, fg_color="white")

    def onmount():
        win.title("SwiftBus - Home")

    def ondestroy():
        pass

    ####

    nav = ctk.CTkFrame(master=page, width=900, fg_color="white")

    logo = ctk.CTkLabel(
        master=nav, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
    )
    logo.place(relx=0.05, rely=0.03, anchor="nw")

    nav.place(relx=0, rely=0.03, anchor="nw")

    ####

    search = ctk.CTkFrame(master=page, width=900, height=240, fg_color="white")

    search.place(relx=0.5, rely=0.35, anchor="center")
    search.grid_propagate(0)

    search.rowconfigure(2, minsize=20)
    # search.rowconfigure(4, minsize=20)

    search.columnconfigure(2, minsize=80)

    ####

    source_widget, source_var = SearchBox(search, "Source", [])
    source_widget.grid(row=1, column=1, sticky="w")

    def handle_swap():
        dest = dest_var.get()
        dest_var.set(source_var.get())
        source_var.set(dest)
        logo.focus()

    swap = ImageButton(
        search, "./assets/swap.png", (20, 20), padx=25, pady=25, callback=handle_swap
    )
    swap.grid(row=1, column=2, sticky="s")

    dest_widget, dest_var = SearchBox(search, "Destination", [])
    dest_widget.grid(row=1, column=3, sticky="w")

    ####

    dates = ctk.CTkFrame(master=search, width=900, height=80, fg_color="white")
    dates.grid_propagate(0)

    #####

    departure_stringvar = ctk.StringVar(master=dates, value="")
    departure = DateSelectWidget(dates, "Date Of Departure", departure_stringvar.set)
    departure.grid(row=1, column=1, sticky="w")

    #####

    adult_count_frame = ctk.CTkFrame(master=dates, fg_color="white", width=230)
    adult_count_title = ctk.CTkLabel(
        master=adult_count_frame, text="Adults", font=("Roboto", 16)
    )
    adult_count_entry = ctk.CTkEntry(
        master=adult_count_frame, height=40, width=230, font=("Roboto", 16)
    )

    adult_count_title.grid(row=1, column=1, sticky="w")
    adult_count_entry.grid(row=2, column=1, sticky="w")

    adult_count_frame.grid(row=1, column=2, sticky="w", padx=40)

    #####

    child_count_frame = ctk.CTkFrame(master=dates, fg_color="white", width=230)
    child_count_title = ctk.CTkLabel(
        master=child_count_frame, text="Children", font=("Roboto", 16)
    )
    child_count_entry = ctk.CTkEntry(
        master=child_count_frame, height=40, width=230, font=("Roboto", 16)
    )

    child_count_title.grid(row=1, column=1, sticky="w")
    child_count_entry.grid(row=2, column=1, sticky="w")

    child_count_frame.grid(row=1, column=3, sticky="w", padx=10)

    #####

    dates.grid(row=3, column=1, columnspan=3)

    ####

    find = ctk.CTkButton(
        master=search,
        text="  Find My Ride",
        image=load_image_ctk("./assets/search_icon.png", (25, 0)),
        width=900,
        height=50,
        font=("Roboto", 16)
    )
    find.grid(row=4, column=1, columnspan=3, sticky="nw", pady=20)

    ####

    return "home", page, onmount, ondestroy
