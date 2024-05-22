import customtkinter  # type:ignore
from widgets.image import load_image_ctk
import datetime as dt

selected_date = None


def CalendarWidget(parent, callback):
    global selected_date

    today = dt.date.today()
    year, month_index = today.year, today.month - 1

    cal_frame = customtkinter.CTkFrame(master=parent, width=350, height=400, fg_color="white")

    MONTHS = [
        ("January", 31),
        ("February", 28),
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31),
    ]

    DAYS = "SMTWTFS"

    month, ndays = MONTHS[month_index]

    month_row = customtkinter.CTkFrame(
        master=cal_frame, fg_color="#3B8ED0", corner_radius=0, height=50
    )

    def goto_prev_month():
        nonlocal month_index, year, month_label
        month_index -= 1

        if month_index < 0:
            month_index = 11
            year -= 1

        month, ndays = MONTHS[month_index]
        if month == "February":
            ndays = 29 if year % 4 == 0 else 28

        month_label.configure(text=f"{month} {year}")
        generate_date_grid(first_day(), ndays)

    def goto_next_month():
        nonlocal month_index, year, month_label
        month_index += 1

        if month_index > 11:
            month_index = 0
            year += 1

        month_label.configure(text=f"{MONTHS[month_index][0]} {year}")
        generate_date_grid(first_day(), MONTHS[month_index][1])


    month_label = customtkinter.CTkLabel(
        master=month_row, text=f"{month}  {year}", text_color="white", width=280
    )
    month_label.cget("font").configure(size=18)
    month_label.grid(row=1, column=2, pady=8)

    prev_month = customtkinter.CTkButton(
        master=month_row,
        fg_color="#347fba",
        corner_radius=0,
        width=35,
        text="",
        image=load_image_ctk("./assets/left_arr.png", (7, 10)),
        command=goto_prev_month,
    )
    prev_month.grid(row=1, column=1, sticky="nsw")


    next_month = customtkinter.CTkButton(
        master=month_row,
        fg_color="#347fba",
        corner_radius=0,
        width=35,
        text="",
        image=load_image_ctk("./assets/right_arr.png", (7, 10)),
        command=goto_next_month,
    )
    next_month.grid(row=1, column=3, sticky="nse")

    month_row.grid(row=1, column=1, sticky="nwe")



    def first_day():
        fd = dt.date(year, month_index + 1, 1).weekday()
        fd += 1
        if fd == 7:
            fd = 0
        return fd

    day_row = customtkinter.CTkFrame(master=cal_frame, fg_color="white")
    date_row = customtkinter.CTkFrame(master=cal_frame, fg_color="white")

    for i, day in enumerate(DAYS):
        day_label = customtkinter.CTkLabel(master=day_row, text=day)

        day_row.columnconfigure(i + 1, minsize=50)
        date_row.columnconfigure(i + 1, minsize=50)

        day_label.grid(row=1, column=i + 1)

    day_row.grid(row=2, column=1, sticky="nwe")

    def close(date, month, year):
        global selected_date
        selected_date = None
        callback((date, month, year))
        parent.destroy()

    btn = customtkinter.CTkButton(
        master=cal_frame,
        text=f"Select Date: {selected_date.cget('text')}/{month_index + 1}/{year}"
        if selected_date
        else "Select Date",
        command=lambda: close(selected_date.cget("text"), month_index + 1, year),
    )

    def generate_date_grid(first_day, ndays):
        for _, child in date_row.children.items():
            child.grid_forget()

        date_row.children.clear()

        iday = 1

        for y in range(6):
            date_row.rowconfigure(y + 1, minsize=50)

            for x in range(7):
                if iday > ndays:
                    break

                if y == 0:
                    if x == 0:
                        empty = customtkinter.CTkLabel(master=date_row, text="")
                        empty.grid(
                            row=1, column=1, columnspan=7 - first_day, sticky="w"
                        )
                    if x < first_day:
                        continue

                date_button = customtkinter.CTkButton(
                    master=date_row,
                    text=iday,
                    text_color="black",
                    fg_color="#f1f1f1",
                    bg_color="transparent",
                    hover_color="lightgray",
                    width=50,
                    height=50,
                )

                def on_click(event):
                    global selected_date
                    nonlocal btn
                    if selected_date is not None:
                        selected_date.configure(
                            fg_color="#f1f1f1",
                            text_color="black",
                            hover_color="lightgray",
                        )

                    selected_date = event.widget.master

                    selected_date.configure(
                        fg_color="#3B8ED0", text_color="white", hover_color="#347fba"
                    )
                    btn.configure(
                        text=f"Select Date: {selected_date.cget('text')}/{month_index + 1}/{year}"
                        if selected_date
                        else "Select Date"
                    )

                date_button.bind("<Button 1>", on_click)

                date_button.grid(row=y + 1, column=x + 1)
                # date_frame.grid(row=y + 1, column=x + 1)

                iday += 1

    generate_date_grid(first_day(), ndays)
    date_row.grid(row=3, column=1, sticky="nwe")
    btn.grid(row=4, column=1, sticky="swe")

    return cal_frame


def DateSelectWidget(parent, label, callback):
    widget_frame = customtkinter.CTkFrame(master=parent, fg_color="transparent")

    date_label = customtkinter.CTkLabel(master=widget_frame, text=label)
    date_label.cget("font").configure(size=16)
    date_label.grid(row=1, column=1, sticky="w")

    display_frame = customtkinter.CTkFrame(
        master=widget_frame,
        width=300,
        height=40,
        fg_color="white",
        border_width=2,
        bg_color="transparent",
        border_color="darkgray",
        background_corner_colors=("#EBEBEB", "#3B8ED0", "#3B8ED0", "#EBEBEB"),
    )

    selected_date_label = customtkinter.CTkLabel(
        master=display_frame, text="18/04/2024"
    )
    selected_date_label.grid(row=1, column=1, sticky="w", padx=10)
    selected_date_label.cget("font").configure(size=16)
    display_frame.rowconfigure(1, minsize=40)
    display_frame.columnconfigure(1, minsize=300)

    display_frame.grid(row=2, column=1)

    def open_select():
        top = customtkinter.CTkToplevel(parent)
        top.geometry("350x400")

        def onselect(date):
            selected_date_label.configure(text=f"{date[0]}/{date[1]}/{date[2]}")
            callback(f"{date[0]}/{date[1]}/{date[2]}")

        calendar_widget = CalendarWidget(top, onselect)
        calendar_widget.pack()

        def onclose():
            global selected_date
            selected_date = None
            calendar_widget.destroy()
            top.destroy()

        top.protocol("WM_DELETE_WINDOW", onclose)

    select_btn = customtkinter.CTkButton(
        master=widget_frame,
        height=40,
        width=40,
        command=open_select,
        text="",
        background_corner_colors=("#3B8ED0", "white", "white", "#3B8ED0"),
        bg_color="transparent",
        image=load_image_ctk("./assets/calendar.png", (20, 20)),
    )

    widget_frame.columnconfigure(1, minsize=170)
    select_btn.grid(row=2, column=2)

    return widget_frame
