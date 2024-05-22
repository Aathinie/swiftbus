import customtkinter  # type:ignore

def SearchBox(parent, label, options):
    ENTRY_WIDTH = 410
    ENTRY_HEIGHT = 40

    search_widget = customtkinter.CTkFrame(
        master=parent, fg_color="transparent", width=ENTRY_WIDTH
    )

    def search(word, src, max_res_size=-1):
        matches = []

        for item in src:
            num_match = 0

            for i, char in enumerate(word.lower()):
                if (
                    (i < len(item) and char == item[i].lower())
                    or (i > 0 and i < len(item) and char == item[i - 1].lower())
                    or (i < len(item) - 1 and char == item[i + 1].lower())
                ):
                    num_match += 1

            if len(word) > 0 and num_match / len(word) > 0.6:
                matches.append(item)

        if max_res_size > 0 and len(matches) > max_res_size:
            matches = matches[:max_res_size]
        return matches

    search_label = customtkinter.CTkLabel(
        master=search_widget,
        text=label,
    )

    search_label.grid(row=1, column=1, sticky="w")
    search_label.cget("font").configure(size=16)

    optionmenu_var = customtkinter.StringVar(value="")  # set initial value

    def optionmenu_callback(choice):
        searchvar.set(choice)

        option_dropdown._values = []
        option_dropdown._dropdown_menu._values = []
        option_dropdown._dropdown_menu._add_menu_commands()
        option_dropdown._open_dropdown_menu()

        search_label.focus()

    option_dropdown = customtkinter.CTkOptionMenu(
        master=search_widget,
        values=[],
        command=optionmenu_callback,
        variable=optionmenu_var,
        width=ENTRY_WIDTH,
        height=ENTRY_HEIGHT,
    )
    option_dropdown._dropdown_menu.cget("font").configure(size=16)

    option_dropdown.grid(row=2, column=1)

    parent.update()

    x, y = option_dropdown.winfo_x(), option_dropdown.winfo_y()

    def handle_search(searchvar):
        search_term = searchvar.get()
        results = search(search_term, options, max_res_size=5)

        option_dropdown._values = results
        option_dropdown._dropdown_menu._values = results
        option_dropdown._dropdown_menu._add_menu_commands()
        option_dropdown._open_dropdown_menu()

        entry.focus()

    searchvar = customtkinter.StringVar()
    searchvar.trace_add(
        "write", lambda name, index, mode, var=searchvar: handle_search(var)
    )

    entry = customtkinter.CTkEntry(
        master=search_widget,
        textvariable=searchvar,
        width=ENTRY_WIDTH,
        height=ENTRY_HEIGHT,
    )

    entry.cget("font").configure(size=18)
    entry.place(x=x, y=y)

    return search_widget, searchvar
