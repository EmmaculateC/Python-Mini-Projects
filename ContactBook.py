import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Management System")

        self.contacts = []
        self.create_widgets()

    def create_widgets(self):
        # Create style
        style = ttk.Style()
        style.configure("TFrame", background="#333")
        style.configure("TButton", background="#555", foreground="#000")
        style.configure("TLabel", background="#333", foreground="#fff")

        # Main frame
        main_frame = ttk.Frame(self.master, padding=(20, 10))
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels and Entry widgets
        ttk.Label(main_frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = ttk.Entry(main_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(main_frame, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry = ttk.Entry(main_frame)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(main_frame, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = ttk.Entry(main_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(main_frame, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry = ttk.Entry(main_frame)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        # Buttons
        ttk.Button(main_frame, text="Add Contact", command=self.add_contact, style="TButton").grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)
        ttk.Button(main_frame, text="View Contacts", command=self.view_contacts, style="TButton").grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)
        ttk.Button(main_frame, text="Search Contact", command=self.search_contact, style="TButton").grid(row=6, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)
        ttk.Button(main_frame, text="Update Contact", command=self.update_contact, style="TButton").grid(row=7, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)
        ttk.Button(main_frame, text="Delete Contact", command=self.delete_contact, style="TButton").grid(row=8, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)
       

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact list is empty.")
        else:
            contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
        if search_term:
            results = [f"{contact.name}: {contact.phone}" for contact in self.contacts
                       if search_term.lower() in contact.name.lower() or search_term in contact.phone]
            if results:
                messagebox.showinfo("Search Results", "\n".join(results))
            else:
                messagebox.showinfo("Search Results", "No contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name of contact to update:")
        if search_term:
            for contact in self.contacts:
                if contact.name.lower() == search_term.lower():
                    new_phone = simpledialog.askstring("Update Contact", "Enter new phone number:")
                    new_email = simpledialog.askstring("Update Contact", "Enter new email:")
                    new_address = simpledialog.askstring("Update Contact", "Enter new address:")
                    contact.phone = new_phone if new_phone else contact.phone
                    contact.email = new_email if new_email else contact.email
                    contact.address = new_address if new_address else contact.address
                    messagebox.showinfo("Success", f"Contact '{contact.name}' updated successfully!")
                    return
            messagebox.showinfo("Info", f"No contacts found with the name '{search_term}'.")
        else:
            messagebox.showwarning("Warning", "Please enter a name to update contact details.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name of contact to delete:")
        if search_term:
            for contact in self.contacts:
                if contact.name.lower() == search_term.lower():
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", f"Contact '{contact.name}' deleted successfully!")
                    return
            messagebox.showinfo("Info", f"No contacts found with the name '{search_term}'.")
        else:
            messagebox.showwarning("Warning", "Please enter a name to delete contact.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()   
    app = ContactManagerGUI(root)
    root.mainloop()

