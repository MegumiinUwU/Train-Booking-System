# Train Booking System Database Project

## Introduction

This database project is centered around the development of a train system database using Microsoft SQL Server. It was undertaken as part of the coursework at the Faculty of Computers and Artificial Intelligence, Cairo University (FCAI).

The primary focus of this project is on the design and implementation of the database, as well as the creation of SQL queries to interact with the data. Additionally, the project features a simple user interface developed in Python, allowing users to manipulate the database without the need to write SQL queries manually. Instead, users can input values and interact with the database through intuitive button clicks.

## Tables and Relationships

The database schema for the train system consists of several tables, each serving a specific purpose. Below is a description of each table and the relationships between them:

### Tables

1. **Admin**
    - **admin_id**: INT IDENTITY(1,1) PRIMARY KEY
    - **email**: VARCHAR(255) UNIQUE
    - **password**: VARCHAR(255)
    - **name**: VARCHAR(255)
    - **phone**: VARCHAR(20)

2. **Passenger**
    - **passenger_id**: INT IDENTITY(1,1) PRIMARY KEY
    - **email**: VARCHAR(255) UNIQUE
    - **password**: VARCHAR(255)
    - **name**: VARCHAR(255)
    - **phone**: VARCHAR(20)
    - **age**: INT
    - **gender**: VARCHAR(10)

3. **Train**
    - **train_id**: INT IDENTITY(1,1) PRIMARY KEY
    - **train_model**: VARCHAR(255)
    - **capacity**: INT

4. **Stations**
    - **station_id**: INT IDENTITY(1,1) PRIMARY KEY
    - **name**: VARCHAR(255)
    - **location**: VARCHAR(255)

5. **Seats**
    - **train_id**: INT
    - **seat_number**: INT
    - **seat_tier**: VARCHAR(20)
    - **is_valid**: BIT
    - **trip_id**: INT


6. **Trip**
    - **trip_id**: INT IDENTITY(1,1) PRIMARY KEY
    - **departure_time**: DATETIME
    - **arrival_time**: DATETIME
    - **start_station_id**: INT
    - **end_station_id**: INT
    - **train_id**: INT


7. **Ticket**
    - **ticket_id**: INT IDENTITY(1,1) PRIMARY KEY
    - **price**: NUMERIC(10,2)
    - **tier**: VARCHAR(20)
    - **is_valid**: BIT DEFAULT 1
    - **start_station_id**: INT
    - **end_station_id**: INT
    - **trip_id**: INT


8. **Manage**
    - **admin_id**: INT
    - **trip_id**: INT
    - **train_id**: INT


9. **Buy**
    - **passenger_id**: INT
    - **ticket_id**: INT
    - **train_id**: INT
    - **seat_number**: INT


### Relationships

- **Admin** to **Trip** and **Train**: The `Manage` table establishes a many-to-many relationship between admins and trips/trains, indicating which admin is responsible for managing which trip with the train assigned.
- **Train** to **Seats**: Each train has multiple seats, and the relationship is established through the `train_id` foreign key in the `Seats` table.
- **Trip** to **Stations**: Each trip has a start and end station, linked through `start_station_id` and `end_station_id` foreign keys in the `Trip` table.
- **Trip** to **Train**: Each trip is associated with one train, and this relationship is defined by the `train_id` foreign key in the `Trip` table.
- **Trip** to **Ticket**: Tickets are issued for specific trips, and this relationship is defined by the `trip_id` foreign key in the `Ticket` table.
- **Passenger** to **Ticket**: Passengers buy tickets, and this relationship is defined in the `Buy` table, linking `passenger_id` and `ticket_id`.
- **Train** to **Seats** to **Trip**: Seats are assigned to specific trains and trips, linking the `Seats` and `Trip` tables via `train_id` and `trip_id` foreign keys.

These tables and relationships form the backbone of the train system database, enabling efficient management of train schedules, ticketing, and passenger information.

<iframe src="README images and gifs/ERD.pdf" width="600px" height="500px"></iframe>

Check the SQL code directory for more about the implementation, defined views, and functions

## Simple Main UI

<img src="README images and gifs/1.gif" alt="Add Record Feature" width="800px" />



## Features

### 1. Ability to Add Any Record for Each Table
The application provides an intuitive user interface to add new records to any table in the database. Users can easily input the required data and submit it without needing to write SQL queries manually.

<img src="README images and gifs/ADD TRIP.gif" alt="Add Record Feature" width="800px" />

### 2. Ability to Sign Up and Log In
Users can sign up and log in securely. Passwords are hashed to ensure user data security.

<img src="README images and gifs/SIGNUP.gif" alt="Sign Up and Log In Feature" width="800px" />

<img src="README images and gifs/Hash.png" alt="Sign Up and Log In Feature" width="800px" />

### 3. Ability to Update or Remove Any Records
Users can update or delete records across the database tables. This includes the ability for users to update their profile information.

<img src="README images and gifs/Edit trip.gif" alt="Update or Remove Records Feature" width="800px" />

<img src="README images and gifs/Remove trip.gif" alt="Update or Remove Records Feature" width="800px" />

### 4. Ticket Purchase Functionality
Passengers can buy tickets with a simple click. This action automatically updates three tables: it adds a record to the `Buy` table and marks the corresponding seat and ticket as reserved.

<img src="README images and gifs/Buy Ticket.gif" alt="Ticket Purchase Feature" width="800px" />

### 5. Generating Reports with Simple Graphs
The system can generate various reports with simple graphs, including:
- Total revenue for each trip.
- Total trips per month.
- A pie chart showing the percentage of train seats occupied on a certain trip, which helps in optimizing train capacity based on passenger demand.

<img src="README images and gifs/Reports.gif" alt="Reports and Graphs Feature" width="800px" />

## Exception Handling

In this project, we placed a strong emphasis on handling exceptions to ensure data integrity and a smooth user experience. Here are some key areas where exception handling is implemented:

### 1. Validating Trip Dates
We ensure that the arrival date and time of a trip are always after the departure date and time. Any attempt to create a trip record where the arrival time precedes the departure time is immediately rejected with an appropriate error message.

<img src="README images and gifs/Exception Handling 2.gif" alt="Trip Date Exception Handling" width="800px" />

### 2. Validating User Sign-Up Information
During the sign-up process, we validate the email format to ensure it is a valid email address. Invalid emails are not accepted, and users are prompted to enter a correct email format.

<img src="README images and gifs/Exception Handling 1.gif" alt="Sign-Up Email Validation" width="800px" />

### 3. Avoiding Duplicate Train Assignments
The system prevents the same train from being assigned to multiple trips that overlap in time. If an attempt is made to assign a train to conflicting trips, the system raises an error and informs the admin of the conflict.


### 4. Ensuring Referential Integrity
We handle critical exceptions that could disturb referential integrity. For example, when attempting to delete or update records that are referenced by other tables, the system checks for these dependencies and prevents actions that would violate referential integrity constraints.


### 5. Comprehensive Input Validation
Throughout the application, we perform thorough input validation for all forms and data entries. This includes checking for:
- Non-nullable fields being filled.
- Correct data types and value ranges.
- Unique constraints, such as unique emails for both admins and passengers.


These exception handling mechanisms ensure that the database remains consistent, accurate, and secure, providing a reliable foundation for the train system.

## Technologies Used



### Database

- **Microsoft SQL Server**: The primary database management system used for storing and managing the train system data.

### Programming Language

- **Python**: The main programming language used for developing the application and its user interface.

### Python Libraries

### Python Libraries

- **pyodbc**: Used to connect and interact with the SQL Server database.
- **numpy**: Utilized for numerical operations and data manipulation.
- **matplotlib**: Employed for generating plots and visualizations, particularly in the reporting features.
- **tkcalendar**: A widget used for selecting dates, enhancing the user experience for scheduling trips.
- **tkinter**: Used for creating the graphical user interface (GUI) of the application.
- **hashlib**: Utilized for hashing passwords to ensure secure user authentication.
- **re**: A module for handling regular expressions, used for input validation, such as checking email formats.


These technologies were chosen for their reliability, ease of use, and extensive support, ensuring a smooth development process.

## Conclusion

We believe that this project serves as a valuable resource for learning, offering insights into data management best practices and showcasing the power of modern technologies in solving real-world challenges.

We welcome feedback, and suggestions from the community to further improve and enhance our skills and learn more.


