import customtkinter as ctk
from widgets.image import load_image_ctk


def TableSelectPage(win, db, sql):
    page = ctk.CTkFrame(
        master=win, width=1200, height=600, bg_color="#ececec", fg_color="#ececec"
    )
    page.pack_propagate(0)

    def onmount():
        win.title("SwiftBus Admin - Select")

    frame = ctk.CTkFrame(master=page, bg_color="#ececec", fg_color="#ececec")

    def TableButton(table):
        table_btn = ctk.CTkButton(
            master=frame,
            text=f"\n{table}",
            image=load_image_ctk(f"./assets/{table.lower()}_icon.png", (30, 30)),
            compound="left",
            corner_radius=5,
            width=640,
            height=50,
            bg_color="white",
            fg_color="white",
            hover_color="#f3f3f3",
            text_color="black",
            font=("Roboto", 16),
            background_corner_colors=("#ececec",) * 4,
            command=lambda: win.nav.navigate_to(table.lower()),
        )
        return table_btn

    TableButton("Users").grid(row=1, column=1, padx=10, pady=10)
    TableButton("Brands").grid(row=2, column=1, padx=10, pady=10)
    TableButton("Bus").grid(row=3, column=1, padx=10, pady=10)
    TableButton("Locations").grid(row=4, column=1, padx=10, pady=10)
    TableButton("Routes").grid(row=5, column=1, padx=10, pady=10)
    TableButton("Bookings").grid(row=6, column=1, padx=10, pady=10)

    ctk.CTkLabel(
        master=page, text="", image=load_image_ctk("./assets/logo.png", (200, 0))
    ).place(relx=0.5, rely=0.07, anchor="center")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    return "tableselect", page, onmount, lambda: None
