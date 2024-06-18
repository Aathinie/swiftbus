import customtkinter as ctk
from admin.bus.api import *
from tkinter.filedialog import askopenfilename
from widgets.image_preview import ImagePreview
from widgets.dropselect import DropSelect



def edit_bus(win, db, cursor, _id, refresh_callback):
    window = ctk.CTkToplevel()
    window.transient(win)
    window.title("SwiftBus Admin - Edit Bus")
    window.geometry("500x700")

    uid, name, brand, description, image, perkm, seats = fetch_bus_by_id(cursor, _id)

    form_frame = ctk.CTkFrame(master=window, width=400, fg_color="transparent")

    ctk.CTkLabel(
        master=form_frame, text="Edit Bus", font=("Roboto", 16, "bold")
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

    name_label = ctk.CTkLabel(master=form_frame, text="Name", font=("Roboto", 14))
    name_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    name_label.grid(row=4, column=1, sticky="w")
    name_entry.grid(row=5, column=1, sticky="we")
    name_entry.insert(0, name)

    #####

    desc_label = ctk.CTkLabel(master=form_frame, text="Decription", font=("Roboto", 14))
    desc_entry = ctk.CTkEntry(
        master=form_frame, width=400, height=40, font=("Roboto", 16)
    )
    desc_label.grid(row=7, column=1, sticky="w")
    desc_entry.grid(row=8, column=1, sticky="we")
    desc_entry.insert(0, description)

    #####

    def get_image(store, callback):
        store.set(askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")]))
        callback(store.get())

    bus_image_label = ctk.CTkLabel(master=form_frame, text="Image")
    bus_image_select = ctk.CTkFrame(master=form_frame, fg_color="transparent")
    bus_image_preview, bus_preview_set = ImagePreview(bus_image_select, 50, image)

    bus_image_store = ctk.StringVar(value=None, name="bus_image_store")

    bus_image_button = ctk.CTkButton(
        master=bus_image_select,
        text="Select Image",
        width=100,
        height=40,
        font=("Roboto", 16),
        command=lambda: get_image(bus_image_store, bus_preview_set),
    )

    bus_image_preview.grid(row=1, column=1, sticky="w")
    bus_image_button.grid(row=1, column=2, sticky="w")

    bus_image_label.grid(row=10, column=1, sticky="w")
    bus_image_select.grid(row=11, column=1, sticky="w")


    #####

    row = ctk.CTkFrame(
        master=form_frame, width=400, fg_color="#ffffff", corner_radius=0
    )

    row.columnconfigure(1, minsize=200)
    row.columnconfigure(2, minsize=200)

    perkm_label = ctk.CTkLabel(master=row, text="Per Km")
    perkm_entry = ctk.CTkEntry(master=row, width=180, height=40)
    perkm_label.grid(row=1, column=1, sticky="w")
    perkm_entry.grid(row=2, column=1, sticky="w")
    perkm_entry.insert(0, perkm)

    seats_label = ctk.CTkLabel(master=row, text="Seats")
    seats_entry = ctk.CTkEntry(master=row, width=200, height=40)
    seats_label.grid(row=1, column=2, sticky="w")
    seats_entry.grid(row=2, column=2, sticky="w")
    seats_entry.insert(0, seats)

    row.grid(row=13, rowspan=2, column=1, sticky="w")

    #####

    brand_var = ctk.StringVar(master=form_frame)
    brand_select, brand_name_id_map = DropSelect(
        form_frame,
        cursor,
        "Brand",
        "brands",
        "uid",
        "name",
        brand_var,
    )

    brand_select.grid(row=16, column=1, sticky="w", rowspan=2)

    brand_var.set(
        list(brand_name_id_map.keys())[list(brand_name_id_map.values()).index(brand)]
    )

    #####

    submit = ctk.CTkButton(
        master=form_frame,
        text="Edit Bus",
        height=40,
        text_color="#ffffff",
        command=lambda: handle_sql_create(
            window,
            db,
            cursor,
            str(uid),
            name_entry.get().strip(),
            brand_name_id_map[brand_var.get()],
            desc_entry.get().strip(),
            bus_image_store.get(),
            perkm_entry.get(),
            seats_entry.get(),
            refresh_callback,
        ),
    )

    submit.grid(row=19, column=1, sticky="we")

    for i in [3, 6, 9, 12, 15, 18]:
        form_frame.rowconfigure(i, minsize=20)

    form_frame.place(relx=0.5, rely=0.5, anchor="center")
