import json
import os

class ContactBook:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def add_contact(self, contacts):
       name = input("Name:\n")
       phone = input("Phone number:\n")
       email = input("Email:\n")
       contacts.append(ContactBook(name,phone,email))
       print("Contact added!")

    def search_contact(self, contacts):
       name = input("Enter name to search: ")
       for i in contacts:
          if i.name == name:
             print(f"✅ Found: {i.name} | {i.phone} | {i.email}")
             return 
       print("this name is not exists in your contact list")
    
    def delete_contact(self, contacts):
       name = input("Enter name to delete: ")
       for i in contacts:
          if i.name == name:
             contacts.remove(i)
             print("contact deleted!")
             return
       print("⚠️ This name does not exist in your contact list.")

    def show_all_contacts(self):
        if not contacts:
            print("⚠️ No contacts to show.")
        for c in contacts:
            print(f"{c.name} | {c.phone} | {c.email}")
       
    def to_dict(self):
        return {
            "name" : self.name ,
            "phone": self.phone ,
            "email" : self.email
        }
    
    @classmethod
    def from_dict(clss, data):
        return clss(data["name"], data["phone"], data["email"])
    
# --------------------------saving methods--------------------------------

def save_contacts(contacts, filename="contacts.json"):
    data = [p.to_dict() for p in contacts]
    with open(filename, "w") as f:
       json.dump(data, f)

def load_contacts(filename="contacts.json"):
    if not os.path.exists(filename):
      return []
    with open(filename, "r") as f:
      data = json.load(f)
      return [ContactBook.from_dict(p) for p in data]

# ---------------------------main program------------------------------------

contacts = load_contacts()

while True:
   print("\n--- Contact Book ---")
   print("1. Add Contact")
   print("2. Search Contact")
   print("3. Delete Contact")
   print("4. Show All Contacts")
   print("5. Exit")

   try:
        choice = int(input("Choose an option (1-5): "))
   except ValueError:
        print("⚠️ Please enter a number.")
        continue
   
   if choice == 1:
        ContactBook("","","").add_contact(contacts)
   elif choice == 2:
        ContactBook("","","").search_contact(contacts)
   elif choice == 3:
       ContactBook("","","").delete_contact(contacts)
   elif choice == 4:
       ContactBook.show_all_contacts(contacts)
   elif choice == 5:
       save_contacts(contacts)
       print("Goodbye!")
       break
   else:
            print("Invalid choice!")
      
      