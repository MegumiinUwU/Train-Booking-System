CREATE TABLE Admin (
    admin_id INT IDENTITY(1,1) PRIMARY KEY ,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    name VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE Passenger (
    passenger_id INT IDENTITY(1,1) PRIMARY KEY ,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    name VARCHAR(255),
    phone VARCHAR(20),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE Train (
    train_id INT IDENTITY(1,1) PRIMARY KEY ,
    train_model VARCHAR(255),
    capacity INT
);

CREATE TABLE Stations (
    station_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);


CREATE TABLE Seats (
    train_id INT,
    seat_number INT,
    seat_tier VARCHAR(20),
    is_valid BIT,
    trip_id INT,
    PRIMARY KEY (train_id, seat_number),
    FOREIGN KEY (train_id) REFERENCES Train(train_id) ON DELETE CASCADE,
);

CREATE TABLE Trip (
    trip_id INT IDENTITY(1,1) PRIMARY KEY ,
    departure_time DATETIME,
    arrival_time DATETIME,
    start_station_id INT,
    end_station_id INT,
    train_id INT,
    FOREIGN KEY (train_id) REFERENCES Train(train_id) ON DELETE CASCADE,
    FOREIGN KEY (start_station_id) REFERENCES Stations(station_id),
    FOREIGN KEY (end_station_id) REFERENCES Stations(station_id),
);


CREATE TABLE Ticket (
    ticket_id INT IDENTITY(1,1) PRIMARY KEY ,
    price NUMERIC(10,2),
    tier VARCHAR(20),
    is_valid BIT DEFAULT 1,
    start_station_id INT,
    end_station_id INT,
	trip_id INT,
    FOREIGN KEY (start_station_id) REFERENCES Stations(station_id),
    FOREIGN KEY (end_station_id) REFERENCES Stations(station_id),
    FOREIGN KEY (trip_id) REFERENCES Trip(trip_id) ON DELETE CASCADE
);

CREATE TABLE Manage (
    admin_id INT,
    trip_id INT,
    train_id INT,
    PRIMARY KEY (admin_id, trip_id),
    FOREIGN KEY (admin_id) REFERENCES Admin(admin_id),
    FOREIGN KEY (trip_id) REFERENCES Trip(trip_id) ON DELETE CASCADE,
);

CREATE TABLE Buy (
    passenger_id INT,
    ticket_id INT,
    train_id INT,
    seat_number INT,
    PRIMARY KEY (passenger_id, ticket_id),
    FOREIGN KEY (passenger_id) REFERENCES Passenger(passenger_id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id) ON DELETE CASCADE,
);