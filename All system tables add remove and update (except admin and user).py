import pypyodbc as odbc


# Set up connection parameters
server = 'YOUSSEF'
database = 'TEST2'
username = 'jojo'
password = '812200388'
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
        exists = cursor.fetchone() is not None

        return exists

    except Exception as e:
        print(f"Error checking admin existence: {str(e)}")
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

        print("Train inserted successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error inserting train: {str(e)}")

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

        print("Train details updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error updating train details: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def get_all_trains():
    trains = {}
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

        # Loop through the rows and store data in a dictionary
        for row in rows:
            train_id, train_model, capacity = row
            trains[train_id] = {'train_model': train_model, 'capacity': capacity}

    except Exception as e:
        print(f"Error retrieving trains: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

    return trains


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

        print("Train removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error removing train: {str(e)}")

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
            # Check if start_station_id and end_station_id exist in the Stations table
            if station_exists(start_station_id) and station_exists(end_station_id):
                # Insert query
                insert_query = "INSERT INTO Ticket (price, tier, start_station_id, end_station_id, trip_id) VALUES (?, ?, ?, ?, ?)"

                # Add tickets individually
                for _ in range(quantity):
                    # Execute the query with parameters
                    cursor.execute(insert_query, (price, tier, start_station_id, end_station_id, trip_id))

                # Commit the transaction
                conn.commit()

                print(f"{quantity} tickets added successfully!")
            else:
                print("Start or end station ID does not exist. Please provide valid station IDs.")
        else:
            print("Trip ID does not exist. Please provide a valid trip ID.")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error adding tickets: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()



def remove_ticket(ticket_id):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Delete query
        delete_query = "DELETE FROM Ticket WHERE ticket_id = ?"

        # Execute the query with parameters
        cursor.execute(delete_query, (ticket_id,))

        # Commit the transaction
        conn.commit()

        print("Ticket removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error removing ticket: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def update_ticket(ticket_id, new_price=None, new_tier=None, new_start_station_id=None, new_end_station_id=None, new_trip_id=None):
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
        if new_trip_id is not None:
            if trip_exists(new_trip_id):
                update_query += "trip_id = ?, "
                update_params.append(new_trip_id)
            else:
                print("Trip ID does not exist. Please provide a valid trip ID.")
                return

        # Remove the trailing comma and space
        update_query = update_query.rstrip(', ')

        # Append WHERE clause
        update_query += " WHERE ticket_id = ?"
        update_params.append(ticket_id)

        # Execute the query with parameters
        cursor.execute(update_query, update_params)

        # Commit the transaction
        conn.commit()

        print("Ticket details updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error updating ticket details: {str(e)}")

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


def add_trip(departure_time, arrival_time, train_id):
    try:
        # Check if train_id exists
        if not train_exists(train_id):
            print("Train ID does not exist. Please provide a valid train ID.")
            return

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Insert query
        insert_query = "INSERT INTO Trip (departure_time, arrival_time, train_id) VALUES (?, ?, ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (departure_time, arrival_time, train_id))

        # Commit the transaction
        conn.commit()

        print("Trip added successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error adding trip: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def update_trip(trip_id, new_departure_time=None, new_arrival_time=None, new_train_id=None):
    try:
        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Update query
        update_query = "UPDATE Trip SET "
        update_params = []

        if new_departure_time is not None:
            update_query += "departure_time = ?, "
            update_params.append(new_departure_time)
        if new_arrival_time is not None:
            update_query += "arrival_time = ?, "
            update_params.append(new_arrival_time)
        if new_train_id is not None:
            if not train_exists(new_train_id):
                print("New train ID does not exist. Please provide a valid train ID.")
                return
            else:
                update_query += "train_id = ?, "
                update_params.append(new_train_id)

        # Remove the trailing comma and space
        update_query = update_query.rstrip(', ')

        # Append WHERE clause
        update_query += " WHERE trip_id = ?"
        update_params.append(trip_id)

        # Execute the query with parameters
        cursor.execute(update_query, update_params)

        # Commit the transaction
        conn.commit()

        print("Trip details updated successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error updating trip details: {str(e)}")

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

        print("Trip removed successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error removing trip: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def add_purchase(passenger_id, ticket_id, train_id, seat_number):
    try:
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

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Insert query
        insert_query = "INSERT INTO Buy (passenger_id, ticket_id, train_id, seat_number) VALUES (?, ?, ?, ?)"

        # Execute the query with parameters
        cursor.execute(insert_query, (passenger_id, ticket_id, train_id, seat_number))

        # Commit the transaction
        conn.commit()

        print("Purchase entry added successfully!")

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"Error adding purchase entry: {str(e)}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


def update_purchase(passenger_id, ticket_id, train_id, seat_number, new_seat_number):
    try:
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

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

        # Update query
        update_query = "UPDATE Buy SET seat_number = ? WHERE passenger_id = ? AND ticket_id = ? AND train_id = ? AND seat_number = ?"

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

def remove_purchase(passenger_id, ticket_id, train_id, seat_number):
    try:
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

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

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

def add_manage_entry(admin_id, trip_id, train_id):
    try:
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

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

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

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

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

        # Establish connection
        conn = odbc.connect(connection_string)

        # Create a cursor object
        cursor = conn.cursor()

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






