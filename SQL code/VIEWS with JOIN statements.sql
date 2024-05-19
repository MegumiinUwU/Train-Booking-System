CREATE VIEW PassengerTripSeatDetails AS
SELECT 
    p.name AS passenger_name,
    p.email AS passenger_email,
    s1.name AS from_station,
    s2.name AS to_station,
    t.departure_time,
    t.arrival_time,
    s.seat_number,
    s.seat_tier
FROM 
    Passenger p
INNER JOIN 
    Buy b ON p.passenger_id = b.passenger_id
INNER JOIN 
    Ticket tk ON b.ticket_id = tk.ticket_id
INNER JOIN 
    Trip t ON tk.trip_id = t.trip_id
INNER JOIN 
    Train tr ON t.train_id = tr.train_id
INNER JOIN 
    Seats s ON tr.train_id = s.train_id
           AND s.seat_number = b.seat_number
INNER JOIN 
    Stations s1 ON tk.start_station_id = s1.station_id
INNER JOIN 
    Stations s2 ON tk.end_station_id = s2.station_id;
GO




CREATE VIEW PassengerTicketsByEmail AS
SELECT
                            tk.ticket_id,
                            p.name AS passenger_name,
                            p.email AS passenger_email,
                            s1.name AS from_station,
                            s2.name AS to_station,
                            t.departure_time,
                            t.arrival_time,
                            s.seat_number,
                            s.seat_tier
                        FROM 
                            Passenger p
                        INNER JOIN 
                            Buy b ON p.passenger_id = b.passenger_id
                        INNER JOIN 
                            Ticket tk ON b.ticket_id = tk.ticket_id
                        INNER JOIN 
                            Trip t ON tk.trip_id = t.trip_id
                        INNER JOIN 
                            Train tr ON t.train_id = tr.train_id
                        INNER JOIN 
                            Seats s ON tr.train_id = s.train_id
                                AND s.seat_number = b.seat_number
                        INNER JOIN 
                            Stations s1 ON tk.start_station_id = s1.station_id
                        INNER JOIN 
                            Stations s2 ON tk.end_station_id = s2.station_id
GO