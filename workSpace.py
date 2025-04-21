import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from ttkthemes import ThemedTk

# Configuration
ROOM_PRICES = {
    "Standard": 15.00,
    "Premium": 25.00,
    "VIP": 40.00,
    "Private": 50.00
}

ITEM_PRICES = {
    "Coffee": 25.00,
    "Tea": 10.00,
    "Water": 10.00,
    "Snacks": 2.00
}

active_customers = {}

def show_customer_details(event):
    selected = customer_tree.selection()
    if not selected:
        return

    name = customer_tree.item(selected, 'values')[0]
    session = active_customers[name]

    details_window = tk.Toplevel(root)
    details_window.title(f"Session: {name}")
    details_window.geometry("500x500")
    details_window.configure(background=root.cget('background'))
    
    # Session info frame
    info_frame = ttk.LabelFrame(details_window, text="Session Details", padding=10)
    info_frame.pack(fill=tk.X, padx=10, pady=10)
    
    ttk.Label(info_frame, text=f"Check-in Time: {session['start_time'].strftime('%H:%M:%S')}",
             font=('Segoe UI', 10)).grid(row=0, column=0, sticky='w', padx=5)
    
    duration_label = ttk.Label(info_frame, text="Calculating...", font=('Segoe UI', 10))
    duration_label.grid(row=1, column=0, sticky='w', padx=5)

    # Purchases section
    purchases_frame = ttk.LabelFrame(details_window, text="Purchases", padding=10)
    purchases_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tree = ttk.Treeview(purchases_frame, columns=("item", "price"), show="headings")
    tree.heading("item", text="Item")
    tree.heading("price", text="Price (EGP)")
    tree.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # Edit functionality
    edit_frame = ttk.Frame(purchases_frame)
    edit_frame.pack(fill=tk.X, pady=5)
    
    def delete_item():
        selected_item = tree.selection()
        if not selected_item:
            return
        item = tree.item(selected_item, 'values')[0]
        session['items'] = [i for i in session['items'] if i[0] != item]
        update_details()
    
    ttk.Button(edit_frame, text="Remove Selected", command=delete_item).pack(side=tk.LEFT)
    
    # Total charges
    total_label = ttk.Label(details_window, text="Total: 0.00 EGP", 
                          font=('Segoe UI', 12, 'bold'))
    total_label.pack(pady=10)

    def update_details():
        # Update duration
        duration = (datetime.now() - session['start_time']).total_seconds()
        hours, rem = divmod(duration, 3600)
        mins = rem // 60
        duration_label.config(text=f"Duration: {int(hours)}h {int(mins)}m")
        
        # Update purchases
        tree.delete(*tree.get_children())
        for item, price in session['items']:
            tree.insert("", tk.END, values=(item, f"{price:.2f} EGP"))
        
        # Calculate total
        workspace_charge = (duration/3600) * session['room_price']
        items_charge = sum(price for _, price in session['items'])
        total = workspace_charge + items_charge
        
        total_label.config(text=f"Total: {total:.2f} EGP")
        
        details_window.after(1000, update_details)

    update_details()
    ttk.Button(details_window, text="Close", 
              command=details_window.destroy).pack(pady=5)

def add_customer():
    name = entry_name.get().strip()
    room = room_var.get()
    
    if not name:
        messagebox.showwarning("Error", "Please enter customer name")
        return
    if not room or room not in ROOM_PRICES:
        messagebox.showwarning("Error", "Please select valid room type")
        return

    if name in active_customers:
        messagebox.showwarning("Error", f"{name} already checked in")
        return

    active_customers[name] = {
        "start_time": datetime.now(),
        "room_type": room,
        "room_price": ROOM_PRICES[room],
        "items": []
    }
    
    success_lbl = ttk.Label(frame_left, text=f"✓ {name} ({room}) Checked In!", 
                           foreground="#4CAF50", font=('Segoe UI', 10))
    success_lbl.pack(pady=(5, 0))
    success_lbl.after(2000, success_lbl.destroy)
    
    update_customer_tree()

def update_customer_tree():
    customer_tree.delete(*customer_tree.get_children())
    for name, data in active_customers.items():
        duration = (datetime.now() - data['start_time']).total_seconds()
        hours = duration / 3600
        workspace_charge = hours * data['room_price']
        items_charge = sum(price for _, price in data['items'])
        total = workspace_charge + items_charge
        customer_tree.insert("", tk.END, values=(name, data['room_type'], f"{total:.2f} EGP"))

def add_item():
    selected = customer_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select customer first")
        return

    name = customer_tree.item(selected, 'values')[0]
    item = item_var.get()

    if item not in ITEM_PRICES:
        messagebox.showwarning("Error", "Invalid item selection")
        return

    active_customers[name]["items"].append((item, ITEM_PRICES[item]))
    update_customer_tree()
    messagebox.showinfo("Success", f"Added {item} to {name}")

def checkout_customer():
    selected = customer_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select customer first")
        return

    name = customer_tree.item(selected, 'values')[0]
    session = active_customers.pop(name)
    
    duration = (datetime.now() - session['start_time']).total_seconds()
    hours = duration / 3600
    mins = (duration % 3600) // 60
    
    workspace_charge = hours * session['room_price']
    items_list = "\n".join([f"- {item}: {price:.2f} EGP" for item, price in session['items']])
    items_charge = sum(price for _, price in session['items'])
    total = workspace_charge + items_charge
    
    bill = (
        f"Customer: {name}\n"
        f"Room Type: {session['room_type']} ({session['room_price']:.2f} EGP/h)\n"
        f"Check-in Time: {session['start_time'].strftime('%H:%M:%S')}\n"
        f"Duration: {int(hours)}h {int(mins)}m\n"
        f"Workspace Charge: {workspace_charge:.2f} EGP\n"
        f"Purchases:\n{items_list}\n"
        f"Total: {total:.2f} EGP"
    )
    
    messagebox.showinfo("Checkout Complete", bill)
    update_customer_tree()

# Main application setup
root = ThemedTk(theme="clearlooks")
root.title("co-workingSpace")
root.geometry("1200x600")
root.iconbitmap("path\\letter-m.ico")
style = ttk.Style()
style.configure("Treeview", rowheight=30)
style.configure("Treeview.Heading", font=('Segoe UI', 10, 'bold'))

# Main layout
content = ttk.Frame(root)
content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(0, weight=1)
content.grid_columnconfigure(1, weight=2)

# Left panel - Customer Management
frame_left = ttk.LabelFrame(content, text="Customer Management", padding=15)
frame_left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

# Customer name entry
ttk.Label(frame_left, text="Customer Name:", font=('Segoe UI', 10)).pack(pady=(10, 0))
entry_name = ttk.Entry(frame_left, font=('Segoe UI', 10))
entry_name.pack(fill=tk.X, pady=10)

# Room selection
ttk.Label(frame_left, text="Room Type:", font=('Segoe UI', 10)).pack(pady=(5, 0))
room_var = tk.StringVar()
room_menu = ttk.Combobox(frame_left, textvariable=room_var, state="readonly")
room_menu['values'] = list(ROOM_PRICES.keys())
room_menu.current(0)
room_menu.pack(fill=tk.X, pady=5)

ttk.Button(frame_left, text="Check In", command=add_customer).pack(pady=(10, 0))

# Customer list with room type
customer_tree = ttk.Treeview(frame_left, 
                            columns=("name", "room", "total"),
                            show="headings")
customer_tree.heading("name", text="Name")
customer_tree.heading("room", text="Room Type")
customer_tree.heading("total", text="Total Charge")
customer_tree.column("name", width=200)
customer_tree.column("room", width=150)
customer_tree.column("total", width=100)
customer_tree.pack(fill=tk.BOTH, expand=True, pady=10)
customer_tree.bind('<Double-1>', show_customer_details)

# Right panel - Actions
frame_right = ttk.LabelFrame(content, text="Actions", padding=15)
frame_right.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

item_var = tk.StringVar()
item_menu = ttk.Combobox(frame_right, textvariable=item_var, state="readonly")
item_menu['values'] = list(ITEM_PRICES.keys())
item_menu.current(0)
item_menu.pack(fill=tk.X, pady=10)

ttk.Button(frame_right, text="Add Item", command=add_item).pack(pady=5)
ttk.Button(frame_right, text="Checkout", command=checkout_customer).pack(pady=5)

update_customer_tree()
root.mainloop()
