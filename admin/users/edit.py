import customtkinter as ctk
from admin.users.api import *

def edit_user(_, db, cursor, _id, refresh_callback):
    window = ctk.CTkToplevel()
    window.title("Ubran Utopia Admin - Edit User")
    window.geometry("500x500")

    uid, name, email, password = fetch_user_by_id(cursor, _id)

    form_frame = ctk.CTkFrame(master=window, width=400, fg_color="transparent")

    ctk.CTkLabel(master=form_frame, text="Edit User", font=("Roboto", 16, "bold")).grid(
        row=0, column=1, sticky="we"
    )

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
    name_entry.insert(0, name)
    name_label.grid(row=4, column=1, sticky="w")
    name_entry.grid(row=5, column=1, sticky="we")

    email_label = ctk.CTkLabel(master=form_frame, text="Email", font=("Roboto", 14))
    email_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    email_entry.insert(0, email)
    email_label.grid(row=7, column=1, sticky="w")
    email_entry.grid(row=8, column=1, sticky="we")

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
            name_entry.get().strip(),
            email_entry.get().strip(),
            password,
            refresh_callback,
        ),
    )

    submit.grid(row=13, column=1, sticky="we")

    for i in [3, 6, 9, 12]:
        form_frame.rowconfigure(i, minsize=20)

    form_frame.place(relx=0.5, rely=0.5, anchor="center")
