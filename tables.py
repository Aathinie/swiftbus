TABLES = {}

TABLES[
    "users"
] = """
create table users (
  uid varchar(36) not null,
  name varchar(255) not null,
  email varchar(255) not null unique,
  password varchar(255) not null,
  primary key (uid)
)
"""

TABLES[
    "brands"
] = """
create table brands (
  uid varchar(36) not null unique,
  name varchar(255) not null unique,
  logo varchar (255) not null,
  primary key (uid)
)
"""

TABLES[
    "bus"
] = """
create table bus (
  uid varchar(36) not null unique,
  name varchar(255) not null,
  brand varchar(255) not null,
  description varchar(1028) not null,
  image varchar(255) not null,
  perkm float not null,
  seats int not null,
  primary key (uid)
)
"""

TABLES[
    "locations"
] = """
create table locations (
  uid varchar(36) not null unique,
  name varchar(255) not null,
  district varchar(255) not null,
  state varchar(255) not null,
  country varchar(255) not null,
  primary key (uid)
)
"""

TABLES[
    "routes"
] = """
create table routes (
  uid varchar(36) not null unique,
  source varchar(36) not null,
  destination varchar(36) not null,
  distance float not null,
  busID varchar(36) not null,
  days varchar(16) not null,
  timings varchar(255) not null,
  journeyTimeHrs varchar(16) not null,
  primary key (uid)
)
"""

TABLES[
    "bookings"
] = """
create table bookings (
  uid varchar(36) not null unique,
  userID varchar(36) not null,
  routeID varchar(36) not null,
  adults int not null,
  children int not null,
  journeyDate date not null,
  seats varchar(256),
  primary key (uid)
)
"""
