import tkinter as tk
from tkinter import ttk
import random

def hire_window():
    global hire_root
    hire_root = tk.Toplevel(root)
    hire_root.title("Hire")

#Hire Labels and Entry
    #Name
    customer_name_label = tk.Label(hire_root, text="Customer Name:")
    customer_name_label.grid(row=0, column=0, padx=10, pady=10)
    customer_name_entry = tk.Entry(hire_root)
    customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

    #Receipt Number
    receipt_number_label = tk.Label(hire_root, text="Receipt Number:")
    receipt_number_label.grid(row=1, column=0, padx=10, pady=10)
    receipt_number = random.randint(1000, 9999)
    receipt_number_display = tk.Label(hire_root, text=receipt_number)
    receipt_number_display.grid(row=1, column=1, padx=10, pady=10)

    #Hired Item
    item_hired_label = tk.Label(hire_root, text="Item Hired:")
    item_hired_label.grid(row=2, column=0, padx=10, pady=10)
    item_hired_combo = ttk.Combobox(hire_root, values=["Chairs", "Tables", "Decorations", "Sound System", "Lighting"])
    item_hired_combo.grid(row=2, column=1, padx=10, pady=10)

    #Number of Item Hired
    amount_hired_label = tk.Label(hire_root, text="Amount Hired:")
    amount_hired_label.grid(row=3, column=0, padx=10, pady=10)
    amount_hired_entry = tk.Entry(hire_root)
    amount_hired_entry.grid(row=3, column=1, padx=10, pady=10)

#Submit Button
    def submit_hire():
        customer_name = customer_name_entry.get()
        item_hired = item_hired_combo.get()
        amount_hired = amount_hired_entry.get()
        
        #Prints hire details
        print(f"Customer Name: {customer_name}")
        print(f"Receipt Number: {receipt_number}")
        print(f"Item Hired: {item_hired}")
        print(f"Amount Hired: {amount_hired}")
        print("-" * 20)

        #Clear user entries
        customer_name_entry.delete(0, tk.END)
        item_hired_combo.set("")
        amount_hired_entry.delete(0, tk.END)

    submit_button = tk.Button(hire_root, text="Submit", command=submit_hire)
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#Back Button
    def back_to_main():
        hire_root.destroy()

    back_button = tk.Button(hire_root, text="Back", command=back_to_main)
    back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

def return_window():
    global return_root
    return_root = tk.Toplevel(root)
    return_root.title("Return")

#Return Labels and Entry
    #Customer Name
    customer_name_label = tk.Label(return_root, text="Customer Name:")
    customer_name_label.grid(row=0, column=0, padx=10, pady=10)
    customer_name_entry = tk.Entry(return_root)
    customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

    #Receipt Number
    receipt_number_label = tk.Label(return_root, text="Receipt Number:")
    receipt_number_label.grid(row=1, column=0, padx=10, pady=10)
    receipt_number_entry = tk.Entry(return_root)
    receipt_number_entry.grid(row=1, column=1, padx=10, pady=10)

    #Item Returned
    item_returned_label = tk.Label(return_root, text="Item Returned:")
    item_returned_label.grid(row=2, column=0, padx=10, pady=10)
    item_returned_entry = tk.Entry(return_root)
    item_returned_entry.grid(row=2, column=1, padx=10, pady=10)

    #Amount Returned
    amount_returned_label = tk.Label(return_root, text="Amount Returned:")
    amount_returned_label.grid(row=3, column=0, padx=10, pady=10)
    amount_returned_entry = tk.Entry(return_root)
    amount_returned_entry.grid(row=3, column=1, padx=10, pady=10)

# Submit Button
    def submit_return():
        customer_name = customer_name_entry.get()
        receipt_number = receipt_number_entry.get()
        item_returned = item_returned_entry.get()
        amount_returned = amount_returned_entry.get()

        #Prints customer details
        print(f"Customer Name: {customer_name}")
        print(f"Receipt Number: {receipt_number}")
        print(f"Item Returned: {item_returned}")
        print(f"Amount Returned: {amount_returned}")
        print("-" * 20)

        #Clear the entered entries
        customer_name_entry.delete(0, tk.END)
        receipt_number_entry.delete(0, tk.END)
        item_returned_entry.delete(0, tk.END)
        amount_returned_entry.delete(0, tk.END)

    submit_button = tk.Button(return_root, text="Submit", command=submit_return)
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    #Back Button
    def back_to_main():
        return_root.destroy()

    back_button = tk.Button(return_root, text="Back", command=back_to_main)
    back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#Main Window Setup and Label
root = tk.Tk()
root.title("Julie's Party Hire")

#Header
main_menu_label = tk.Label(root, text="Julie's Party Hire", font=("Arial", 24))
main_menu_label.pack(pady=20)

#Hire Button
hire_button = tk.Button(root, text="Hire", command=hire_window, width=10)
hire_button.pack(pady=10)

#Return Button
return_button = tk.Button(root, text="Return", command=return_window, width=10)
return_button.pack(pady=10)

#Quit Button
quit_button = tk.Button(root, text="Quit", command=root.quit, width=10)
quit_button.pack(pady=10)

root.mainloop()
