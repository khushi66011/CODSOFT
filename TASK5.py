# -----------------------
# Task5: Contact Book
# -----------------------
# Made by: [khushi bhawsar]
#Requirmnet---- 
# Store contact information: name, phone number, email, and address
# Add new contacts
# View saved contacts
# Search contacts by name or phone
# Update contact details
# Delete contact

import re  
from pickle import dump, load  
from os import system, name  

#clears the screen 

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

# check if phone number is exactly 10 digits

def is_valid_phone(phone):
    return re.fullmatch(r'\d{10}', phone) is not None

# check if email is valid
def is_valid_email(email):
    return re.fullmatch(r"^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

#class stores one contact's details
class Contact:
    def __init__(self, name="", phone="", email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return (
f"""---------------------------------------
Name    : {self.name}
Phone   : {self.phone}
Email   : {self.email}
Address : {self.address}
---------------------------------------"""
        )

#------- contact book logic--------

class ContactBook:
    def __init__(self):
        self.contacts = []  
        self.load_file()    # Load saved file if exist

    # saves the contact list to a file
    def save_file(self):
        with open("contacts.pkl", "wb") as f:
            dump(self.contacts, f)

    # loads the contact list from the file
    def load_file(self):
        try:
            with open("contacts.pkl", "rb") as f:
                self.contacts = load(f)
        except FileNotFoundError:
            self.contacts = []

    # adds a new contact
    def add_contact(self):
        print("\n--- Add Contact ---")
        name = input("Enter Full Name  : ").strip()
        phone = input("Enter Phone No   : ").strip()
        email = input("Enter Email      : ").strip()
        address = input("Enter Address    : ").strip()

        # check phone number is valid
        if not is_valid_phone(phone):
            print("Invalid phone number! It must be exactly 10 digits.\n")
            return

        # check email is valid
        if not is_valid_email(email):
            print("Invalid email format! Example: user@example.com\n")
            return

        # Check for duplicate phone number
        for c in self.contacts:
            if c.phone == phone:
                print("Contact with this phone number already exists.\n")
                return

        # Add the contact
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.\n")

    #displays all saved contacts
    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts available.\n")
            return
        for contact in self.contacts:
            print(f"{contact.name} - {contact.phone}")
        print()

    # search contact by name or phone
    def search_contact(self):
        print("\n--- Search Contact ---")
        query = input("Enter Name or Phone Number: ").lower().strip()
        found = False
        for contact in self.contacts:
            if query in contact.name.lower() or query == contact.phone:
                print(contact)
                found = True
        if not found:
            print("Contact not found.\n")

    # update a contact's details
    def update_contact(self):
        print("\n--- Update Contact ---")
        phone = input("Enter Phone Number to Update: ").strip()
        for i, contact in enumerate(self.contacts):
            if contact.phone == phone:
                print("Leave blank if you don’t want to change a value.")
                new_name = input(f"New Name    [{contact.name}] : ") or contact.name
                new_email = input(f"New Email   [{contact.email}] : ") or contact.email
                new_address = input(f"New Address [{contact.address}] : ") or contact.address

                # check updated email is valid
                if not is_valid_email(new_email):
                    print("Invalid email format! Update cancelled.\n")
                    return

                # Save updated contact
                updated = Contact(
                    name=new_name,
                    phone=contact.phone,
                    email=new_email,
                    address=new_address
                )
                self.contacts[i] = updated
                print("Contact updated successfully.\n")
                return
        print("Phone number not found.\n")

    #deletes a contact based on phone number
    def delete_contact(self):
        print("\n--- Delete Contact ---")
        phone = input("Enter Phone Number to Delete: ").strip()
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.\n")
                return
        print("Contact not found.\n")


    def home_page(self):
        while True:
            print("======== Contact Book ==========")
            print("      1. Add Contact")
            print("      2. View Contact List")
            print("      3. Search Contact")
            print("      4. Update Contact")
            print("      5. Delete Contact")
            print("      6. Exit")
            try:
                choice = int(input("Enter your choice (1-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            clear_screen()

            if choice == 1:
                self.add_contact()
                self.save_file()
            elif choice == 2:
                self.view_contacts()
            elif choice == 3:
                self.search_contact()
            elif choice == 4:
                self.update_contact()
                self.save_file()
            elif choice == 5:
                self.delete_contact()
                self.save_file()
            elif choice == 6:
                print("Exiting... Goodbye!\n")
                break
            else:
                print("Invalid option. Try again.\n")


# run the program
if __name__ == "__main__":
    app = ContactBook()
    app.home_page()
