import customtkinter as ctk
from widgets.table import Table
from widgets.image import load_image_ctk
from admin.routes.api import *
from admin.routes.edit import edit_route
from admin.routes.create import create_route


def RoutesPage(win, db, cursor):
    page = ctk.CTkFrame(
        master=win, width=1200, height=720, bg_color="#ececec", fg_color="#ececec"
    )
    page.pack_propagate(0)

    ## Create Table Component
    action_row = ctk.CTkFrame(master=page, fg_color="#ececec", width=900, height=50)

    table, refersh_callback = Table(
        page,
        "Routes",
        [
            ("ID", 50),
            ("[GETNAME:name,locations]Source", 100),
            ("[GETNAME:name,locations]Destination", 100),
            ("Distance", 100),
            ("[GETNAME:name,bus]Bus", 200),
            ("Days", 200),
            ("Timings", 100),
            ("Duration", 50),
        ],
        fetch_routes(cursor),
        edit_route,
        handle_sql_delete,
        db,
        cursor,
        null_data_text="No Routes Found",
        row_height=50,
    )

    title = ctk.CTkLabel(master=action_row, text="Routes", font=("Roboto", 20))
    add_brand = ctk.CTkButton(
        master=action_row,
        text="+  Add Route",
        command=lambda: create_route(win, db, cursor, refersh_callback),
    )

    def reload_func():
        return refersh_callback(fetch_routes(cursor))

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
    add_brand.place(relx=1, rely=0, anchor="ne")

    # spacing
    ctk.CTkLabel(master=page, text="").pack(pady=10)
    action_row.pack(pady=10)

    table.pack(pady=10)

    return "routes", page
