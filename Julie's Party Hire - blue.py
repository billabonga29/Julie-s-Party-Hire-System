import tkinter as tk
from tkinter import ttk
import random
import os
import PIL 
from PIL import Image, ImageTk

# Creates a text file to store the data.
def write_hire_details(customer_name, receipt_number, item_hired, amount_hired):
    with open("hire_details.txt", "a") as file:
        file.write(f"{customer_name},{receipt_number},{item_hired},{amount_hired}\n")

def hire_window():
    # Sets up the window for hire.
    global hire_root
    hire_root = tk.Toplevel(root)
    hire_root.title("Hire")
    hire_root.configure(bg="#B0C4DE")

    # Creates all the hire-related labels and widgets and places them in correct grid placement.
    hire_label = tk.Label(hire_root, text="Hire", font=("Vivaldi", 24), bg="#B0C4DE")
    hire_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    
    customer_name_label = tk.Label(hire_root, text="Customer Name:", bg="#4682B4", font=("Comic Sans MS", 12))
    customer_name_label.grid(row=1, column=0, padx=10, pady=10)
    customer_name_entry = tk.Entry(hire_root, width=20, bg="white", font=("Comic Sans MS", 12))
    customer_name_entry.grid(row=1, column=1, padx=10, pady=10)

    receipt_number_label = tk.Label(hire_root, text="Receipt Number:", bg="#4682B4", font=("Comic Sans MS", 12))
    receipt_number_label.grid(row=2, column=0, padx=10, pady=10)
    receipt_number = random.randint(1000, 9999)
    receipt_number_display = tk.Label(hire_root, text=receipt_number, bg="white", font=("Comic Sans MS", 12))
    receipt_number_display.grid(row=2, column=1, padx=10, pady=10)

    item_hired_label = tk.Label(hire_root, text="Item Hired:", bg="#4682B4", font=("Comic Sans MS", 12))
    item_hired_label.grid(row=3, column=0, padx=10, pady=10)
    item_hired_combo = ttk.Combobox(hire_root, values=["Chairs", "Tables", "Decorations", "Sound System", "Lighting"], width=20, font=("Comic Sans MS", 12))
    item_hired_combo.grid(row=3, column=1, padx=10, pady=10)
    
    amount_hired_label = tk.Label(hire_root, text="Amount Hired:", bg="#4682B4", font=("Comic Sans MS", 12))
    amount_hired_label.grid(row=4, column=0, padx=10, pady=10)
    amount_hired_entry = tk.Entry(hire_root, width=10, bg="white", font=("Comic Sans MS", 12))
    amount_hired_entry.grid(row=4, column=1, padx=10, pady=10)

    output_text = tk.Text(hire_root, wrap=tk.WORD, height=5, width=30, bg="white", font=("Comic Sans MS", 10))
    output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Creates a submit button for the hire window.
    def submit_hire():
        # Gets the inputted data.
        customer_name = customer_name_entry.get()
        item_hired = item_hired_combo.get()
        amount_hired = amount_hired_entry.get()

        # Sends an error message if the user leaves the fields blank.
        if not customer_name or not item_hired or not amount_hired:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "ERROR! Please fill in all the fields.\n")
            return

        # Adds the inputted details into the text file.
        write_hire_details(customer_name, receipt_number, item_hired, amount_hired)

        # Prints the hire details into the output box.
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Customer Name: {customer_name}\n")
        output_text.insert(tk.END, f"Receipt Number: {receipt_number}\n")
        output_text.insert(tk.END, f"Item Hired: {item_hired}\n")
        output_text.insert(tk.END, f"Amount Hired: {amount_hired}\n")
        output_text.insert(tk.END, "-" * 20)

        # Clears the user's entries from the GUI.
        customer_name_entry.delete(0, tk.END)
        item_hired_combo.set("")
        amount_hired_entry.delete(0, tk.END)
        
    # Creates submit button and places it in it's correct grid location.
    submit_button = tk.Button(hire_root, text="Submit", command=submit_hire, bg="#4682B4", font=("Comic Sans MS", 12))
    submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Creates a back button that goes back to the main menu window.
    def back_to_main():
        # Closes the hire page window.
        hire_root.destroy()

    # Creates the back button in the GUI and places it in the correct grid placement.
    back_button = tk.Button(hire_root, text="Back", command=back_to_main, bg="#4682B4", font=("Comic Sans MS", 12))
    back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Gets the hire details from the text file.
def get_hire_details(receipt_number):
    if os.path.exists("hire_details.txt"):
        with open("hire_details.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                stored_customer_name, stored_receipt_number, stored_item_hired, stored_amount_hired = line.strip().split(",")
                if stored_receipt_number == receipt_number:
                    return stored_customer_name, stored_item_hired, stored_amount_hired
    return None

def return_window(receipt_number, hire_details):
    # Sets up the return window.
    global return_root
    return_root = tk.Toplevel(root)
    return_root.title("Return")
    return_root.configure(bg="#B0C4DE")
    
    # Turns the stored data from text file into the variable 'hire_details'.
    stored_customer_name, stored_item_hired, stored_amount_hired = hire_details

    # Creates the labels and widgets related to return and places them in the correct grid location.
    return_label = tk.Label(return_root, text="Hire", font=("Vivaldi", 24), bg="#B0C4DE")
    return_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    
    customer_name_label = tk.Label(return_root, text="Customer Name:", bg="#4682B4", font=("Comic Sans MS", 12))
    customer_name_label.grid(row=1, column=0, padx=10, pady=10)
    customer_name_entry = tk.Entry(return_root, width=20, font=("Comic Sans MS", 12))
    customer_name_entry.insert(0, stored_customer_name)
    customer_name_entry.config(state="disabled")
    customer_name_entry.grid(row=1, column=1, padx=10, pady=10)

    receipt_number_label = tk.Label(return_root, text="Receipt Number:", bg="#4682B4", font=("Comic Sans MS", 12))
    receipt_number_label.grid(row=2, column=0, padx=10, pady=10)
    receipt_number_entry = tk.Entry(return_root, width=10, font=("Comic Sans MS", 12))
    receipt_number_entry.insert(0, receipt_number)
    receipt_number_entry.config(state="disabled")
    receipt_number_entry.grid(row=2, column=1, padx=10, pady=10)

    item_returned_label = tk.Label(return_root, text="Item Hired:", bg="#4682B4", font=("Comic Sans MS", 12))
    item_returned_label.grid(row=3, column=0, padx=10, pady=10)
    item_returned_entry = tk.Entry(return_root, width=20, font=("Comic Sans MS", 12))
    item_returned_entry.insert(0, stored_item_hired)
    item_returned_entry.config(state="disabled")
    item_returned_entry.grid(row=3, column=1, padx=10, pady=10)

    amount_hired_label = tk.Label(return_root, text="Amount Hired:", bg="#4682B4", font=("Comic Sans MS", 12))
    amount_hired_label.grid(row=4, column=0, padx=10, pady=10)
    amount_hired_entry = tk.Entry(return_root, width=10, font=("Comic Sans MS", 12))
    amount_hired_entry.insert(0, stored_amount_hired)
    amount_hired_entry.config(state="disabled")
    amount_hired_entry.grid(row=5, column=1, padx=10, pady=10)

    amount_returned_label = tk.Label(return_root, text="Amount Returned:", bg="#4682B4", font=("Comic Sans MS", 12))
    amount_returned_label.grid(row=5, column=0, padx=10, pady=10)
    amount_returned_entry = tk.Entry(return_root, width=10, font=("Comic Sans MS", 12))
    amount_returned_entry.grid(row=5, column=1, padx=10, pady=10)

    output_text = tk.Text(return_root, wrap=tk.WORD, height=10, width=50, bg="white", font=("Comic Sans MS", 10))
    output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Prints the old hire details in the output box.
    output_text.insert(tk.END, f"Hire Details:\nCustomer Name: {stored_customer_name}\nReceipt Number: {receipt_number}\nItem Hired: {stored_item_hired}\nAmount Hired: {stored_amount_hired}\n")
    output_text.insert(tk.END, "-" * 20 + "\n")

    def submit_return():
        # Gets data for how much of the item the customer is returning.
        amount_returned = amount_returned_entry.get()

        # Checks if the user has returned a valid amount and prints error message if they don't.
        if not amount_returned or int(amount_returned) > int(stored_amount_hired) or int(amount_returned) <= 0:
            output_text.insert(tk.END, "Error! The amount you have returned is invalid. Please enter a valid amount.\n")
            return

        # Prints the updated hire details in box
        output_text.insert(tk.END, f"Updated Hire Amount:\nAmount Returned: {amount_returned}\n")
        output_text.insert(tk.END, "-" * 20 + "\n")

        # Clears the user's entries.
        amount_returned_entry.delete(0, tk.END)

        # Prints new receipt
        new_amount_hired = int(stored_amount_hired) - int(amount_returned)
        output_text.insert(tk.END, f"New Hire Details:\nCustomer Name: {stored_customer_name}\nReceipt Number: {receipt_number}\nItem Hired: {stored_item_hired}\nAmount Remaining: {new_amount_hired}\n")
        output_text.insert(tk.END, "=" * 20 + "\n")

    submit_button = tk.Button(return_root, text="Submit", command=submit_return, bg="#4682B4", font=("Comic Sans MS", 12))
    submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Creates a back button
    def back_to_main():
        return_root.destroy()

    # Creates button and places it in correct grid location.
    back_button = tk.Button(return_root, text="Back", command=back_to_main, bg="#4682B4", font=("Comic Sans MS", 12))
    back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Creates a pop-up window to find the correct customer that is returning.
def open_return_window():
    # Checks if the receipt number exists.
    def on_validate():
        receipt_number = receipt_number_entry.get()
        hire_details = get_hire_details(receipt_number)
        if hire_details:
            enter_receipt_root.destroy()
            return_window(receipt_number, hire_details)
        else:
            error_label.config(text="Invalid receipt number. Please try again.", bg="#4682B4")

    # Sets up the pop-up window.
    enter_receipt_root = tk.Toplevel(root)
    enter_receipt_root.title("Enter Receipt Number")
    enter_receipt_root.configure(bg="#B0C4DE")

    # Creates the labels and buttons and places them in the correct grid placement.
    receipt_number_label = tk.Label(enter_receipt_root, text="Receipt Number:", bg="#4682B4", font=("Comic Sans MS", 12))
    receipt_number_label.grid(row=0, column=0, padx=10, pady=10)
    global receipt_number_entry
    receipt_number_entry = tk.Entry(enter_receipt_root, width=15, font=("Comic Sans MS", 12))
    receipt_number_entry.grid(row=0, column=1, padx=10, pady=10)

    validate_button = tk.Button(enter_receipt_root, text="Validate", command=on_validate, bg="#4682B4", font=("Comic Sans MS", 12))
    validate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    error_label = tk.Label(enter_receipt_root, text="", bg="#B0C4DE", font=("Comic Sans MS", 12), fg="black")
    error_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Updates the hire details in the text file
def update_hire_details(receipt_number, new_amount_hired):
    lines = []
    with open("hire_details.txt", "r") as file:
        lines = file.readlines()

    with open("hire_details.txt", "w") as file:
        for line in lines:
            stored_customer_name, stored_receipt_number, stored_item_hired, stored_amount_hired = line.strip().split(",")
            if stored_receipt_number == receipt_number:
                if new_amount_hired > 0:
                    file.write(f"{stored_customer_name},{stored_receipt_number},{stored_item_hired},{new_amount_hired}\n")
            else:
                file.write(line)

def history():
    # Sets up history window.
    history_root = tk.Toplevel(root)
    history_root.title("Hire History")
    history_root.configure(bg="#B0C4DE")

    header_label = tk.Label(history_root, text="Hire History", font=("Vivaldi", 20), bg="#B0C4DE")
    header_label.pack(pady=10)

    # Treeview widget to show the history of receipts of things people have hired.
    tree = ttk.Treeview(history_root, columns=("Customer Name", "Receipt Number", "Item Hired", "Amount Hired"), show="headings")
    style = ttk.Style()
    style.configure("Treeview", background="#B0C4DE",
                    foreground="black", fieldbackground="#B0C4DE")
    style.configure("Treeview.Heading", background="#4682B4",  
                    foreground="black")
    tree.heading("Customer Name", text="Customer Name")
    tree.heading("Receipt Number", text="Receipt Number")
    tree.heading("Item Hired", text="Item Hired")
    tree.heading("Amount Hired", text="Amount Hired")
    tree.pack(fill=tk.BOTH, expand=True)

    # Brings the data from the text file to treeview
    if os.path.exists("hire_details.txt"):
        with open("hire_details.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                customer_name, receipt_number, item_hired, amount_hired = line.strip().split(",")
                tree.insert("", "end", values=(customer_name, receipt_number, item_hired, amount_hired))

    def back_to_main():
        history_root.destroy()

    back_button = tk.Button(history_root, text="Back", command=back_to_main, bg="#4682B4", font=("Comic Sans MS", 12))
    back_button.pack(pady=10)

def main():
    # Sets up the main window.
    global root
    root = tk.Tk()
    root.title("Julie's Party Hire")
    root.configure(bg="#B0C4DE")

    # Creates all the labels and buttons and places them in the correct grid placement.
    logo = [ImageTk.PhotoImage(Image.open("logo_blue.png").resize((250,120)))]
    main_menu_label = tk.Label(root, image=logo, bg="#B0C4DE")
    main_menu_label.grid(row=1, column=0, columnspan=2, padx=30, pady=20)

    hire_button = tk.Button(root, text="Hire", command=hire_window, width=10, bg="#4682B4", font=("Comic Sans MS", 12))
    hire_button.grid(row=2, column=0, pady=10)

    return_button = tk.Button(root, text="Return", command=open_return_window, width=10, bg="#4682B4", font=("Comic Sans MS", 12))
    return_button.grid(row=2, column=1, pady=10)

    history_button = tk.Button(root, text="History", command=history, width=10, bg="#4682B4", font=("Comic Sans MS",12))
    history_button.grid(row=3, column=0, pady=10)

    quit_button = tk.Button(root, text="Quit", command=root.quit, width=10, bg="#4682B4", font=("Comic Sans MS", 12))
    quit_button.grid(row=3, column=1, pady=20)

    root.mainloop()
main()
