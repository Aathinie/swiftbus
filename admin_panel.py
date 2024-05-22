import customtkinter as ctk

from utils import correct_path
from tknav import Navigator

from admin.tableselect import TableSelectPage
from admin.users.page import UsersPage
from admin.brands.page import BrandsPage
from admin.bus.page import BusPage
from admin.locations.page import LocationsPage

from backend import *


def make_window():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme(correct_path("./theme.json"))

    window = ctk.CTk()
    window.title("SwiftBus Admin")
    window.geometry("1200x600")
    window.resizable(False, False)
    return window


def config_navigator(win, pages):
    nav = Navigator()
    for page in pages:
        nav.add_page(*page(win, connection, cursor))

    win.nav = nav
    return nav


def main():
    window = make_window()

    PAGES = [TableSelectPage, UsersPage, BrandsPage, BusPage, LocationsPage]
    nav = config_navigator(window, PAGES)

    nav.navigate_to("tableselect")

    window.mainloop()


if __name__ == "__main__":
    main()
