import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sai@123',
    port='3306',
    database='python_project'
)


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.state("zoomed")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_login_form()
        # Load and display the background image
        self.load_background_image()
        # Load and display the top image
        self.load_top_image()

    def create_login_form(self):
        login_frame = tk.Frame(self.root, width=400, height=300, bg='pink')
        login_frame.pack_propagate(False)  # Prevent frame from resizing to fit its contents
        login_frame.pack(padx=20, pady=20)

        # Centering labels and button
        username_label = tk.Label(login_frame, text="USERNAME:", bg='pink', fg='black', font=("Helvetica", 12, "bold"))
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        username_entry = tk.Entry(login_frame, textvariable=self.username, font=("Helvetica", 12, "bold"))
        username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        password_label = tk.Label(login_frame, text="PASSWORD:", bg='pink', fg='black', font=("Helvetica", 12, "bold"))
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        password_entry = tk.Entry(login_frame, textvariable=self.password, show='*', font=("Helvetica", 12, "bold") )
        password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        login_button = tk.Button(login_frame, text="Login", command=self.check_login, font=("Helvetica", 12, "bold"))
        login_button.grid(row=2, columnspan=2, pady=20)

        # Positioning the entire login frame near the top of the root window
        login_frame.place(relx=0.5, rely=0.1, anchor=tk.N)

    def load_background_image(self):
        try:
            # Load image using PIL
            image_path = r"C:\Users\cheve\PycharmProjects\Python Project\Screenshot 2025-01-14 124404.png"
            img = Image.open(image_path)
            img = img.resize(
                (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))  # Resize image to fit screen
            self.background_image = ImageTk.PhotoImage(img)

            # Create a label to hold the image and place it in the root window
            background_label = tk.Label(self.root, image=self.background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

            # Ensure the label is behind all other widgets
            background_label.lower()

        except FileNotFoundError:
            messagebox.showerror("Error", "Failed to load background image.")

    def load_top_image(self):
        try:
            image_path = r"C:\Users\cheve\PycharmProjects\Python Project\Aurora.jpg"  # Update with your actual image file name
            img = Image.open(image_path)
            img = img.resize((200, 200))  # Resize image to fit the window width
            self.top_image = ImageTk.PhotoImage(img)

            # Display the image in a label in the top right corner
            image_label = tk.Label(self.root, image=self.top_image)
            image_label.place(relx=1.0, x=-20, y=20, anchor=tk.NE)  # Position at top right with offset

        except FileNotFoundError:
            messagebox.showerror("Error", "Failed to load top image.")

    def check_login(self):
        username = self.username.get()
        password = self.password.get()

        # Check the credentials (this is just a placeholder, implement your own logic)
        if username == "learning3" and password == "12345":
            self.root.destroy()  # Close the login window
            main_app()  # Open the main application
        else:
            messagebox.showerror("Error", "Invalid username or password")


def main_app():
    root = tk.Tk()
    EventManagementSystem(root)
    root.mainloop()

class EventManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.state("zoomed")

        self.client_name = tk.StringVar()
        self.client_contact = tk.StringVar()
        self.event_type = tk.StringVar()

        self.event_items = {
            "Conference": {
                "Chairs": 50,
                "Tables": 500,
                "Projector and Screen": 5000,
                "Microphones": 2000,
                "Sound System": 20000,
                "Name Tags and Lanyards": 20,
                "Notepads and Pens": 50,
                "Refreshments": 200
            },
            "Meeting": {
                "Chairs": 50,
                "Tables": 500,
                "Projector and Screen": 5000,
                "Microphones": 2000,
                "Refreshments": 100
            },
            "Product Launch": {
                "Chairs": 50,
                "Stage": 15000,
                "Projector and Screen": 5000,
                "Sound System": 20000,
                "Branding Materials": 10000,
                "Refreshments": 300
            },
            "Workshop": {
                "Chairs": 50,
                "Tables": 500,
                "Materials": 50,
                "Projector and Screen": 5000,
                "Refreshments": 200
            },
            "Wedding": {
                "Chairs": 50,
                "Tables": 500,
                "Linens and Centerpieces": 1000,
                "Dance Floor": 10000,
                "Catering": 1000,
                "Drinks": 500,
                "Decorations": 30000,
                "DJ/Band": 25000
            },
            "Birthday Party": {
                "Chairs": 50,
                "Tables": 500,
                "Catering": 500,
                "Drinks": 200,
                "Decorations": 10000,
                "Entertainment": 15000
            },
            "Festival": {
                "Stalls/Tents": 2000,
                "Chairs": 50,
                "Tables": 500,
                "Stage": 15000,
                "Sound System": 20000,
                "Decorations": 10000,
                "Refreshments": 300
            },
            "Parade": {
                "Parade Floats": 50000,
                "Seating": 50,
                "Barricades": 20000,
                "Sound System": 20000
            },
            "Concert": {
                "Seating": 50,
                "Stage": 15000,
                "Sound System": 20000,
                "Lighting": 15000,
                "Refreshments": 300
            },
            "Theatrical Performance": {
                "Seating": 50,
                "Stage": 15000,
                "Sound System": 20000,
                "Lighting": 15000,
                "Costumes and Props": 10000
            },
            "Lectures and Talks": {
                "Seating": 50,
                "Tables": 500,
                "Projector and Screen": 5000,
                "Sound System": 20000,
                "Notepads and Pens": 50,
                "Refreshments": 200
            },
            "Science Fair": {
                "Exhibition Stalls": 2000,
                "Seating": 50,
                "Tables": 500,
                "Projector and Screen": 5000,
                "Materials": 20000,
                "Refreshments": 200
            },
            "Webinar": {
                "Webinar Platform Subscription": 15000,
                "Microphones and Cameras": 10000,
                "Presentation Materials": 5000,
                "Technical Support": 10000
            },
            "Hybrid Event": {
                "Seating": 50,
                "Tables": 500,
                "Projector and Screen": 5000,
                "Sound System": 20000,
                "Cameras and Streaming Equipment": 20000,
                "Refreshments": 20000
            },
            "Private Dinner": {
                "Seating": 50,
                "Tables": 500,
                "Table Settings": 100,
                "Catering": 800,
                "Decorations": 20000,
                "Drinks": 500
            },
            "Private Celebration": {
                "Seating": 50,
                "Tables": 500,
                "Decorations": 15000,
                "Catering": 500,
                "Drinks": 200,
                "Entertainment": 15000
            },
            "Others": {}  # This will be populated with all items
        }

        # Populate "Others" with all items
        for event, items in self.event_items.items():
            if event != "Others":
                self.event_items["Others"].update(items)

        self.orders = {}

        self.gst_percentage = 18

        self.create_gui()
        self.invoice_manager = self.InvoiceManager(self.convert_to_inr)

    def create_gui(self):
        # Create GUI components
        details_frame = tk.LabelFrame(self.root, text="Client Details", fg="Crimson", font=("Helvetica", 12, "bold"))
        details_frame.pack(fill="x", padx=10, pady=10)

        name_label = tk.Label(details_frame, text="Name:",fg="Teal", font=("Helvetica", 12, "bold"))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        name_entry = tk.Entry(details_frame, textvariable=self.client_name, font=("Helvetica", 12, "bold"))
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        contact_label = tk.Label(details_frame, text="Contact:",fg="Teal", font=("Helvetica", 12, "bold"))
        contact_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        contact_entry = tk.Entry(details_frame, textvariable=self.client_contact, font=("Helvetica", 12, "bold"))
        contact_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        contact_entry.configure(validate="key", validatecommand=(self.root.register(self.validate_contact), "%P"))

        event_type_label = tk.Label(details_frame, text="Event Type:",fg="Teal", font=("Helvetica", 12, "bold"))
        event_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        event_type_combo = ttk.Combobox(details_frame, textvariable=self.event_type, font=("Helvetica", 12, "bold"))
        event_type_combo['values'] = list(self.event_items.keys())
        event_type_combo.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        event_type_combo.bind("<<ComboboxSelected>>", self.update_services)

        self.services_frame = tk.LabelFrame(self.root, text="Services",fg="Crimson", font=("Helvetica", 12, "bold"))
        self.services_frame.pack(fill="both", expand=True, padx=10, pady=10)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(fill="x", padx=10, pady=10)

        print_invoice_button = tk.Button(buttons_frame, text="Print Invoice", command=self.show_invoice_popup, font=("Helvetica", 12, "bold"))
        print_invoice_button.pack(side="left", padx=5)

        past_record_button = tk.Button(buttons_frame, text="Past Records", command=self.past_records, font=("Helvetica", 12, "bold"))
        past_record_button.pack(side="left", padx=5)

        clear_selection_button = tk.Button(buttons_frame, text="Clear Selection", command=self.clear_selection, font=("Helvetica", 12, "bold"))
        clear_selection_button.pack(side="left", padx=5)

        self.sample_invoice_text = tk.Text(self.root, height=10)
        self.sample_invoice_text.pack(fill="x", padx=10, pady=10)

    def validate_contact(self, value_if_allowed):
        if value_if_allowed.isdigit() and len(value_if_allowed) <= 10:
            if len(value_if_allowed) == 0 or (len(value_if_allowed) == 1 and value_if_allowed[0] in '6789'):
                return True
            elif len(value_if_allowed) > 1:
                return True
        return False

    def update_services(self, event):
        for widget in self.services_frame.winfo_children():
            widget.destroy()

        event_type = self.event_type.get()
        if event_type not in self.event_items or event_type == "":
            self.orders = {}
            return

        services = self.event_items.get(event_type, {})

        service_header = tk.Label(self.services_frame, text="Services")
        service_header.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        quantity_header = tk.Label(self.services_frame, text="Quantity")
        quantity_header.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        total_header = tk.Label(self.services_frame, text="Total")
        total_header.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.orders = {}

        row = 1
        for service, price in services.items():
            service_var = tk.IntVar()
            service_label = tk.Label(self.services_frame, text=f"{service} - {self.convert_to_inr(price)}")
            service_label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

            quantity_entry = tk.Entry(self.services_frame, width=5)
            quantity_entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")

            total_label = tk.Label(self.services_frame, text="")
            total_label.grid(row=row, column=2, padx=5, pady=5, sticky="w")

            quantity_entry.configure(validate="key", validatecommand=(self.root.register(self.validate_quantity), "%P"))
            quantity_entry.bind("<KeyRelease>",
                                lambda e, s=service, p=price, q=quantity_entry, t=total_label: self.calculate_total(e,
                                                                                                                    s,
                                                                                                                    p,
                                                                                                                    q,
                                                                                                                    t))

            self.orders[service] = {
                "price": price,
                "quantity_entry": quantity_entry,
                "total_label": total_label
            }

            row += 1

    def validate_quantity(self, value_if_allowed):
        if value_if_allowed.isdigit() or value_if_allowed == "":
            return True
        return False

    def calculate_total(self, event, service, price, quantity_entry, total_label):
        try:
            quantity = int(quantity_entry.get())
            total = quantity * price
            total_label.config(text=self.convert_to_inr(total))
            self.update_invoice_text()  # Update invoice details automatically
        except ValueError:
            total_label.config(text="")


    def update_invoice_text(self):
        client_name = self.client_name.get()
        client_contact = self.client_contact.get()
        event_type = self.event_type.get()

        if not client_name or not client_contact or not event_type:
            return

        total_price = 0
        selected_services = []

        for service, details in self.orders.items():
            try:
                quantity = int(details["quantity_entry"].get())
                price = details["price"]
                total = quantity * price
                total_price += total
                selected_services.append((service, quantity, price))
            except ValueError:
                continue

        gst_amount = (total_price * self.gst_percentage) / 100
        grand_total = total_price + gst_amount

        invoice_text = f"Client Name: {client_name}\n"
        invoice_text += f"Contact: {client_contact}\n"
        invoice_text += f"Event Type: {event_type}\n\n"

        invoice_text += f"{'Service':<30}{'Quantity':<10}{'Price':<15}{'Total':<15}\n"
        invoice_text += "-"*70 + "\n"

        for service, quantity, price in selected_services:
            total = quantity * price
            invoice_text += f"{service:<30}{quantity:<10}{self.convert_to_inr(price):<15}{self.convert_to_inr(total):<15}\n"

        invoice_text += "-"*70 + "\n"
        invoice_text += f"{'Total Price':<55}{self.convert_to_inr(total_price):<15}\n"
        invoice_text += f"{'GST ({self.gst_percentage}%)':<55}{self.convert_to_inr(gst_amount):<15}\n"
        invoice_text += f"{'Grand Total':<55}{self.convert_to_inr(grand_total):<15}\n"

        self.sample_invoice_text.delete(1.0, tk.END)
        self.sample_invoice_text.insert(tk.END, invoice_text)

    def show_invoice_popup(self):
        client_name = self.client_name.get()
        client_contact = self.client_contact.get()
        event_type = self.event_type.get()

        if not client_name or not client_contact or not event_type:
            messagebox.showerror("Error", "Please fill all the details")
            return

        total_price = 0
        selected_services = []

        for service, details in self.orders.items():
            try:
                quantity = int(details["quantity_entry"].get())
                price = details["price"]
                total = quantity * price
                total_price += total
                selected_services.append((service, quantity, price))
            except ValueError:
                continue

        gst_amount = (total_price * self.gst_percentage) / 100
        grand_total = total_price + gst_amount

        invoice_text = f"Client Name:  {client_name}\n"
        invoice_text += f"Contact: {client_contact}\n"
        invoice_text += f"Event Type: {event_type}\n\n"

        invoice_text += f"{'Service':<30}{'Quantity':<10}{'Price':<15}{'Total':<15}\n"
        invoice_text += "-"*70 + "\n"

        for service, quantity, price in selected_services:
            total = quantity * price
            invoice_text += f"{service:<30}{quantity:<10}{self.convert_to_inr(price):<15}{self.convert_to_inr(total):<15}\n"

        invoice_text += "-"*70 + "\n"
        invoice_text += f"{'Total Price':<55}{self.convert_to_inr(total_price):<15}\n"
        invoice_text += f"{'GST ({self.gst_percentage}%)':<55}{self.convert_to_inr(gst_amount):<15}\n"
        invoice_text += f"{'Grand Total':<55}{self.convert_to_inr(grand_total):<15}\n"

        self.sample_invoice_text.delete(1.0, tk.END)
        self.sample_invoice_text.insert(tk.END, invoice_text)

        self.invoice_manager.save_invoice_to_db(client_name, client_contact, event_type, total_price, gst_amount, grand_total, selected_services)

    def past_records(self):
        # Create a new window for past records
        past_records_window = tk.Toplevel(self.root)
        past_records_window.title("Past Records")

        try:
            # Fetch records from invoice_services and invoices tables
            cursor = mydb.cursor()

            cursor.execute("""
                       SELECT i.id, i.client_name, i.event_type, i.invoice_date, 
                              GROUP_CONCAT(CONCAT(iv.service_name, ' (', iv.quantity, ')') SEPARATOR ', ') AS selected_services
                       FROM invoices i
                       INNER JOIN invoice_services iv ON i.id = iv.invoice_id
                       GROUP BY i.id
                   """)
            records = cursor.fetchall()

            # Create a Treeview widget for displaying records
            tree = ttk.Treeview(past_records_window)
            tree["columns"] = ("#1", "#2", "#3", "#4")
            tree.heading("#0", text="ID")
            tree.heading("#1", text="Client Name")
            tree.heading("#2", text="Event Type")
            tree.heading("#3", text="Invoice Date")
            tree.heading("#4", text="Selected Services")

            # Calculate column widths based on content
            tree.column("#0", width=50, minwidth=50)
            tree.column("#1", width=self.calculate_column_width(records, 1), anchor="w")
            tree.column("#2", width=self.calculate_column_width(records, 2), anchor="w")
            tree.column("#3", width=self.calculate_column_width(records, 3), anchor="w")
            tree.column("#4", width=self.calculate_column_width(records, 4), anchor="w")

            # Insert records into the Treeview
            for record in records:
                tree.insert("", tk.END, text=record[0], values=(record[1], record[2], record[3], record[4]))

            tree.pack(expand=True, fill="both")

            cursor.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def clear_selection(self):
        self.client_name.set("")
        self.client_contact.set("")
        self.event_type.set("")
        self.update_services(None)
        self.sample_invoice_text.delete(1.0, tk.END)

    class InvoiceManager:

        def __init__(self, convert_to_inr):
            self.convert_to_inr = convert_to_inr

        def save_invoice_to_db(self, client_name, client_contact, event_type, total_price, gst_amount, grand_total,
                               selected_services):
            try:
                cursor = mydb.cursor()

                invoice_query = """
                INSERT INTO invoices (client_name, client_contact, event_type, total_price, gst_amount, grand_total, invoice_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                invoice_data = (
                    client_name,
                    client_contact,
                    event_type,
                    total_price,
                    gst_amount,
                    grand_total,
                    datetime.datetime.now().strftime('%Y-%m-%d')
                )

                cursor.execute(invoice_query, invoice_data)
                invoice_id = cursor.lastrowid

                service_query = """
                INSERT INTO invoice_services (invoice_id, service_name, quantity, price)
                VALUES (%s, %s, %s, %s)
                """
                for service, quantity, price in selected_services:
                    cursor.execute(service_query, (invoice_id, service, quantity, price))

                mydb.commit()
                cursor.close()
                messagebox.showinfo("Success", "Invoice saved to database successfully.")

                # Call the function to print the invoice
                self.print_invoice(client_name, client_contact, event_type, total_price, gst_amount, grand_total,
                                   selected_services)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

        def draw_client_details(self, draw, font, x_left_column, x_right_column, y, line_spacing, client_name,
                                client_contact, event_type):
            draw.text((x_left_column, y), "Client Name:      ", fill="black", font=font)
            draw.text((x_right_column, y), f"{client_name}", fill="black", font=font)
            y += line_spacing
            draw.text((x_left_column, y), f"Client Contact:      {client_contact}", fill="black", font=font)
            y += line_spacing
            draw.text((x_left_column, y), f"Event Type:       {event_type}", fill="black", font=font)
            y += line_spacing
            return y

        def draw_services_section(self, draw, font, x, y, line_spacing, selected_services):
            # Determine maximum lengths for each column
            max_service_length = max(len(service) for service, _, _ in selected_services)
            max_quantity_length = max(len(str(quantity)) for _, quantity, _ in selected_services)
            max_price_length = max(len(self.convert_to_inr(price)) for _, _, price in selected_services)
            max_total_length = max(
                len(self.convert_to_inr(quantity * price)) for _, quantity, price in selected_services)

            # Calculate starting positions for each column
            service_start = x
            quantity_start = service_start + max_service_length + 300
            price_start = quantity_start + max_quantity_length + 250
            total_start = price_start + max_price_length + 250

            # Draw table header
            draw.text((service_start, y), "Service", fill="black", font=font)
            draw.text((quantity_start, y), "Quantity", fill="black", font=font)
            draw.text((price_start, y), "Price", fill="black", font=font)
            draw.text((total_start, y), "Total", fill="black", font=font)
            y += line_spacing

            # Draw separator line
           # draw.line([(service_start, y), (total_start, y)], fill="black")
           # y += line_spacing

            # Draw each service row
            for service, quantity, price in selected_services:
                total = quantity * price
                draw.text((service_start, y), service, fill="black", font=font)
                draw.text((quantity_start, y), str(quantity), fill="black", font=font)
                draw.text((price_start, y), self.convert_to_inr(price), fill="black", font=font)
                draw.text((total_start, y), self.convert_to_inr(total), fill="black", font=font)
                y += line_spacing

            return y

        def draw_totals(self, draw, font, x, y, line_spacing, total_price, gst_amount, grand_total):
            # Draw separator line
            #draw.text((x, y), "-" * 70, fill="black", font=font)
            #y += line_spacing

            # Draw each total line with proper alignment
            label_width = 555

            draw.text((x, y), f"{'Total Price':<{label_width}}", fill="black", font=font)
            draw.text((x + label_width, y), f"{self.convert_to_inr(total_price)}", fill="black", font=font)
            y += line_spacing

            draw.text((x, y), f"{'GST ({self.gst_percentage}%):':<{label_width}}", fill="black", font=font)
            draw.text((x + label_width, y), f"{self.convert_to_inr(gst_amount)}", fill="black", font=font)
            y += line_spacing

            draw.text((x, y), f"{'Grand Total':<{label_width}}", fill="black", font=font)
            draw.text((x + label_width, y), f"{self.convert_to_inr(grand_total)}", fill="black", font=font)
            y += line_spacing

            return y

        def print_invoice(self, client_name, client_contact, event_type, total_price, gst_amount, grand_total,
                          selected_services):
            # Load an existing image
            image_path = "C:\\Users\\cheve\\PycharmProjects\\Python Project\\Invoice.jpg"
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            font_size = 20  # Adjust as needed
            font = ImageFont.truetype("arialbd.ttf", font_size)

            # Define the position and spacing for client details
            x_left_column = 166
            x_right_column = 300
            y_client_details = 434
            line_spacing_client = 50  # Increase line spacing for more distance between lines

            # Draw client details
            y = self.draw_client_details(draw, font, x_left_column, x_right_column, y_client_details,
                                         line_spacing_client, client_name, client_contact, event_type)

            # Draw services section at the specified position
            x_services_section = 246
            y_services_section = 670
            line_spacing_services = 50  # Define line spacing for services section

            y_services_section = self.draw_services_section(draw, font, x_services_section, y_services_section,
                                                            line_spacing_services, selected_services)

            # Draw totals section at the specified position
            x_totals = 246
            y_totals = 1387  # Set to the specified position
            line_spacing_totals = 30  # Define line spacing for totals section

            y_totals = self.draw_totals(draw, font, x_totals, y_totals, line_spacing_totals, total_price, gst_amount,
                                        grand_total)

            # Save the image with invoice details
            output_path = "C:\\Users\\cheve\\PycharmProjects\\Python Project\\Invoice_print.jpg"
            image.save(output_path)
            image.show()
            #messagebox.showinfo("Success", f"Invoice printed to {output_path}")

    @staticmethod
    def convert_to_inr(value):
        return f"₹{value:,.2f}"
    def past_records(self):
        # Create a new window for past records
        past_records_window = tk.Toplevel(self.root)
        past_records_window.title("Past Records")
        past_records_window.state("zoomed")

        try:
            # Fetch records from invoice_services and invoices tables
            cursor = mydb.cursor()

            cursor.execute("""
                SELECT i.id, i.client_name, i.event_type, i.invoice_date, i.total_price,
                       GROUP_CONCAT(CONCAT(iv.service_name, ' (', iv.quantity, ')') SEPARATOR ', ') AS selected_services
                FROM invoices i
                INNER JOIN invoice_services iv ON i.id = iv.invoice_id
                GROUP BY i.id
            """)
            records = cursor.fetchall()

            # Create a Treeview widget for displaying records
            tree = ttk.Treeview(past_records_window)
            tree["columns"] = ("#1", "#2", "#3", "#4", "#5")
            tree.heading("#0", text="ID")
            tree.heading("#1", text="Client Name")
            tree.heading("#2", text="Event Type")
            tree.heading("#3", text="Invoice Date")
            tree.heading("#4", text="Total Price")
            tree.heading("#5", text="Selected Services")

            # Calculate column widths based on content
            tree.column("#0", width=50, minwidth=50)

            # Calculate widths for columns dynamically
            max_widths = [100, 150, 150, 100, 300]  # Adjust initial minimum widths

            for record in records:
                for i in range(1, 6):  # Adjust range based on number of columns
                    text = str(record[i])
                    width = len(text) * 10  # Adjust multiplier based on font and content
                    if width > max_widths[i - 1]:
                        max_widths[i - 1] = width

            tree.column("#1", width=max_widths[0], anchor="w")
            tree.column("#2", width=max_widths[1], anchor="w")
            tree.column("#3", width=max_widths[2], anchor="w")
            tree.column("#4", width=max_widths[3], anchor="w")
            tree.column("#5", width=max_widths[4], anchor="w")

            # Insert records into the Treeview
            for record in records:
                tree.insert("", tk.END, text=record[0],
                            values=(record[1], record[2], record[3], self.convert_to_inr(record[4]), record[5]))

            tree.pack(expand=True, fill="both")

            cursor.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def calculate_column_width(self, records, column_index):
        max_width = 100  # Set a minimum width
        for record in records:
            text = str(record[column_index])
            width = len(text) * 10  # Adjust multiplier based on font and content
            if width > max_width:
                max_width = width
        return max_width

    def clear_selection(self):
        self.client_name.set("")
        self.client_contact.set("")
        self.event_type.set("")
        self.update_services(None)
        self.sample_invoice_text.delete(1.0, tk.END)

        # Clear all quantity entries in self.orders
        for service, details in self.orders.items():
            details['quantity_entry'].delete(0, tk.END)
            details['total_label'].config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
