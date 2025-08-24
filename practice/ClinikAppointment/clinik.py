import json
import os
from datetime import datetime

# --------------------------------patient class--------------------------------

class Patient:
    def __init__(self, patient_id, name, dob, phone):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.phone = phone

    def to_dict(self):
        return {
            "patient_id" :  self.patient_id ,
            "name" : self.name ,
            "birthday_date" : self.dob ,
            "phone": self.phone    
        }
    
    @classmethod
    def from_dict(clss, data):
        return clss(data["patient_id"],data["name"],data["birthday_date"],data["phone"])
    

# --------------------------------appointment class--------------------------------

class Clinik:
    def __init__(self, patient_id, date, time, status= "scheduled"):
        self.patient_id = patient_id
        self.date = date
        self.time = time
        self.status = status

    def to_dict(self):
        return {
            "patient_id" :  self.patient_id ,
            "date" : self.date ,
            "time" : self.time ,
            "status": self.status   
        }
    
    @classmethod
    def from_dict(clss, data):
        return clss(data["patient_id"],data["date"],data["time"],data["status"])
    
# --------------------------------save and load data--------------------------------
def save_data(patients, appointments, filename="clinik.json"):
    data = {
        "patients": [p.to_dict() for p in patients],
        "appointments": [a.to_dict() for a in appointments]
    }
    with open(filename, "w") as f:
       json.dump(data, f)

def load_data(filename="clinik.json"):
    if not os.path.exists(filename):
      return [] , []
    with open(filename, "r") as f:
      data = json.load(f)
      patients = [Patient.from_dict(p) for p in data.get("patients", [])]
      appointments = [Clinik.from_dict(a) for a in data.get("appointments", [])]
      return patients, appointments
    
# ---------------------------------------main program -----------------------------

patients, appointments = load_data()

while True:
    print("\n--- Clinic Appointment System ---")
    print("1. Register Patient")
    print("2. Add Appointment")
    print("3. View All Appointments")
    print("4. Search Appointments")
    print("5. Change Appointment Status")
    print("6. Delete Appointment")
    print("7. Daily Report")
    print("8. Exit")

    try:
        choice = int(input("Choose an option (1-8): "))
    except ValueError:
        print("⚠️ Please enter a number.")
        continue

    if choice == 1:
        pid = input("Enter patient ID: ")
        name = input("Name: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        phone = input("Phone number: ")
        patients.append(Patient(pid, name, dob, phone))
        print("✅ Patient registered!")

    elif choice == 2:
        pid = input("Enter patient ID: ")
        date = input("Appointment Date (YYYY-MM-DD): ")
        time = input("Appointment Time (HH:MM): ")
        appointments.append(Clinik(pid, date, time))
        print("✅ Appointment added!")

    elif choice == 3:
        print("\n--- All Appointments ---")
        for a in appointments:
            print(f"Patient ID: {a.patient_id} | Date: {a.date} {a.time} | Status: {a.status}")

    elif choice == 4:
        key = input("Search by (patient_id/date/status): ").lower()
        value = input("Enter value: ")
        results = [a for a in appointments if getattr(a, key, "") == value]
        if results:
            for a in results:
                print(f"Patient ID: {a.patient_id} | Date: {a.date} {a.time} | Status: {a.status}")
        else:
            print("⚠️ No appointments found.")

    elif choice == 5:
        pid = input("Enter patient ID to update: ")
        for a in appointments:
            if a.patient_id == pid:
                new_status = input("Enter new status (Scheduled/Cancelled/Done): ")
                a.status = new_status
                print("✅ Status updated!")
                break
        else:
            print("⚠️ Appointment not found.")

    elif choice == 6:
        pid = input("Enter patient ID to delete appointment: ")
        appointments = [a for a in appointments if a.patient_id != pid]
        print("✅ Appointment deleted!")

    elif choice == 7:
        today = datetime.today().strftime("%Y-%m-%d")
        print("\n--- Today's Report ---")
        for a in appointments:
            if a.date == today:
                print(f"Patient ID: {a.patient_id} | Time: {a.time} | Status: {a.status}")

        print("\n--- Cancelled Appointments ---")
        for a in appointments:
            if a.status.lower() == "cancelled":
                print(f"Patient ID: {a.patient_id} | Date: {a.date} {a.time}")

    elif choice == 8:
        save_data(patients, appointments)
        print("💾 Data saved. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice!")