import customtkinter as ctk
from admin.routes.api import *
from tkinter.filedialog import askopenfilename
from widgets.dropselect import DropSelect
import uuid

selected_days = []
day_buttons = []


def edit_route(win, db, cursor, _id, refresh_callback):
    global selected_days, day_buttons
    selected_days = []
    day_buttons = []


    window = ctk.CTkToplevel()
    window.transient(win)
    window.title("SwiftBus Admin - Edit Route")
    window.geometry("500x900")

    (
        uid,
        source,
        destination,
        distance,
        busID,
        days,
        timings,
        journeyTime,
    ) = fetch_route_by_id(cursor, _id)

    form_frame = ctk.CTkFrame(master=window, width=400, fg_color="transparent")

    ctk.CTkLabel(
        master=form_frame, text="Edit Route", font=("Roboto", 16, "bold")
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

    #####

    source_var = ctk.StringVar(master=form_frame)
    source_select, source_name_id_map = DropSelect(
        form_frame,
        cursor,
        "Source",
        "locations",
        "uid",
        "name",
        source_var,
    )

    source_select.grid(row=4, column=1, sticky="w", rowspan=2)

    source_var.set(
        list(source_name_id_map.keys())[list(source_name_id_map.values()).index(source)]
    )

    #####

    dest_var = ctk.StringVar(master=form_frame)
    dest_select, dest_name_id_map = DropSelect(
        form_frame,
        cursor,
        "Destination",
        "locations",
        "uid",
        "name",
        dest_var,
    )

    dest_select.grid(row=7, column=1, sticky="w", rowspan=2)

    dest_var.set(
        list(dest_name_id_map.keys())[
            list(dest_name_id_map.values()).index(destination)
        ]
    )

    #####

    distance_label = ctk.CTkLabel(
        master=form_frame, text="Distance", font=("Roboto", 16)
    )
    distance_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    distance_entry.insert(0, distance)
    distance_label.grid(row=10, column=1, sticky="w")
    distance_entry.grid(row=11, column=1, sticky="w")

    #####

    bus_var = ctk.StringVar(master=form_frame)
    bus_select, bus_name_id_map = DropSelect(
        form_frame,
        cursor,
        "Bus",
        "bus",
        "uid",
        "name",
        bus_var,
    )

    bus_select.grid(row=13, column=1, sticky="w", rowspan=2)

    bus_var.set(
        list(bus_name_id_map.keys())[list(bus_name_id_map.values()).index(busID)]
    )

    #####

    timing_label = ctk.CTkLabel(
        master=form_frame,
        text="Timings [24 hour format, seperated by ;]",
        font=("Roboto", 16),
    )

    timing_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    timing_entry.insert(0, timings)
    timing_label.grid(row=16, column=1, sticky="w")
    timing_entry.grid(row=17, column=1, sticky="w")

    #####

    journey_time_label = ctk.CTkLabel(
        master=form_frame, text="Journey Time [hours]", font=("Roboto", 16)
    )

    journey_time_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    journey_time_entry.insert(0, journeyTime)
    journey_time_label.grid(row=19, column=1, sticky="w")
    journey_time_entry.grid(row=20, column=1, sticky="w")

    #####

    days_label = ctk.CTkLabel(master=form_frame, text="Days", font=("Roboto", 16))
    days_row = ctk.CTkFrame(master=form_frame, width=400, height=50, fg_color="#F2F2F2")

    selected_days = days.split(";")

    for idx, d in enumerate(["Su", "M", "Tu", "W", "Th", "F", "Sa"]):

        def onclick(index, day):
            if day in selected_days:
                selected_days.pop(selected_days.index(day))
                day_buttons[index].configure(fg_color="#BCBCBC", hover_color="#BCBCBC")
            else:
                selected_days.append(day)
                day_buttons[index].configure(fg_color="#3b8ed0", hover_color="#3b8ed0")

        day_btn = ctk.CTkButton(
            master=days_row,
            text=d,
            height=50,
            width=50,
            fg_color="#3b8ed0" if d in selected_days else "#BCBCBC",
            hover_color="#3b8ed0" if d in selected_days else "#BCBCBC",
            command=lambda x=idx, y=d: onclick(x, y),
        )

        day_buttons.append(day_btn)

        day_btn.grid(
            row=1,
            column=idx + 1,
            padx=4.1,
        )

    days_label.grid(row=19, column=1, sticky="w")
    days_row.grid(row=20, column=1, sticky="w")

    #####

    submit = ctk.CTkButton(
        master=form_frame,
        text="Update",
        height=40,
        text_color="#ffffff",
        command=lambda: handle_sql_edit(
            window,
            db,
            cursor,
            str(uid),
            source_name_id_map[source_var.get()],
            dest_name_id_map[dest_var.get()],
            distance_entry.get(),
            bus_name_id_map[bus_var.get()],
            ";".join(selected_days),
            timing_entry.get(),
            journey_time_entry.get(),
            refresh_callback,
        ),
    )

    submit.grid(row=22, column=1, sticky="we")

    for i in [3, 6, 9, 12, 15, 18, 21]:
        form_frame.rowconfigure(i, minsize=20)

    form_frame.place(relx=0.5, rely=0.5, anchor="center")
