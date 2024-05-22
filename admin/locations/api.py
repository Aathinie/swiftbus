import customtkinter as ctk
import mysql.connector
from utils import encrypt

# Table Schema:
#   uid varchar(36) not null primary key,
#   name varchar(255) not null,
#   district varchar(255) not null unique,
#   state varchar(255) not null unique,
#   country varchar(255) not null unique,


def fetch_locations(cursor):
    cursor.execute("select * from locations")
    return cursor.fetchall()


def fetch_location_by_id(cursor, id):
    cursor.execute(f"select * from locations where uid='{id}'")
    return cursor.fetchone()


def handle_sql_create(
    window, db, cursor, uid, name, district, state, country, refresh_callback
):
    if not (len(uid) or len(name) or len(district) or len(country) or len(state)):
        err = ctk.CTkToplevel(window)
        err.title("SwiftBus Admin - Error")
        err.geometry("200x100")
        ctk.CTkLabel(
            master=err,
            text="Not all fields are filled!",
            font=("Roboto", 16),
            text_color="#f11",
        ).place(relx=0.5, rely=0.5, anchor="center")

    try:
        cursor.execute(
            f'insert into locations (uid, name, district, state, country) values ("{uid}", "{name}", "{district}", "{state}", "{country}")'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_locations(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_edit(window, db, cursor, uid, name, district, state, country, refresh_callback):
    if not (len(uid) or len(name) or len(district) or len(country) or len(state)):
        err = ctk.CTkToplevel(window)
        err.title("SwiftBus Admin - Error")
        err.geometry("200x100")
        ctk.CTkLabel(
            master=err,
            text="Not all fields are filled!",
            font=("Roboto", 16),
            text_color="#f11",
        ).place(relx=0.5, rely=0.5, anchor="center")

    try:
        cursor.execute(
            f'update locations set name="{name}", district="{district}", state="{state}", country="{country}", where uid="{uid}"'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_locations(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_delete(db, cursor, uid, refresh_callback):
    try:
        cursor.execute(f'delete from locations where uid="{uid}"')

        db.commit()
        refresh_callback(fetch_locations(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True
