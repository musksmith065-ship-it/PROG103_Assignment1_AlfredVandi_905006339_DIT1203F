print("=" * 50)
print("*" * 50)

# 1. Global list to store patient records
patient_dictionary = []


# 2. Function to register a patient
def patient_list():
    print("\n--- Registering New Patient ---")
    name = input("Enter patient name: ")
    p_id = input("Enter the patient id: ")
    age = input("Enter your age: ")
    sickness = input("Enter the patient sickness: ")

    patient_record = {
        "Name": name,
        "ID": p_id,
        "age": age,
        "sick": sickness
    }

    patient_dictionary.append(patient_record)

    # FIXED: Added a summary display so you can see what you just entered
    print("\n" + "-" * 30)
    print("REGISTRATION SUCCESSFUL!")
    print(f"Name Recorded: {name}")
    print(f"ID Recorded:   {p_id}")
    print(f"Age Recorded:  {age}")
    print(f"Condition:     {sickness}")
    print("-" * 30 + "\n")


# 3. Function to view all registered patients
def view_patient():
    if len(patient_dictionary) == 0:
        print("\n[!] No patients currently in the queue.\n")
    else:
        number = 1
        print("\n" + "@" * 50)
        print("CURRENT CLINIC QUEUE")
        print("@" * 50)
        for record in patient_dictionary:
            print(f"Queue Position: {number}")
            print(f"Patient Name:   {record['Name']}")
            print(f"Patient ID:     {record['ID']}")
            print(f"Patient Age:    {record['age']}")
            print(f"Sickness:       {record['sick']}")
            print("-" * 20)
            number += 1
        print("@" * 50 + "\n")


# 4. Main Menu Loop
while True:
    print("MAIN MENU")
    print("1. Register Patient")
    print("2. View Registered Patients")
    print("3. Serve Patient (Next in Queue)")
    print("4. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        patient_list()

    elif choice == "2":
        view_patient()

    elif choice == "3":
        if len(patient_dictionary) > 0:
            # Removes the first person added (FIFO - First In First Out)
            patient = patient_dictionary.pop(0)
            print("\n" + "!" * 50)
            print("NOW SERVING:")
            print(f"Patient: {patient['Name']} (ID: {patient['ID']})")
            print(f"Treating for: {patient['sick']}")
            print("!" * 50 + "\n")
        else:
            print("\n[!] The queue is empty. No one to serve.\n")

    elif choice == "4":
        print("\nExiting System... Have a great day!")
        break

    else:
        print("\n[!] Invalid choice. Please select 1-4.\n")