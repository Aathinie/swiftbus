import customtkinter as ctk
from admin.locations.api import *


def edit_location(win, db, cursor, _id, refresh_callback):
    window = ctk.CTkToplevel()
    window.transient(win)
    window.title("SwiftBus Admin - Edit Location")
    window.geometry("500x600")

    uid, name, district, state, country = fetch_location_by_id(cursor, _id)

    form_frame = ctk.CTkFrame(master=window, width=400, fg_color="transparent")

    ctk.CTkLabel(
        master=form_frame, text="Edit Location", font=("Roboto", 16, "bold")
    ).grid(row=0, column=1, sticky="we")

    id_label = ctk.CTkLabel(master=form_frame, text="ID", font=("Roboto", 14))
    id_entry = ctk.CTkEntry(
        master=form_frame,
        placeholder_text=str(uid),
        width=400,
        height=40,
        font=("Roboto", 16),
    )
    id_entry.configure(state="disabled")
    id_label.grid(row=1, column=1, sticky="w")
    id_entry.grid(row=2, column=1, sticky="we")

    name_label = ctk.CTkLabel(master=form_frame, text="Name", font=("Roboto", 14))
    name_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    name_label.grid(row=4, column=1, sticky="w")
    name_entry.grid(row=5, column=1, sticky="we")
    name_entry.insert(0, name)

    #####

    district_label = ctk.CTkLabel(
        master=form_frame, text="District", font=("Roboto", 14)
    )
    district_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    district_label.grid(row=7, column=1, sticky="w")
    district_entry.grid(row=8, column=1, sticky="we")
    district_entry.insert(0, district)

    #####

    state_label = ctk.CTkLabel(master=form_frame, text="State", font=("Roboto", 14))
    state_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    state_label.grid(row=10, column=1, sticky="w")
    state_entry.grid(row=11, column=1, sticky="we")
    state_entry.insert(0, state)

    #####

    country_label = ctk.CTkLabel(master=form_frame, text="Country", font=("Roboto", 14))
    country_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    country_label.grid(row=13, column=1, sticky="w")
    country_entry.grid(row=14, column=1, sticky="we")
    country_entry.insert(0, country)

    #####

    submit = ctk.CTkButton(
        master=form_frame,
        text="Edit Location",
        height=40,
        text_color="#ffffff",
        command=lambda: handle_sql_create(
            window,
            db,
            cursor,
            str(uid),
            name_entry.get().strip(),
            district_entry.get().strip(),
            state_entry.get().strip(),
            country_entry.get().strip(),
            refresh_callback,
        ),
    )

    submit.grid(row=16, column=1, sticky="we")

    for i in [3, 6, 9, 12, 15]:
        form_frame.rowconfigure(i, minsize=20)

    form_frame.place(relx=0.5, rely=0.5, anchor="center")
