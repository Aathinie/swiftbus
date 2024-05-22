import customtkinter as ctk
import mysql.connector
from utils import encrypt

# Table Schema:
#   uid varchar(36) not null primary key,
#   name varchar(255) not null,
#   brand varchar(255) not null unique,
#   description varchar(255) not null unique,
#   image varchar(255) not null unique,
#   perkm varchar(255) not null unique,
#   seats varchar(255) not null unique,


def fetch_bus(cursor):
    cursor.execute("select * from bus")
    return cursor.fetchall()


def fetch_bus_by_id(cursor, id):
    cursor.execute(f"select * from bus where uid='{id}'")
    return cursor.fetchone()


def handle_sql_create(
    window,
    db,
    cursor,
    uid,
    name,
    brand,
    description,
    image,
    perkm,
    seats,
    refresh_callback,
):
    if not (len(uid) or len(name) or len(brand) or len(description) or len(image)):
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
            f'insert into bus (uid, name, brand, description, image, perkm, seats) values ("{uid}", "{name}", "{brand}", "{description}", "{image}", "{perkm}", "{seats}")'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_bus(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_edit(
    window,
    db,
    cursor,
    uid,
    name,
    brand,
    description,
    image,
    perkm,
    seats,
    refresh_callback,
):
    if not (len(uid) or len(name) or len(brand) or len(description) or len(image)):
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
            f'update bus set name="{name}", brand="{brand}", description="{description}", image="{image}", perkm={perkm}, seats={seats} where uid="{uid}"'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_bus(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_delete(db, cursor, uid, refresh_callback):
    try:
        cursor.execute(f'delete from bus where uid="{uid}"')

        db.commit()
        refresh_callback(fetch_bus(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True
