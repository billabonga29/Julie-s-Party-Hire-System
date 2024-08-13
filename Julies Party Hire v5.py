import tkinter as tk
from tkinter import ttk
import random
import os

# Creates a text file to store the data.
def write_hire_details(customer_name, receipt_number, item_hired, amount_hired):
    with open("hire_details.txt", "a") as file:
        file.write(f"{customer_name},{receipt_number},{item_hired},{amount_hired}\n")

def hire_window():
    # Sets up the window for hire.
    global hire_root
    hire_root = tk.Toplevel(root)
    hire_root.title("Hire")
    hire_root.configure(bg="#FFA500")

    # Creates all the hire-related labels and widgets and places them in correct grid placement.
    customer_name_label = tk.Label(hire_root, text="Customer Name:", bg="#FFA500", font=("Comic Sans MS", 12))
    customer_name_label.grid(row=0, column=0, padx=10, pady=10)
    customer_name_entry = tk.Entry(hire_root, width=20, font=("Comic Sans MS", 12))
    customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

    receipt_number_label = tk.Label(hire_root, text="Receipt Number:", bg="#FFA500", font=("Comic Sans MS", 12))
    receipt_number_label.grid(row=1, column=0, padx=10, pady=10)
    receipt_number = random.randint(1000, 9999)
    receipt_number_display = tk.Label(hire_root, text=receipt_number, bg="#FFA500", font=("Comic Sans MS", 12))
    receipt_number_display.grid(row=1, column=1, padx=10, pady=10)

    item_hired_label = tk.Label(hire_root, text="Item Hired:", bg="#FFA500", font=("Comic Sans MS", 12))
    item_hired_label.grid(row=2, column=0, padx=10, pady=10)
    item_hired_combo = ttk.Combobox(hire_root, values=["Chairs", "Tables", "Decorations", "Sound System", "Lighting"], width=20, font=("Comic Sans MS", 12))
    item_hired_combo.grid(row=2, column=1, padx=10, pady=10)

    amount_hired_label = tk.Label(hire_root, text="Amount Hired:", bg="#FFA500", font=("Comic Sans MS", 12))
    amount_hired_label.grid(row=3, column=0, padx=10, pady=10)
    amount_hired_entry = tk.Entry(hire_root, width=10, font=("Comic Sans MS", 12))
    amount_hired_entry.grid(row=3, column=1, padx=10, pady=10)

    output_text = tk.Text(hire_root, wrap=tk.WORD, height=5, width=30, bg="#FFFFE0", font=("Comic Sans MS", 10))
    output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

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
    submit_button = tk.Button(hire_root, text="Submit", command=submit_hire, bg="#FFA500", font=("Comic Sans MS", 12))
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Creates a back button that goes back to the main menu window.
    def back_to_main():
        # Closes the hire page window.
        hire_root.destroy()

    # Creates the back button in the GUI and places it in the correct grid placement.
    back_button = tk.Button(hire_root, text="Back", command=back_to_main, bg="#FFA500", font=("Comic Sans MS", 12))
    back_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

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
    return_root.configure(bg="#FFA500")
    
    # Turns the stored data from text file into the variable 'hire_details'.
    stored_customer_name, stored_item_hired, stored_amount_hired = hire_details

    # Creates the labels and widgets related to return and places them in the correct grid location.
    customer_name_label = tk.Label(return_root, text="Customer Name:", bg="#FFA500", font=("Comic Sans MS", 12))
    customer_name_label.grid(row=0, column=0, padx=10, pady=10)
    customer_name_entry = tk.Entry(return_root, width=20, font=("Comic Sans MS", 12))
    customer_name_entry.insert(0, stored_customer_name)
    customer_name_entry.config(state="disabled")
    customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

    receipt_number_label = tk.Label(return_root, text="Receipt Number:", bg="#FFA500", font=("Comic Sans MS", 12))
    receipt_number_label.grid(row=1, column=0, padx=10, pady=10)
    receipt_number_entry = tk.Entry(return_root, width=10, font=("Comic Sans MS", 12))
    receipt_number_entry.insert(0, receipt_number)
    receipt_number_entry.config(state="disabled")
    receipt_number_entry.grid(row=1, column=1, padx=10, pady=10)

    item_returned_label = tk.Label(return_root, text="Item Hired:", bg="#FFA500", font=("Comic Sans MS", 12))
    item_returned_label.grid(row=2, column=0, padx=10, pady=10)
    item_returned_entry = tk.Entry(return_root, width=20, font=("Comic Sans MS", 12))
    item_returned_entry.insert(0, stored_item_hired)
    item_returned_entry.config(state="disabled")
    item_returned_entry.grid(row=2, column=1, padx=10, pady=10)

    amount_hired_label = tk.Label(return_root, text="Amount Hired:", bg="#FFA500", font=("Comic Sans MS", 12))
    amount_hired_label.grid(row=3, column=0, padx=10, pady=10)
    amount_hired_entry = tk.Entry(return_root, width=10, font=("Comic Sans MS", 12))
    amount_hired_entry.insert(0, stored_amount_hired)
    amount_hired_entry.config(state="disabled")
    amount_hired_entry.grid(row=3, column=1, padx=10, pady=10)

    amount_returned_label = tk.Label(return_root, text="Amount Returned:", bg="#FFA500", font=("Comic Sans MS", 12))
    amount_returned_label.grid(row=4, column=0, padx=10, pady=10)
    amount_returned_entry = tk.Entry(return_root, width=10, font=("Comic Sans MS", 12))
    amount_returned_entry.grid(row=4, column=1, padx=10, pady=10)

    output_text = tk.Text(return_root, wrap=tk.WORD, height=10, width=50, bg="#FFFFE0", font=("Comic Sans MS", 10))
    output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

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

    submit_button = tk.Button(return_root, text="Submit", command=submit_return, bg="#FFA500", font=("Comic Sans MS", 12))
    submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Creates a back button
    def back_to_main():
        return_root.destroy()

    # Creates button and places it in correct grid location.
    back_button = tk.Button(return_root, text="Back", command=back_to_main, bg="#FFA500", font=("Comic Sans MS", 12))
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
            error_label.config(text="Invalid receipt number. Please try again.")

    # Sets up the pop-up window.
    enter_receipt_root = tk.Toplevel(root)
    enter_receipt_root.title("Enter Receipt Number")
    enter_receipt_root.configure(bg="#FFA500")

    # Creates the labels and buttons and places them in the correct grid placement.
    receipt_number_label = tk.Label(enter_receipt_root, text="Receipt Number:", bg="#FFA500", font=("Comic Sans MS", 12))
    receipt_number_label.grid(row=0, column=0, padx=10, pady=10)
    global receipt_number_entry
    receipt_number_entry = tk.Entry(enter_receipt_root, width=10, font=("Comic Sans MS", 12))
    receipt_number_entry.grid(row=0, column=1, padx=10, pady=10)

    validate_button = tk.Button(enter_receipt_root, text="Validate", command=on_validate, bg="#FFA500", font=("Comic Sans MS", 12))
    validate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    error_label = tk.Label(enter_receipt_root, text="", bg="#FFA500", font=("Comic Sans MS", 12), fg="red")
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

def main():
    # Sets up the main window.
    global root
    root = tk.Tk()
    root.title("Julie's Party Hire")
    root.configure(bg="#FFA500")

    # Creates all the labels and buttons and places them in the correct grid placement.
    main_menu_label = tk.Label(root, text="Julie's Party Hire", font=("Comic Sans MS", 24), bg="#FFA500")
    main_menu_label.pack(pady=20)

    hire_button = tk.Button(root, text="Hire", command=hire_window, width=10, bg="#FFA500", font=("Comic Sans MS", 12))
    hire_button.pack(pady=10)

    return_button = tk.Button(root, text="Return", command=open_return_window, width=10, bg="#FFA500", font=("Comic Sans MS", 12))
    return_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=root.quit, width=10, bg="#FFA500", font=("Comic Sans MS", 12))
    quit_button.pack(pady=10)

    root.mainloop()
main()
