# Event Management System

This Python project implements a simple Event Management System using Tkinter for the GUI and MySQL for database interaction.

## Features:

- **User Login:**
    - Basic login functionality with username and password.
- **Event Management:**
    - Add new events with client details, event type, and services.
    - Calculate and display the total cost, including GST.
    - Generate and print invoices with client information, services, and pricing.
    - Store event data in a MySQL database.
- **Past Records:**
    - View a list of past events with client details, event type, invoice date, and selected services.
- **User Interface:**
    - Intuitive GUI with user-friendly forms.
    - Visual feedback and error handling.

## Technologies Used:

- Python
- Tkinter (for GUI)
- PIL (for image handling)
- MySQL (for database)
- mysql.connector (for MySQL database connectivity)

## Installation:

1. **Install required libraries:**
    ```bash
    pip install mysql-connector-python pillow
    ```

2. **Create a MySQL database:**
    - Create a database named `python_project` (or your desired name).
    - Create the following tables in the database:
      - `invoices` (columns: `id`, `client_name`, `client_contact`, `event_type`, `total_price`, `gst_amount`, `grand_total`, `invoice_date`)
      - `invoice_services` (columns: `invoice_id`, `service_name`, `quantity`, `price`)

3. **Replace placeholders:**
    - Update `mydb = mysql.connector.connect(...)` with your actual MySQL credentials (host, user, password).
    - Modify the image path variables in `load_background_image()` and `load_top_image()` with the correct paths to your images.

## Usage:

1. Run the Python script.
2. Enter the login credentials (username and password).
3. Enter client details, select the event type, and choose the required services.
4. View the calculated invoice.
5. Print the invoice (generates an image file).
6. View past records in the "Past Records" window.

## Screenshots

### Login Window
![image](https://github.com/user-attachments/assets/848b99bd-0091-4b1e-b1b9-fa81b75fdfb1)

### Main Window
![image](https://github.com/user-attachments/assets/67ce9b01-3321-492a-8b62-4351ffe16054)

### Invoice
![tmpkh4bpptm](https://github.com/user-attachments/assets/2123af53-b879-4bff-819b-b2e30f76b8e4)

## Note:

- This is a basic implementation and can be further enhanced with features like:
  - Advanced search and filtering for past records.
  - User role-based access control.
  - More sophisticated invoice printing options (e.g., PDF generation).
  - Integration with payment gateways.

- The invoice printing functionality relies on an existing invoice template image (`Invoice.jpg`). You'll need to create and adjust this image according to your needs.

## Disclaimer:

This code is provided for educational and demonstration purposes only. It may require modifications and improvements for real-world use.
