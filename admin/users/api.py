import customtkinter as ctk
import mysql.connector
from utils import encrypt

# Table Schema:
#   uid varchar(36) not null primary key,
#   name varchar(255) not null,
#   email varchar(255) not null unique,
#   password varchar(255) not null,

def fetch_users(cursor):
    cursor.execute("select * from users")
    return cursor.fetchall()


def fetch_user_by_id(cursor, id):
    cursor.execute(f"select * from users where uid='{id}'")
    return cursor.fetchone()


def handle_sql_create(window, db, cursor, uid, name, email, password, refresh_callback):
    if not (len(uid) or len(name) or len(email) or len(password)):
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
            f'insert into users (uid, name, email, password) values ("{uid}", "{name}", "{email}", "{encrypt(password)}")'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_users(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_edit(window, db, cursor, uid, name, email, password, refresh_callback):
    if not (len(uid) or len(name) or len(email) or len(password)):
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
            f'update users set name="{name}", email="{email}", password="{password}" where uid="{uid}"'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_users(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_delete(db, cursor, uid, refresh_callback):
    try:
        cursor.execute(f'delete from users where uid="{uid}"')

        db.commit()
        refresh_callback(fetch_users(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True

