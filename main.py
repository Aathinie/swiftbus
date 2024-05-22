import customtkinter as ctk
from tknav import Navigator

from utils import correct_path

from pages.login import LoginPage
from pages.singup import SingupPage
from pages.home import HomePage

def make_window():
    window = ctk.CTk()
    window.title("SwiftBus")
    window.geometry("1200x600")

    window.resizable(False, False)

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    # ctk.set_default_color_theme(correct_path("./theme.json"))

    return window


def config_navigator(win, pages):
    nav = Navigator()
    for page in pages:
        page_info = page(win)
        if len(page_info) == 2:
            nav.add_page(page_name=page_info[0], page_widget=page_info[1])
        else:
            nav.add_page(
                page_name=page_info[0],
                page_widget=page_info[1],
                on_mount=page_info[2],
                on_destroy=page_info[3],
            )

    win.nav = nav
    return nav


def main():
    window = make_window()

    PAGES = [
        LoginPage,
        SingupPage,
        HomePage
    ]
    nav = config_navigator(window, PAGES)

    nav.navigate_to("home")

    window.mainloop()


if __name__ == "__main__":
    main()
