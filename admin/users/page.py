import customtkinter as ctk
from widgets.table import Table
from widgets.image import load_image_ctk
from admin.users.api import *
from admin.users.edit import edit_user
from admin.users.create import create_user


def UsersPage(win, db, cursor):
    page = ctk.CTkFrame(
        master=win, width=1280, height=720, bg_color="#ececec", fg_color="#ececec"
    )
    page.pack_propagate(0)

    ## Create Table Component
    action_row = ctk.CTkFrame(master=page, fg_color="#ececec", width=900, height=50)

    table, refersh_callback = Table(
        page,
        "Users",
        [
            ("ID", 300),
            ("Name", 300),
            ("Email", 300),
        ],
        fetch_users(cursor),
        edit_user,
        handle_sql_delete,
        db,
        cursor,
        null_data_text="No Users Found",
        row_height=50,
    )

    title = ctk.CTkLabel(master=action_row, text="Users", font=("Roboto", 20))
    add_user = ctk.CTkButton(
        master=action_row,
        text="+  Add User",
        command=lambda: create_user(db, cursor, refersh_callback),
    )

    def reload_func():
        return refersh_callback(fetch_users(cursor))

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
    add_user.place(relx=0.95, rely=0, anchor="ne")

    # spacing
    ctk.CTkLabel(master=page, text="").pack(pady=10)
    action_row.pack(pady=10)

    table.pack(pady=10)

    return "users", page
