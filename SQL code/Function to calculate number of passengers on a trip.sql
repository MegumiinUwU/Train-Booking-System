CREATE FUNCTION dbo.GetNumPassengersForTrip(@trip_id INT)
RETURNS INT
AS
BEGIN
    DECLARE @num_passengers INT;
    SELECT @num_passengers = COUNT(*)
    FROM Ticket
    WHERE trip_id = @trip_id;
    RETURN @num_passengers;
END;
GO -- Add a semicolon to end the function definition

-- Add a computed column to the Trip table to use the user-defined function
ALTER TABLE Trip
ADD num_passengers AS dbo.GetNumPassengersForTrip(trip_id);
