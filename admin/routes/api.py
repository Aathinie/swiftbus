import customtkinter as ctk
import mysql.connector
from utils import encrypt

# Table Schema:
#   uid varchar(36) not null primary key,
#   source varchar(255) not null,
#   destination varchar(255) not null unique,
#   busID varchar(255) not null unique,
#   days varchar(255) not null unique,
#   timings varchar(255) not null unique,
#   jounreyTimeHrs varchar(255) not null unique,


def fetch_routes(cursor):
    cursor.execute("select * from routes")
    return cursor.fetchall()


def fetch_route_by_id(cursor, id):
    cursor.execute(f"select * from routes where uid='{id}'")
    return cursor.fetchone()


def handle_sql_create(
    window,
    db,
    cursor,
    uid,
    source,
    destination,
    distance,
    busID,
    days,
    timings,
    journeyTimeHrs,
    refresh_callback,
):
    if not (len(uid) or len(source) or len(destination) or len(days)):
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
            f'insert into routes (uid, source, destination, distance, busID, days, timings, journeyTimeHrs) values ("{uid}", "{source}", "{destination}", {distance}, "{busID}", "{days}", "{timings}","{journeyTimeHrs}")'
        )

        db.commit()

        window.destroy()
        refresh_callback(fetch_routes(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_edit(
    window,
    db,
    cursor,
    uid,
    source,
    destination,
    distance,
    busID,
    days,
    timings,
    journeyTimeHrs,
    refresh_callback,
):
    if not (len(uid) or len(source) or len(destination) or len(days)):
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
            f'update routes set source="{source}", destination="{destination}", distance={distance}, busID="{busID}", days ="{days}", timings="{timings}", journeyTimeHrs="{journeyTimeHrs}" where uid="{uid}"'
        )
        db.commit()

        window.destroy()
        refresh_callback(fetch_routes(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True


def handle_sql_delete(db, cursor, uid, refresh_callback):
    try:
        cursor.execute(f'delete from brands where uid="{uid}"')

        db.commit()
        refresh_callback(fetch_routes(cursor))

    except mysql.connector.Error as err:
        return print(err)

    return True
