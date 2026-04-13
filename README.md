# Geolocation Data Project

This project retrieves geographic data from an API and stores it in a SQLite database.  
The stored data is then converted into a JavaScript file that can be used to visualize locations on a map.

## Project Files

- **geoload.py**  
  Reads addresses from `where.data`, sends requests to the API, and stores the results in a SQLite database.

- **geodump.py**  
  Reads the stored JSON data from the database and converts it into a JavaScript file (`where.js`) used for map visualization.

- **where.data**  
  A text file containing a list of locations to be processed.

## Technologies Used

- Python
- SQLite
- JSON
- HTTP Requests
- API Data Processing

## How It Works

1. The script reads location names from `where.data`.
2. It sends a request to the API to get geographic data.
3. The response is stored in a SQLite database (`opengeo.sqlite`).
4. Another script reads the stored data and generates a JavaScript file for map visualization.

## Run the Project

Run the scripts in order:

```bash
python geoload.py
python geodump.py