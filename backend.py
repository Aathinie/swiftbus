import os
import mysql.connector
from mysql.connector import errorcode
from uuid import uuid4
import hashlib
from utils import encrypt
from utils import correct_path

from tables import TABLES

MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "aathinie<3"
MYSQL_DBNAME = "swiftbus"
FILE_STORE_LOCATION = f"./uploads"

connection = mysql.connector.connect(
    user=MYSQL_USERNAME,
    password=MYSQL_PASSWORD,
    host="127.0.0.1",
)

cursor = connection.cursor(buffered=True)

## Create and use database
cursor.execute(f"create database if not exists {MYSQL_DBNAME}")
cursor.execute(f"use {MYSQL_DBNAME}")

## Create tables
for table_name, table_desc in TABLES.items():
    try:
        cursor.execute(table_desc)
    except mysql.connector.Error as err:
        continue

#############################
#############################


def store_image(file_path):
    file_ext = file_path.split(os.sep)[-1].split(".")[-1]
    new_file_name = f"{uuid4()}.{file_ext}"
    new_file_loc = FILE_STORE_LOCATION + new_file_name

    with open(file_path, "rb") as src:
        with open(correct_path(new_file_loc), "wb") as dest:
            dest.writelines(src.readlines())

    return new_file_loc


#############################
#############################


def get_user(email):
    cursor.execute(f"select * from users where email='{email}'")
    return cursor.fetchone()


def signup_user(name, email, password):
    if get_user(email):
        return None

    cursor.execute(
        f"insert into users (uid, name, email, password) values ('{uuid4()}', '{name}', '{email}', '{encrypt(password)}')"
    )
    connection.commit()

    return True


def login_user(email, password, hashed=False):
    cursor.execute(f"select password from users where email='{email}'")
    real_pwd = cursor.fetchone()

    if real_pwd is None:
        return "USER_NIL"

    if (encrypt(password) if not hashed else password) != real_pwd[0]:
        return "WRONG_PWD"

    return 1


def change_password(email, password):
    cursor.execute(f"select * from users where email='{email}'")
    user = cursor.fetchone()

    if user == None:
        return "USER_NIL"

    cursor.execute(
        f"update users set password='{encrypt(password)}' where email='{email}'"
    )

    connection.commit()

    return 1
