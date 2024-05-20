# import pypyodbc as odbc
import hashlib
import re
import datetime
import pyodbc as odbc
import numpy as np
import matplotlib.pyplot as plt

server = 'YOUSSEF'
database = 'Train Booking'
username = ''
password = ''
driver = 'ODBC Driver 17 for SQL Server'  # Assuming you're using Microsoft SQL Server

connection_string = f"""
DRIVER={{{driver}}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
"""

def seat_number_valid(train_id, seat_number):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if seat_number is valid for the given train_id
        cursor.execute("SELECT * FROM Seats WHERE train_id = ? AND seat_number = ?", (train_id, seat_number))
        valid = cursor.fetchone() is not None

        return valid

    except Exception as e:
        print(f"Error checking seat number validity: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()



def admin_exists(admin_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if admin_id exists in the Admin table
        cursor.execute("SELECT * FROM Admin WHERE admin_id = ?", (admin_id,))
        exists = cursor.fetchoFne() is not None

        return exists

    except Exception as e:
        print(f"Error checking admin existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def add_station(name , location):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()
        
        if station_exist(name , location):
            print("Station already exists!")
            return

        # Insert query
        insert_query = "INSERT INTO Stations (name , location) VALUES (? , ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (name,location))

        # Commit the transaction
        conn.commit()

        print("Station added successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error adding station: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def station_exist(name,location):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if station_id exists in the Stations table
        cursor.execute("SELECT * FROM Stations WHERE name = ? AND location=?", (name,location))
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking station existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def station_exists(station_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if station_id exists in the Stations table
        cursor.execute("SELECT * FROM Stations WHERE station_id = ?", (station_id,))
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking station existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def trip_exists(trip_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if trip_id exists in the Trip table
        cursor.execute("SELECT * FROM Trip WHERE trip_id = ?", (trip_id,))
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking trip existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def ticket_exists(ticket_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if ticket_id exists in the Ticket table
        cursor.execute("SELECT * FROM Ticket WHERE ticket_id = ?", (ticket_id,))
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking ticket existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def passenger_exists(passenger_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if passenger_id exists in the Passenger table
        cursor.execute("SELECT * FROM Passenger WHERE passenger_id = ?", (passenger_id,))
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking passenger existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def train_exists(train_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if train_id exists in the Train table
        cursor.execute("SELECT * FROM Train WHERE train_id = ?", (train_id,))
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking train existence: {str(e)}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def add_seat(cursor, train_id, seat_number, seat_tier , trip_id):
    try:
        if seat_number_valid(train_id, seat_number):
            cursor.execute("SELECT MAX(seat_number) FROM Seats WHERE train_id = ?", (train_id,))
            max_seat_number = cursor.fetchone()[0]
            seat_number = max_seat_number + 1

        # Insert query
        insert_query = "INSERT INTO Seats (train_id, seat_number, seat_tier , is_valid , trip_id ) VALUES (?, ? , ? , ? , ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (train_id, seat_number , seat_tier , 1 , trip_id))

        # No need to commit here as we're not managing the connection

    except Exception as e:
        # No need to rollback here as we're not managing the connection
        return(f"Error adding seat: {str(e)}")


def add_train(train_model, capacity):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Insert query
        insert_query = "INSERT INTO Train (train_model, capacity) VALUES (?, ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (train_model, capacity))
        
        # Commit the transaction
        conn.commit()

        return("Train inserted successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error inserting train: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()



def update_train(train_id, new_model=None, new_capacity=None):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Update query
        update_query = "UPDATE Train SET "
        update_params = []

        if new_model is not None:
            update_query += "train_model = ?, "
            update_params.append(new_model)
        if new_capacity is not None:
            update_query += "capacity = ?, "
            update_params.append(new_capacity)

        # Remove the trailing comma and space
        update_query = update_query.rstrip(', ')

        # Append WHERE clause
        update_query += " WHERE train_id = ?"
        update_params.append(train_id)

        # Execute the query with parameters
        cursor.execute(update_query, update_params)

        # Commit the transaction
        conn.commit()

        return("Train details updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error updating train details: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def get_all_trains():
    trains = []
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Select query to retrieve all trains
        select_query = "SELECT * FROM Train"

        # Execute the query
        cursor.execute(select_query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Loop through the rows and store data in a list of dictionaries
        for row in rows:
            train_id, train_model, capacity = row
            trains.append({'train_id': train_id, 'train_model': train_model, 'capacity': capacity})

    except Exception as e:
        print(f"Error retrieving trains: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

    return trains

def get_all_stations():
    stations = []
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Select query to retrieve all stations
        select_query = "SELECT * FROM Stations"

        # Execute the query
        cursor.execute(select_query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Loop through the rows and store data in a list of dictionaries
        for row in rows:
            station_id, name, location = row
            stations.append({'station_id': station_id, 'name': name, 'location': location})

    except Exception as e:
        print(f"Error retrieving stations: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

    return stations

def remove_train(train_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Delete query
        delete_query = "DELETE FROM Train WHERE train_id = ?"

        # Execute the query with parameters
        cursor.execute(delete_query, (train_id,))

        # Commit the transaction
        conn.commit()

        return("Train removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error removing train: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def station_id_by_name(station_name):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Select query to retrieve station_id by name
        select_query = "SELECT station_id FROM Stations WHERE name = ?"

        # Execute the query with parameters
        cursor.execute(select_query, (station_name,))

        # Fetch the station_id
        station_id = cursor.fetchone()

        return station_id[0] if station_id else None

    except Exception as e:
        print(f"Error retrieving station ID: {str(e)}")
        return None

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def add_tickets(quantity, price, tier, start_station_id, end_station_id, trip_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        

        if trip_exists(trip_id):
            cursor.execute("SELECT train_id FROM Trip WHERE trip_id = ?", (trip_id,))
            train_id = cursor.fetchone()

            if train_id:
                train_id = train_id[0] 
            # Check if start_station_id and end_station_id exist in the Stations table
            if station_exists(start_station_id) and station_exists(end_station_id):
                # Insert query
                insert_query = "INSERT INTO Ticket (price, tier, start_station_id, end_station_id, trip_id) VALUES (?, ?, ?, ?, ?)"

                
                # # Add tickets individually
                for i in range(int(quantity)):
                    # Execute the query with parameters
                    cursor.execute(insert_query, (price, tier, start_station_id, end_station_id, trip_id))
                    add_seat(cursor, train_id, i, tier , trip_id)

                    
                # Commit the transaction
                conn.commit()

                return(f"{quantity} tickets added successfully!")
            else:
                return("Start or end station ID does not exist. Please provide valid station IDs.")
        else:
            return("Trip ID does not exist. Please provide a valid trip ID.")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error adding tickets: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()



def remove_ticket(trip_id , teir):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Delete query
        delete_query = "DELETE FROM Ticket WHERE trip_id = ? AND tier = ?"

        # Execute the query with parameters
        cursor.execute(delete_query, (trip_id,teir))

        # Commit the transaction
        conn.commit()

        return("Ticket removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error removing ticket: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def update_ticket(trip_id, new_price=None, new_tier=None, new_start_station_id=None, new_end_station_id=None):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Update query
        update_query = "UPDATE Ticket SET "
        update_params = []

        if new_price is not None:
            update_query += "price = ?, "
            update_params.append(new_price)
        if new_tier is not None:
            update_query += "tier = ?, "
            update_params.append(new_tier)
        if new_start_station_id is not None:
            if station_exists(new_start_station_id):
                update_query += "start_station_id = ?, "
                update_params.append(new_start_station_id)
            else:
                print("Start station ID does not exist. Please provide a valid station ID.")
                return
        if new_end_station_id is not None:
            if station_exists(new_end_station_id):
                update_query += "end_station_id = ?, "
                update_params.append(new_end_station_id)
            else:
                print("End station ID does not exist. Please provide a valid station ID.")
                return

        # Remove the trailing comma and space
        update_query = update_query.rstrip(', ')

        # Append WHERE clause
        update_query += " WHERE trip_id = ?"
        update_params.append(trip_id)

        # Debug print statements
        

        # Execute the query with parameters
        cursor.execute(update_query, update_params)

        # Commit the transaction
        conn.commit()

        
        return "Ticket details updated successfully!"

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error updating ticket details: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def get_all_tickets():
    tickets = {}
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Select query to retrieve all tickets
        select_query = "SELECT * FROM Ticket"

        # Execute the query
        cursor.execute(select_query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Loop through the rows and store data in a dictionary
        for row in rows:
            ticket_id, price, tier, start_station_id, end_station_id, trip_id = row
            tickets[ticket_id] = {
                'price': price,
                'tier': tier,
                'start_station_id': start_station_id,
                'end_station_id': end_station_id,
                'trip_id': trip_id
            }

    except Exception as e:
        print(f"Error retrieving tickets: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

    return tickets



def trip_overlap_exists(departure_time, arrival_time, train_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Query to check for overlapping trips
        query = """
            SELECT * 
            FROM Trip 
            WHERE train_id = ? 
            AND (
                (departure_time BETWEEN ? AND ?) OR 
                (arrival_time BETWEEN ? AND ?) OR 
                (? BETWEEN departure_time AND arrival_time)
            )
            """

        # Execute the query with parameters
        cursor.execute(query, (train_id, departure_time, arrival_time, departure_time, arrival_time, departure_time))

        # Fetch any overlapping trips
        overlapping_trips = cursor.fetchall()

        # If there are overlapping trips, return True
        if overlapping_trips:
            return True
        else:
            return False

    except Exception as e:
        print(f"Error checking for trip overlap: {str(e)}")
        return True  # Assume there's an overlap to prevent adding the trip

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def add_trip(departure_time_str, arrival_time_str, train_id, start_station_id, end_station_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Convert string inputs to datetime objects
        departure_time = datetime.datetime.strptime(departure_time_str, "%m/%d/%y %I:%M:%S %p")
        arrival_time = datetime.datetime.strptime(arrival_time_str, "%m/%d/%y %I:%M:%S %p")

        if departure_time >= arrival_time:
            return("Departure time should be before arrival time.")
        if start_station_id == end_station_id:
            return("Start and end stations cannot be the same.")

        # Validate train_id
        if not train_exists(train_id):
            return("Train ID does not exist. Please provide a valid train ID.")
            

        # Validate start_station_id and end_station_id
        if not station_exists(start_station_id) or not station_exists(end_station_id):
            return("One or both station IDs do not exist. Please provide valid station IDs.")
            

        # Check if there are overlapping trips
        if trip_overlap_exists(departure_time, arrival_time, train_id):
            return("Another trip already exists for the same train within the specified period.")
            

        # Insert query
        insert_query = "INSERT INTO Trip (departure_time, arrival_time, train_id, start_station_id, end_station_id) VALUES (?, ?, ?, ?, ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (departure_time, arrival_time, train_id, start_station_id, end_station_id))

        # Commit the transaction
        conn.commit()

        return("Trip added successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error adding trip: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def update_trip(trip_id, new_departure_time=None, new_arrival_time=None, new_train_id=None, new_start_station_id=None, new_end_station_id=None):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Update query
        update_query = "UPDATE Trip SET "
        update_params = []

        if new_departure_time is not None:
            new_departure_time = datetime.datetime.strptime(new_departure_time, "%m/%d/%y %I:%M:%S %p")
            update_query += "departure_time = ?, "
            update_params.append(new_departure_time)
        if new_arrival_time is not None:
            new_arrival_time = datetime.datetime.strptime(new_arrival_time, "%m/%d/%y %I:%M:%S %p")
            update_query += "arrival_time = ?, "
            update_params.append(new_arrival_time)
        if new_train_id is not None:
            if not train_exists(new_train_id):
                return("New train ID does not exist. Please provide a valid train ID.")
                
            else:
                update_query += "train_id = ?, "
                update_params.append(new_train_id)
        if new_start_station_id is not None:
            if not station_exists(new_start_station_id):
                return("New start station ID does not exist. Please provide a valid station ID.")
                
            else:
                update_query += "start_station_id = ?, "
                update_params.append(new_start_station_id)
        if new_end_station_id is not None:
            if not station_exists(new_end_station_id):
                return("New end station ID does not exist. Please provide a valid station ID.")
                
            else:
                update_query += "end_station_id = ?, "
                update_params.append(new_end_station_id)

        # Remove the trailing comma and space
        update_query = update_query.rstrip(', ')

        # Append WHERE clause
        update_query += " WHERE trip_id = ?"
        update_params.append(trip_id)

        # Execute the query with parameters
        cursor.execute(update_query, update_params)

        # Commit the transaction
        conn.commit()

        return("Trip details updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error updating trip details: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()
def remove_trip(trip_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Delete query
        delete_query = "DELETE FROM Trip WHERE trip_id = ?"

        # Execute the query with parameters
        cursor.execute(delete_query, (trip_id,))

        # Commit the transaction
        conn.commit()

        return("Trip removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        return(f"Error removing trip: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def get_all_trips():
    trip_details = []
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Select query to retrieve all trips
        select_query = """SELECT DISTINCT
    t.trip_id,
    t.start_station_id,
    t.end_station_id,
    t.departure_time,
    t.arrival_time,
    t.train_id,
    tk.tier AS seat_tier  -- Ensure the correct column name from the Ticket table
FROM 
    Trip t
FULL JOIN 
    Ticket tk ON t.trip_id = tk.trip_id;

            """


        # Execute the query
        cursor.execute(select_query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Loop through the rows and store data in a list of dictionaries
        for row in rows:
            trip_id = row[0] if len(row) > 0 else None
            start_station = row[1] if len(row) > 1 else None
            end_station = row[2] if len(row) > 2 else None
            departure_time = row[3] if len(row) > 3 else None
            arrival_time = row[4] if len(row) > 4 else None
            train_id = row[5] if len(row) > 5 else None
            tier = row[6] if len(row) > 6 else None

            trip_details.append(dict({
                'trip_id': trip_id,
                'start_station': start_station,
                'end_station': end_station,
                'departure_time': departure_time,
                'arrival_time': arrival_time,
                'train_id': train_id,
                'tier': tier,
            }))
           



    except Exception as e:
        print(f"Error retrieving trips: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

    return trip_details



def update_purchase(passenger_id, ticket_id, train_id, seat_number, new_seat_number):
    try:
         # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if passenger_id, ticket_id, train_id, and seat_number exist
        if not passenger_exists(passenger_id):
            print("Passenger ID does not exist. Please provide a valid passenger ID.")
            return
        if not ticket_exists(ticket_id):
            print("Ticket ID does not exist. Please provide a valid ticket ID.")
            return
        if not train_exists(train_id):
            print("Train ID does not exist. Please provide a valid train ID.")
            return
        if not seat_number_valid(train_id, seat_number):
            print("Current seat number is not valid for the given train ID.")
            return
        if not seat_number_valid(train_id, new_seat_number):
            print("New seat number is not valid for the given train ID.")
            return


        # Remove the new seat from the Seats table
        # Update query
        update_query = "UPDATE Seats SET is_valid = 1 WHERE train_id = ? AND seat_number = ?"

        # Execute the query with parameters
        cursor.execute(update_query, (train_id, seat_number))

        # Update query for Buy table
        update_query = "UPDATE Buy SET seat_number = ? WHERE passenger_id = ? AND ticket_id = ? AND train_id = ? AND seat_number = ?"

        # Update query
        update_seat_query = "UPDATE Seats SET is_valid = 0 WHERE train_id = ? AND seat_number = ?"

        # Execute the query with parameters
        cursor.execute(update_seat_query, (train_id, new_seat_number))
        # Execute the query with parameters
        cursor.execute(update_query, (new_seat_number, passenger_id, ticket_id, train_id, seat_number))

        # Commit the transaction
        conn.commit()

        print("Purchase entry updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error updating purchase entry: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def add_manage_entry(admin_id, trip_id, train_id):
    try:
        
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if admin_id, trip_id, and train_id exist
        if not admin_exists(admin_id):
            print("Admin ID does not exist. Please provide a valid admin ID.")
            return
        if not trip_exists(trip_id):
            print("Trip ID does not exist. Please provide a valid trip ID.")
            return
        if not train_exists(train_id):
            print("Train ID does not exist. Please provide a valid train ID.")
            return

        # Insert query
        insert_query = "INSERT INTO Manage (admin_id, trip_id, train_id) VALUES (?, ?, ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (admin_id, trip_id, train_id))

        # Commit the transaction
        conn.commit()

        print("Manage entry added successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error adding manage entry: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()



def update_manage_entry(admin_id, trip_id, train_id, new_train_id):
    try:
        
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if admin_id, trip_id, and train_id exist
        if not admin_exists(admin_id):
            print("Admin ID does not exist. Please provide a valid admin ID.")
            return
        if not trip_exists(trip_id):
            print("Trip ID does not exist. Please provide a valid trip ID.")
            return
        if not train_exists(train_id):
            print("Current train ID does not exist. Please provide a valid train ID.")
            return
        if not train_exists(new_train_id):
            print("New train ID does not exist. Please provide a valid train ID.")
            return


        # Update query
        update_query = "UPDATE Manage SET train_id = ? WHERE admin_id = ? AND trip_id = ? AND train_id = ?"

        # Execute the query with parameters
        cursor.execute(update_query, (new_train_id, admin_id, trip_id, train_id))

        # Commit the transaction
        conn.commit()

        print("Manage entry updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error updating manage entry: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def remove_manage_entry(admin_id, trip_id, train_id):
    try:
        
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if admin_id, trip_id, and train_id exist
        if not admin_exists(admin_id):
            print("Admin ID does not exist. Please provide a valid admin ID.")
            return
        if not trip_exists(trip_id):
            print("Trip ID does not exist. Please provide a valid trip ID.")
            return
        if not train_exists(train_id):
            print("Train ID does not exist. Please provide a valid train ID.")
            return



        # Delete query
        delete_query = "DELETE FROM Manage WHERE admin_id = ? AND trip_id = ? AND train_id = ?"

        # Execute the query with parameters
        cursor.execute(delete_query, (admin_id, trip_id, train_id))

        # Commit the transaction
        conn.commit()

        print("Manage entry removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error removing manage entry: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()
######################################################

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def validate_email(email):
    # Define the regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)  # Check if the provided email matches the pattern

def login(user_type, email, password):
    if not validate_email(email):
            return("Invalid email format!")
            
            
    
    conn = odbc.connect(connection_string)

        # Create a cursor object
    cursor = conn.cursor()


    user_type = user_type.lower()

    if user_type == "admin":
        sql_select = """
            SELECT * FROM Admin;
            """
    
    elif user_type == "passenger":
        sql_select = """
            SELECT * FROM Passenger;
            """
    # Execute the SELECT statement
    cursor.execute(sql_select)

    # Fetch all the results
    results = cursor.fetchall()

    for row in results:
        # Extract email and password from the row
        row_email = row[1]  # Assuming email is at index 1
        hashed_password = row[2]  # Assuming hashed password is at index 2
        
        if email == row_email:
            provided_hashed_password = hash_password(password)
            
            if hashed_password == provided_hashed_password:
                return("Login successful!")

            else:
                return("Incorrect password!")
                 
    else:
        return("Email not found!")

def signup(user_type, email, password, confirm_password , name, phone, age=None, gender=None):

    if not validate_email(email):
            return("Invalid email format!")
            
    # Establish connection
    conn = odbc.connect(connection_string)

        # Create a cursor object
    cursor = conn.cursor()

    user_type = user_type.lower()

    if user_type == "admin":
        sql_select = """
            SELECT * FROM Admin;
            """
    
    elif user_type == "passenger":
        sql_select = """
            SELECT * FROM Passenger;
            """
    # Execute the SELECT statement
    cursor.execute(sql_select)

    # Fetch all the results
    results = cursor.fetchall()

    for row in results:
        # Extract email and password from the row
        row_email = row[1]  # Assuming email is at index 1
        
        if email == row_email:
            return("Email already exists!")
            
    else:
        if password != confirm_password:
            return("Passwords do not match!")
            

        if user_type == "admin":
            sql_insert = """
            INSERT INTO Admin (email, password, name, phone)
            VALUES (?, ?, ?, ?);
            """
            values_to_insert = (email, hash_password(password), name, phone)
        elif user_type == "passenger":
            sql_insert = """
            INSERT INTO Passenger (email, password, name, phone, age, gender)
            VALUES (?, ?, ?, ?, ?, ?);
            """
            values_to_insert = (email, hash_password(password), name, phone, age, gender)
        
        cursor.execute(sql_insert, values_to_insert)
        conn.commit()
        return("Signup successful!")


def edit_user_details(user_type, email , new_email, password ,confirm_password, new_name=None, new_phone=None, new_age=None, new_gender=None):
    if not validate_email(email):
        return("Invalid email format!")
        
    if password != confirm_password:
        return("Passwords do not match!")
    
     # Establish connection
    conn = odbc.connect(connection_string)

        # Create a cursor object
    cursor = conn.cursor()

    if cursor is None:
        return("Cursor not provided!")
        

    user_type = user_type.lower()

    if user_type == "admin":
        table_name = "Admin"
    
    elif user_type == "passenger":
        table_name = "Passenger"
    
    else:
        return(f"User type '{user_type}' is not valid!")
        
    
    # Execute the SELECT statement to check if the email and password match
    sql_select = f"""
        SELECT * FROM {table_name} WHERE email = ?;
        """
    
    cursor.execute(sql_select, (email))

    # Fetch the result
    result = cursor.fetchone()


    if result:
        # Update the user's details with the new information, if provided
        update_values = {}
        if new_email:
            if not validate_email(new_email):
                return("Invalid email format!")
                
            elif email != new_email:
                # Check if the new email already exists
                sql_check_email = f"""
                    SELECT * FROM {table_name} WHERE email = ?;
                    """
                cursor.execute(sql_check_email, (new_email,))
                if cursor.fetchone():
                    return("Email already exists!")
                    
                else:
                    update_values['email'] = new_email
        
        if password:
            update_values['password'] = hash_password(password)
        
        if new_name:
            update_values['name'] = new_name
        
        if new_phone:
            update_values['phone'] = new_phone
        
        if new_age:
            update_values['age'] = new_age
        
        if new_gender:
            update_values['gender'] = new_gender

        if update_values:
            # Generate the UPDATE statement
            sql_update = f"""
                UPDATE {table_name} SET {', '.join([f"{key} = ?" for key in update_values.keys()])} WHERE email = ?;
                """
            cursor.execute(sql_update, tuple(update_values.values()) + (email,))
            conn.commit()
            return("User details updated successfully!")
        
    else:
        return("Email is not found!")


def remove_user(user_type, email, password, confirm_password):
    if not validate_email(email):
        print("Invalid email format!")
        return

    if password != confirm_password:
        print("Passwords do not match!")
        return
    
    conn = odbc.connect(connection_string)

    # Create a cursor object
    cursor = conn.cursor()

    if cursor is None:
        print("Cursor not provided!")
        return

    user_type = user_type.lower()

    if user_type == "admin":
        table_name = "Admin"
    
    elif user_type == "passenger":
        table_name = "Passenger"
    
    else:
        print(f"User type '{user_type}' is not valid!")
        return

    # Execute the SELECT statement to check if the email and password match
    sql_select = f"""
        SELECT * FROM {table_name} WHERE email = ? AND password = ?;
        """
    
    cursor.execute(sql_select, (email, hash_password(password)))

    # Fetch the result
    result = cursor.fetchone()

    if result:
        # Execute the DELETE statement to remove the user
        sql_delete = f"""
            DELETE FROM {table_name} WHERE email = ?;
            """
        cursor.execute(sql_delete, (email,))
        conn.commit()
        print("User removed successfully!")
    else:
        print("Email and password do not match!")

def get_all_users_tickets(email):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        select_query = """SELECT * FROM PassengerTicketsByEmail
        
        WHERE passenger_email = ?;"""

        # Execute the query
        cursor.execute(select_query , (email,))

        # Fetch all rows 
        rows = cursor.fetchall()

    
        trip_details = []

        for row in rows:
            ticket_id , passenger_name, passenger_email, from_station, to_station, departure_time, arrival_time, seat_number, seat_tier = row

            trip_detail = {
                'ticket_id': ticket_id,
                'passenger_name': passenger_name,
                'passenger_email': passenger_email,
                'from_station': from_station,
                'to_station': to_station,
                'departure_time': departure_time,
                'arrival_time': arrival_time,
                'seat_number': seat_number,
                'seat_tier': seat_tier
            }

            trip_details.append(trip_detail)  # Append trip_detail to trip_details
        #print (trip_details)

    except Exception as e:
        print(f"Error retrieving tickets: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

    return trip_details




def get_ticket_and_passenger_info(ticket_id, passenger_email):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Get passenger ID from email
        cursor.execute("SELECT passenger_id FROM Passenger WHERE email = ?", (passenger_email,))
        passenger_id = cursor.fetchone()[0]

        # Get train ID and seat number from ticket ID
        cursor.execute("SELECT train_id, seat_number FROM Buy WHERE ticket_id = ?", (ticket_id,))
        result = cursor.fetchone()
        if result:
            train_id, seat_number = result
        else:
            raise ValueError("Ticket ID not found in Buy table.")

        return passenger_id, train_id, seat_number

    except Exception as e:
        print(f"Error retrieving ticket and passenger info: {str(e)}")
        return None, None, None

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def remove_purchase2(ticket_id, passenger_email):
    passenger_id, train_id, seat_number = get_ticket_and_passenger_info(ticket_id, passenger_email)
    if passenger_id is None or train_id is None or seat_number is None:
        return
    
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Check if passenger_id, ticket_id, train_id, and seat_number exist
        if not passenger_exists(passenger_id):
            print("Passenger ID does not exist. Please provide a valid passenger ID.")
            return
        if not ticket_exists(ticket_id):
            print("Ticket ID does not exist. Please provide a valid ticket ID.")
            return
        if not train_exists(train_id):
            print("Train ID does not exist. Please provide a valid train ID.")
            return
        if not seat_number_valid(train_id, seat_number):
            print("Seat number is not valid for the given train ID.")
            return

        # Update query
        update_query = "UPDATE Seats SET is_valid = 1 WHERE train_id = ? AND seat_number = ?"

        # Execute the query with parameters
        cursor.execute(update_query, (train_id, seat_number))
        
        # Delete query
        delete_query = "DELETE FROM Buy WHERE passenger_id = ? AND ticket_id = ? AND train_id = ? AND seat_number = ?"

        # Execute the query with parameters
        cursor.execute(delete_query, (passenger_id, ticket_id, train_id, seat_number))

        # Commit the transaction
        conn.commit()

        print("Purchase entry removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error removing purchase entry: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

def get_purchase_data(trip_id, passenger_email, seat_number):
    cursor = None
    conn = None
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Get passenger_id from passenger_email
        select_passenger_query = "SELECT passenger_id FROM Passenger WHERE email = ?"
        cursor.execute(select_passenger_query, (passenger_email,))
        passenger_id = cursor.fetchone()

        if not passenger_id:
            print("Passenger email does not exist. Please provide a valid email.")
            return None

        # Get ticket_id and train_id from trip_id
        select_trip_query = """SELECT tk.ticket_id, t.train_id 
                               FROM Ticket tk 
                               INNER JOIN Trip t ON tk.trip_id = t.trip_id 
                               WHERE tk.trip_id = ? AND tk.is_valid = 1"""
        cursor.execute(select_trip_query, (trip_id,))
        trip_data = cursor.fetchone()

        if not trip_data:
            print("Trip ID does not exist or data is incomplete.")
            return None

        # Unpack trip_data
        ticket_id, train_id = trip_data

        # Check if the seat is available
        select_seat_query = "SELECT 1 FROM Buy WHERE train_id = ? AND seat_number = ?"
        cursor.execute(select_seat_query, (train_id, seat_number))
        seat_taken = cursor.fetchone()

        if seat_taken:
            return("Seat is already taken.")
            

        return passenger_id[0], ticket_id, train_id, seat_number

    except Exception as e:
        print(f"Error retrieving purchase data: {str(e)}")
        

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def add_purchase2(trip_id, passenger_email, seat_number):
    conn = None
    cursor = None
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Get purchase data using trip_id, passenger_email, and seat_number
        purchase_data = get_purchase_data(trip_id, passenger_email, seat_number)

        if not purchase_data:
            return "Error: Unable to retrieve purchase data."

        # Check if purchase_data has exactly four values
        if len(purchase_data) != 4:
            return purchase_data

        passenger_id, ticket_id, train_id, seat_number = purchase_data

        # Check if passenger_id, ticket_id, and train_id exist
        if not passenger_exists(passenger_id):
            return "Passenger ID does not exist. Please provide a valid passenger ID."
        if not ticket_exists(ticket_id):
            return "Ticket ID does not exist. Please provide a valid ticket ID."
        if not train_exists(train_id):
            return "Train ID does not exist. Please provide a valid train ID."
        if not seat_number_valid(train_id, seat_number):
            return "Seat number is not valid for the given train ID."

        select_query = "SELECT * FROM Buy WHERE train_id = ? AND seat_number = ?"
        cursor.execute(select_query, (train_id, seat_number))
        existing_purchase = cursor.fetchone()

        if existing_purchase:
            return "A purchase with the same values already exists."

        # Update query to set is_valid to 0 for the ticket
        update_ticket_query = "UPDATE Ticket SET is_valid = 0 WHERE ticket_id = ?"
        cursor.execute(update_ticket_query, (ticket_id,))
        
        # Commit the update
        conn.commit()

        # Update query for Seats table
        update_seats_query = "UPDATE Seats SET is_valid = 0 WHERE train_id = ? AND seat_number = ?"
        cursor.execute(update_seats_query, (train_id, seat_number))

        conn.commit()

        # Insert query for Buy table
        insert_query = "INSERT INTO Buy (passenger_id, ticket_id, train_id, seat_number) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_query, (passenger_id, ticket_id, train_id, seat_number))

        # Commit the transaction
        conn.commit()

        return "Purchase entry added successfully!"

    except Exception as e:
        # Rollback in case of any error
        if conn:
            conn.rollback()
        print(f"Error adding purchase entry: {str(e)}")

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_user_by_email(email):
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Select query to retrieve user details by email
        select_query = "SELECT * FROM Passenger WHERE email = ?"
        cursor.execute(select_query, (email,))

        # Fetch the result
        result = cursor.fetchone()
        if result:
            user_id, email, password, name  , phone , age , gender = result
            return "passenger" , email, name  , phone , age , gender
            
        else:
            select_query = "SELECT * FROM Admin WHERE email = ?"
            cursor.execute(select_query, (email,))

            # Fetch the result
            result = cursor.fetchone()
            if result:
                user_id, email, password, name, phone = result
                return "admin" , email, name  , phone , None , None
            else:
                return None
            
        


def get_total_profit_per_trip():
    cursor = None
    conn = None
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Define the query to calculate total profit for each trip
        total_profit_query = """
        SELECT 
            t.trip_id,
            COALESCE(SUM(ti.price), 0) AS total_profit
        FROM 
            Trip t
            LEFT JOIN Ticket ti ON t.trip_id = ti.trip_id AND ti.is_valid = 0
        GROUP BY 
            t.trip_id;
        """

        # Execute the query
        cursor.execute(total_profit_query)
        
        # Fetch all results
        results = cursor.fetchall()

        # Format the results as a list of dictionaries
        profit_data = [{'trip_id': row[0], 'total_profit': row[1]} for row in results]

        return profit_data

    except Exception as e:
        print(f"Error retrieving total profit data: {str(e)}")
        return None

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def plot_total_profit_per_trip(profit_data):
    # Extract trip ids and total profits from the data
    trip_ids = [data['trip_id'] for data in profit_data]
    total_profits = [data['total_profit'] for data in profit_data]

    # Convert to numpy arrays for better handling with matplotlib
    trip_ids_np = np.array(trip_ids)
    total_profits_np = np.array(total_profits)

    # Create labels for the x-axis
    x_labels = [f"Trip {trip_id}" for trip_id in trip_ids_np]

    # Create the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(x_labels, total_profits_np, color='blue')

    # Add labels and title
    plt.xlabel('Trip ID')
    plt.ylabel('Total Profit')
    plt.title('Total Profit per Trip')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()


def get_trip_count_per_month():
    cursor = None
    conn = None
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = """
        SELECT 
            MONTH(departure_time) AS month_number,
            YEAR(departure_time) AS year_number,
            COUNT(trip_id) AS trip_count
        FROM 
            Trip
        GROUP BY 
            MONTH(departure_time), YEAR(departure_time)
        ORDER BY 
            YEAR(departure_time), MONTH(departure_time);
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return [{'month_number': row[0], 'year_number': row[1], 'trip_count': row[2]} for row in results]
    except Exception as e:
        print(f"Error retrieving trip count per month: {str(e)}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def plot_trip_count_per_month(trip_counts):
    if not trip_counts:
        print("No data to plot.")
        return

    months = [f"{row['year_number']}-{row['month_number']}" for row in trip_counts]
    trip_counts_values = [row['trip_count'] for row in trip_counts]

    plt.figure(figsize=(10, 6))
    plt.bar(months, trip_counts_values, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Trip Count')
    plt.title('Trip Count per Month')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def get_seats_taken_percentage():
    cursor = None
    conn = None
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = """
            SELECT 
                t.trip_id,
                (CAST(COUNT(s.seat_number) AS FLOAT) / tr.capacity) * 100 AS seats_taken_percentage
            FROM 
                Trip t
                INNER JOIN Seats s ON t.train_id = s.train_id
                INNER JOIN Train tr ON t.train_id = tr.train_id
            WHERE 
                s.is_valid = 0
            GROUP BY 
                t.trip_id, tr.capacity;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return [{'trip_id': row[0], 'seats_taken_percentage': row[1]} for row in results]
    except Exception as e:
        print(f"Error retrieving seats taken percentage: {str(e)}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def plot_seats_taken_percentage(data):
    if not data:
        print("No data to plot.")
        return

    num_trips = len(data)
    num_cols = min(num_trips, 3)  # Set the number of columns for subplots, maximum 3
    num_rows = (num_trips + num_cols - 1) // num_cols  # Calculate the number of rows

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 5*num_rows))
    axs = np.array(axs).flatten()   # Flatten the subplot array for easier iteration

    for i, entry in enumerate(data):
        trip_id = entry['trip_id']
        percentage = entry['seats_taken_percentage']
        ax = axs[i]

        ax.pie([percentage, 100 - percentage], labels=['Taken', 'Available'], autopct='%1.1f%%', startangle=140)
        ax.set_title(f'Seats Taken Percentage for Trip {trip_id}')
        ax.axis('equal')

    # Hide empty subplots
    for i in range(num_trips, num_cols * num_rows):
        axs[i].axis('off')

    plt.tight_layout()
    plt.show()


def add_manage(email , trip_id):
     # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        select_query = "SELECT admin_id FROM Admin WHERE email = ?"
        cursor.execute(select_query, (email,))

        row = cursor.fetchone()
        admin_id = row[0]

        select_query = "SELECT train_id FROM Trip WHERE trip_id = ?"
        cursor.execute(select_query, (trip_id,))

        row = cursor.fetchone()
        train_id = row[0]

        insert_query = "INSERT INTO Manage (admin_id, trip_id, train_id) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (admin_id, trip_id, train_id))

        conn.commit()

        return





