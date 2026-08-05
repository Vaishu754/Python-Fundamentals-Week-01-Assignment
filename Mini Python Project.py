students = []

while True:

    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        branch = input("Enter Branch: ")

        student = {
            "Name": name,
            "Age": age,
            "Branch": branch
        }

        students.append(student)

        print("Student Added Successfully.")

    elif choice == "2":

        if len(students) == 0:
            print("No Student Records Found.")
        else:
            for s in students:
                print(s)

    elif choice == "3":

        search = input("Enter Name to Search: ")

        found = False

        for s in students:
            if s["Name"].lower() == search.lower():
                print(s)
                found = True

        if not found:
            print("Student Not Found.")

    elif choice == "4":

        delete = input("Enter Name to Delete: ")

        found = False

        for s in students:
            if s["Name"].lower() == delete.lower():
                students.remove(s)
                found = True
                print("Student Deleted Successfully.")
                break

        if not found:
            print("Student Not Found.")

    elif choice == "5":

        print("Thank You!")
        break

    else:
        print("Invalid Choice.")