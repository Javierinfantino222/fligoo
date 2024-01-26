
\c testfligoo;
CREATE TABLE IF NOT EXISTS testdata (
    flight_id SERIAL PRIMARY KEY,
    flight_date DATE,
    flight_status VARCHAR(255),
    departure_airport VARCHAR(255),
    departure_timezone VARCHAR(255),
    arrival_airport VARCHAR(255),
    arrival_timezone VARCHAR(255),
    arrival_terminal VARCHAR(255),
    airline_name VARCHAR(255),
    flight_number VARCHAR(255)
);
