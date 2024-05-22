import customtkinter as ctk
import mysql.connector
from utils import encrypt

# Table Schema:
#   uid varchar(36) not null primary key,
#   name varchar(255) not null,
#   logo varchar(255) not null unique,


def fetch_brands(cursor):
    cursor.execute("select * from brands")
    return cursor.fetchall()


def fetch_brand_by_id(cursor, id):
    cursor.execute(f"select * from brands where uid='{id}'")
    return cursor.fetchone()


def handle_sql_create(window, db, cursor, uid, name, logo, refresh_callback):
    if not (len(uid) or len(name) or len(logo)):
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
            f'insert into brands (uid, name, logo) values ("{uid}", "{name}", "{logo}")'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_brands(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_edit(window, db, cursor, uid, name, logo, refresh_callback):
    if not (len(uid) or len(name) or len(logo)):
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
            f'update brands set name="{name}", logo="{logo}" where uid="{uid}"'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_brands(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_delete(db, cursor, uid, refresh_callback):
    try:
        cursor.execute(f'delete from brands where uid="{uid}"')

        db.commit()
        refresh_callback(fetch_brands(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True

