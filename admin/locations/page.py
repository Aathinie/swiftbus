import customtkinter as ctk
from widgets.table import Table
from widgets.image import load_image_ctk
from admin.locations.api import *
from admin.locations.edit import edit_location
from admin.locations.create import create_location


def LocationsPage(win, db, cursor):
    page = ctk.CTkFrame(
        master=win, width=1280, height=720, bg_color="#ececec", fg_color="#ececec"
    )
    page.pack_propagate(0)

    ## Create Table Component
    action_row = ctk.CTkFrame(master=page, fg_color="#ececec", width=900, height=50)

    table, refersh_callback = Table(
        page,
        "Locations",
        [
            ("ID", 300),
            ("Name", 150),
            ("District", 150),
            ("State", 150),
            ("Country", 150),
        ],
        fetch_locations(cursor),
        edit_location,
        handle_sql_delete,
        db,
        cursor,
        null_data_text="No Locations Found",
        row_height=50,
    )

    title = ctk.CTkLabel(master=action_row, text="Locations", font=("Roboto", 20))
    add_location = ctk.CTkButton(
        master=action_row,
        text="+  Add Location",
        command=lambda: create_location(win, db, cursor, refersh_callback),
    )

    def reload_func():
        return refersh_callback(fetch_locations(cursor))

    refresh = ctk.CTkButton(
        master=action_row,
        text="",
        width=25,
        height=25,
        fg_color="#ececec",
        hover_color="#ececec",
        image=load_image_ctk("./assets/reload_icon.png", (25, 25)),
        command=reload_func,
    )

    backbtn = ctk.CTkButton(
        master=action_row,
        text="",
        width=25,
        height=25,
        fg_color="#ececec",
        hover_color="#ececec",
        image=load_image_ctk("./assets/back_icon.png", (10, 19)),
        command=lambda: win.nav.navigate_to("tableselect"),
    )

    backbtn.place(relx=0, rely=0.03, anchor="nw")
    title.place(relx=0.05, rely=0, anchor="nw")
    refresh.place(relx=0.845, rely=0, anchor="ne")
    add_location.place(relx=1, rely=0, anchor="ne")

    # spacing
    ctk.CTkLabel(master=page, text="").pack(pady=10)
    action_row.pack(pady=10)

    table.pack(pady=10)

    return "locations", page
