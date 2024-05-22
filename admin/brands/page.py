import customtkinter as ctk
from widgets.table import Table
from widgets.image import load_image_ctk
from admin.brands.api import *
from admin.brands.edit import edit_brand
from admin.brands.create import create_brand


def BrandsPage(win, db, cursor):
    page = ctk.CTkFrame(
        master=win, width=1280, height=720, bg_color="#ececec", fg_color="#ececec"
    )
    page.pack_propagate(0)

    ## Create Table Component
    action_row = ctk.CTkFrame(master=page, fg_color="#ececec", width=900, height=50)

    table, refersh_callback = Table(
        page,
        "Brands",
        [
            ("ID", 300),
            ("Name", 300),
            ("[IMAGE]Logo", 300),
        ],
        fetch_brands(cursor),
        edit_brand,
        handle_sql_delete,
        db,
        cursor,
        null_data_text="No Brands Found",
        row_height=50,
    )

    title = ctk.CTkLabel(master=action_row, text="Brands", font=("Roboto", 20))
    add_brand = ctk.CTkButton(
        master=action_row,
        text="+  Add Brand",
        command=lambda: create_brand(win, db, cursor, refersh_callback),
    )

    def reload_func():
        return refersh_callback(fetch_brands(cursor))

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

    return "brands", page
