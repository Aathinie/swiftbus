import customtkinter as ctk
from admin.brands.api import *
from widgets.image_preview import ImagePreview
from tkinter.filedialog import askopenfilename


def edit_brand(_, db, cursor, _id, refresh_callback):
    window = ctk.CTkToplevel()
    window.transient(_)
    window.title("SwiftBus Admin - Edit Brand")
    window.geometry("500x500")

    uid, name, logo = fetch_brand_by_id(cursor, _id)

    form_frame = ctk.CTkFrame(master=window, width=400, fg_color="transparent")

    ctk.CTkLabel(
        master=form_frame, text="Edit Brand", font=("Roboto", 16, "bold")
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
    name_entry.insert(0, name)
    name_label.grid(row=4, column=1, sticky="w")
    name_entry.grid(row=5, column=1, sticky="we")

    #####

    def get_image(store, callback):
        store.set(askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")]))
        callback(store.get())

    brand_image_label = ctk.CTkLabel(master=form_frame, text="Logo")
    brand_image_select = ctk.CTkFrame(master=form_frame, fg_color="transparent")
    brand_image_preview, brand_preview_set = ImagePreview(brand_image_select, 50, logo)

    brand_image_store = ctk.StringVar(value=logo, name="brand_image_store")

    brand_image_button = ctk.CTkButton(
        master=brand_image_select,
        text="Select Image",
        width=100,
        height=40,
        font=("Roboto", 16),
        command=lambda: get_image(brand_image_store, brand_preview_set),
    )

    brand_image_preview.grid(row=1, column=1, sticky="w")
    brand_image_button.grid(row=1, column=2, sticky="w")

    brand_image_label.grid(row=7, column=1, sticky="w")
    brand_image_select.grid(row=8, column=1, sticky="w")

    #####

    submit = ctk.CTkButton(
        master=form_frame,
        text="Edit Brand",
        height=40,
        text_color="#ffffff",
        command=lambda: handle_sql_create(
            window,
            db,
            cursor,
            str(uid),
            name_entry.get().strip(),
            brand_image_store.get().strip(),
            refresh_callback,
        ),
    )

    submit.grid(row=13, column=1, sticky="we")

    for i in [3, 6, 9, 12]:
        form_frame.rowconfigure(i, minsize=20)

    form_frame.place(relx=0.5, rely=0.5, anchor="center")
