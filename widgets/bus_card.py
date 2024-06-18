from widgets.image import load_image_ctk
import customtkinter as ctk
from admin.bus.api import fetch_bus_by_id


def BusCard(cursor, master, routeid, source, destination, dist, timing, bus, window):
    uid, bus_name, bus_brand, bus_desc, bus_image, bus_perkm, seats = fetch_bus_by_id(
        cursor, bus
    )

    #####

    detail_frame = ctk.CTkFrame(
        master=master,
        width=920,
        height=170,
        fg_color="#EDEDED",
        corner_radius=7,
        border_width=3,
        border_color="#3B8ED0",
    )

    detail_frame.grid_propagate(0)

    #####

    place = ctk.CTkFrame(master=detail_frame, width=920, fg_color="#EDEDED")
    src = ctk.CTkLabel(master=place, text=source.strip(), font=("Roboto", 20))
    graphic = ctk.CTkLabel(
        master=place, text="", image=load_image_ctk("./assets/distance.png", (341, 0))
    )
    dest = ctk.CTkLabel(master=place, text=destination.strip(), font=("Roboto", 20))

    src.grid(row=1, column=1)
    graphic.grid(row=1, column=2, padx=10)
    dest.grid(row=1, column=3)

    place.grid(
        row=1,
        column=1,
        
        pady=20,
    )

    #####

    info_frame = ctk.CTkFrame(master=detail_frame, fg_color="#EDEDED")

    ##
    departure_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")

    departure_time_title = ctk.CTkLabel(
        master=departure_frame, text="Departure Time", font=("Roboto", 14)
    )
    departure_time = ctk.CTkLabel(
        master=departure_frame, text=timing, font=("Roboto", 25)
    )

    departure_time_title.grid(row=1, column=1, sticky="w")
    departure_time.grid(row=2, column=1, sticky="w")

    departure_frame.grid(row=1, column=1, padx=20)
    ##

    ##
    distance_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")

    distance_title = ctk.CTkLabel(
        master=distance_frame, text="Distance", font=("Roboto", 14)
    )
    distance = ctk.CTkLabel(
        master=distance_frame, text=f"{int(dist)} km", font=("Roboto", 25)
    )

    distance_title.grid(row=1, column=1, sticky="w")
    distance.grid(row=2, column=1, sticky="w")

    distance_frame.grid(row=1, column=2, padx=20)
    ##

    ##
    price_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")

    price_title = ctk.CTkLabel(master=price_frame, text="Price", font=("Roboto", 14))
    price = ctk.CTkLabel(
        master=price_frame, text=f"₹ {int(dist) * bus_perkm}", font=("Roboto", 25)
    )

    price_title.grid(row=1, column=1, sticky="w")
    price.grid(row=2, column=1, sticky="w")

    price_frame.grid(row=1, column=3, padx=20)
    ##

    ##
    vehicle_frame = ctk.CTkFrame(master=info_frame, fg_color="#EDEDED")

    vehicle_title = ctk.CTkLabel(
        master=vehicle_frame, text="Vehicle", font=("Roboto", 14)
    )
    vehicle = ctk.CTkLabel(
        master=vehicle_frame, text=f"{bus_name}", font=("Roboto", 25)
    )

    vehicle_title.grid(row=1, column=1, sticky="w")
    vehicle.grid(row=2, column=1, sticky="w")

    vehicle_frame.grid(row=1, column=4, padx=20)
    ##

    info_frame.grid(row=2, column=1, padx=10)

    def onclick(_):
        window.routeid = routeid
        window.busid = uid
        window.busname = bus_name
        window.depttime = timing
        window.navigator.navigate_to("seat_select")

    detail_frame.bind("<Button-1>", onclick)

    return detail_frame
