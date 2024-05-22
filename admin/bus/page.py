import customtkinter as ctk
from widgets.table import Table
from widgets.image import load_image_ctk
from admin.bus.api import *
from admin.bus.edit import edit_bus
from admin.bus.create import create_bus


def BusPage(win, db, cursor):
    page = ctk.CTkFrame(
        master=win, width=1200, height=720, bg_color="#ececec", fg_color="#ececec"
    )
    page.pack_propagate(0)

    ## Create Table Component
    action_row = ctk.CTkFrame(master=page, fg_color="#ececec", width=1000, height=50)

    table, refersh_callback = Table(
        page,
        "Brands",
        [
            ("ID", 150),
            ("Name", 150),
            ("[GETNAME:name,brands]Brand", 150),
            ("Decription", 300),
            ("[IMAGE]Image", 100),
            ("Per Km", 100),
            ("Seats", 100),
        ],
        fetch_bus(cursor),
        edit_bus,
        handle_sql_delete,
        db,
        cursor,
        null_data_text="No Busses Found",
        row_height=50,
    )

    title = ctk.CTkLabel(master=action_row, text="Bus", font=("Roboto", 20))
    add_bus= ctk.CTkButton(
        master=action_row,
        text="+  Add Bus",
        command=lambda: create_bus(win, db, cursor, refersh_callback),
    )

    def reload_func():
        return refersh_callback(fetch_bus(cursor))

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
    add_bus.place(relx=1, rely=0, anchor="ne")

    # spacing
    ctk.CTkLabel(master=page, text="").pack(pady=10)
    action_row.pack(pady=10)

    table.pack(pady=10)

    return "bus", page
