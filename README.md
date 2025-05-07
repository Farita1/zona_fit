# ZonaFit Project

This project is a client management application for a gym, developed in Python. It allows registering, querying, and managing clients using a database, either through the terminal or a graphical interface.

## Project Structure

- **logger_base.py**: Handles logging. It creates a `capa_dato.log` file that stores logs of all processed operations.

- **cliente.py**: Defines the `Cliente` class with attributes: `id`, `name`, `last name`, and `membership`.

- **clientedao.py**: Implements the DAO (Data Access Object) pattern to perform CRUD operations on client data.

- **conexion.py**: Manages the database connection using a connection pool for better performance and resource reuse.

- **cursor_del_pool.py**: Implements a context manager (`with`) that obtains a cursor from the connection pool. It automatically commits or rolls back transactions depending on whether an exception occurs. Example usage:
  
app_zona_fit.py: Main application logic for terminal use. Allows interaction with client data through command-line input.

app_zona_fit_GUI.py: Graphical interface version of the application, built using PySide or Tkinter, offering a more user-friendly experience.

Requirements
Python 3.x

GUI library (PySide6 or Tkinter, depending on implementation)

Database (MySQL, PostgreSQL, or any supported by your setup)

Standard libraries: logging, psycopg2, mysql-connector-python, etc.

How to Use
Clone the repository.

Set up your database and update the connection parameters in conexion.py.

Run app_zona_fit.py for the terminal version or app_zona_fit_GUI.py for the graphical interface.
