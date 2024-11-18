import json
import os
import tkinter as tk
from tkinter import messagebox

ORDER_DATA_FILE = "orders.json"

def load_orders():
    if os.path.exists(ORDER_DATA_FILE):
        with open(ORDER_DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Save order data to JSON file
def save_orders(orders):
    with open(ORDER_DATA_FILE, "w") as file:
        json.dump(orders, file, indent=4)


# Add a new order
def add_order():
    name = entry_name.get()
    order_id = entry_id.get()

    if not name or not order_id :
        messagebox.showwarning("Input Error", "Please enter  name, ID and price.")
        return

    try:
       order_id = int(order_id)

    except ValueError:
        messagebox.showwarning("Input Error", "ID must be a number.")
        return

    orders = load_orders()
    if any(order['name'] == name and order['id'] == order_id for order in orders):
        messagebox.showinfo("Duplicate Entry", f"Order ({name}, {order_id}) already exists.")
    else:
        orders.append({"name": name, "id": order_id})
        save_orders(orders)
        entry_name.delete(0, tk.END)
        entry_id.delete(0, tk.END)
        messagebox.showinfo("Success", f"Order ({name}, {order_id}) added successfully.")
        view_order_list()


# Display list of orders
def view_order_list():
    orders = load_orders()
    listbox_orders.delete(0, tk.END)
    for order in orders:
        listbox_orders.insert(tk.END, f"{order['name']} (ID: {order['id']})")


# Search for an order
def search_order():
    name = entry_name.get()
    order_id = entry_id.get()

    if not name or not order_id:
        messagebox.showwarning("Input Error", "Please enter both name and ID to search.")
        return

    try:
        order_id = int(order_id)
    except ValueError:
        messagebox.showwarning("Input Error", "ID must be a number.")
        return

    orders = load_orders()
    found = next((order for order in orders if order['name'] == name and order['id'] == order_id), None)
    if found:
        messagebox.showinfo("Record Found", f"Order found: {found['name']} (ID: {found['id']})")
    else:
        messagebox.showinfo("No Record", f"No record found for order ({name}, {order_id}).")


# Remove an order
def remove_order():
    name = entry_name.get()
    order_id = entry_id.get()

    if not name or not order_id:
        messagebox.showwarning("Input Error", "Please enter both name and ID to remove.")
        return

    try:
        order_id = int(order_id)
    except ValueError:
        messagebox.showwarning("Input Error", "ID must be a number.")
        return

    orders = load_orders()
    new_orders = [order for order in orders if not (order['name'] == name and order['id'] == order_id)]
    if len(new_orders) < len(orders):
        save_orders(new_orders)
        messagebox.showinfo("Success", f"Order ({name}, {order_id}) removed successfully.")
        view_order_list()
    else:
        messagebox.showinfo("No Record", f"No record found for order ({name}, {order_id}).")


# Setup the GUI
root = tk.Tk()
root.title("Order Management System")
root.geometry("450x500")

# Labels and Entry Fields
label_name = tk.Label(root, text="Order Name")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_id = tk.Label(root, text="Order ID")
label_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()


# Buttons
button_add = tk.Button(root, width=16, text=" Add Item ", command=add_order)
button_add.pack()

button_view = tk.Button(root, width=16, text="View my Order", command=view_order_list)
button_view.pack()

button_search = tk.Button(root, width=16, text="Search Order", command=search_order)
button_search.pack()

button_remove = tk.Button(root, width=16, text="Remove my Order", command=remove_order)
button_remove.pack()

# Listbox to display orders
listbox_orders = tk.Listbox(root, width=100)
listbox_orders.pack()

# Display all list of order on start
view_order_list()

# Start the GUI loop
root.mainloop()