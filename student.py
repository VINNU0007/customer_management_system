students =[]

def add_student():
    print("\n----ADD STUDENT----")

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
                print("Student already exists!🤐")
                return

    name = input("Enter sudent name: ").strip()
    standard = input("Enter standard: ").strip()
    rank_input = input("Enter rank: ").strip()

    rank = int(rank_input)

    if rank < 0 :
        print("Enter a valid rank.")
        return

    student = {
         "id" : student_id,
         "name" : name,
         "standard" : standard,
         "rank" : rank
    }

    students.append(student)
    print("Student added successfully!✔")

def view_students():
    print("\n----VIEW STUDENTS----")

    if not students:
        print("NO students found❌.")
        return

    for student in students:
        print("\n------------------")

        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Standard:", student["standard"])
        print("Rank:", student["rank"])

def search_student():
    print("\n----SERACH STUDENT----")

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
           print("Student found✔.")
           print("Name:", student["name"])
           print("Standard:", student["standard"])
           print("Rank:", student["rank"])
           return

    print("Student not found❌.")

def update_student():
    print("\n----UPDATE STUDENT----")

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
           new_name = input("Enter new name (press enter to keep current)")
           new_standard = input("Enter standard (press enter to keep current)")
           new_rank = input("Enter rank (press enter to keep current)")

           if new_name:
              student["name"] = new_name
           if new_standard:
              student["standard"] = new_standard
           if new_rank:
              student["rank"] = new_rank
           print("Student updated successfully!✔")
           return

def delete_student():
    print("\n----DELETE STUDENT----")

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
           students.remove(student)
           print("Student deleted successfully!✔")
           return
    print("Student not found.")

def main():
    while True:
        print("===========================")
        print("    STUDENT MANAGEMENT    ")
        print("===========================")
        print("1. Add student")
        print("2. view students")
        print("3. search student")
        print("4. update student")
        print("5. delete student")
        print("6. exit")

        choice = input("enter your choice: ").strip()

        if choice == "1":
           add_student()
        elif choice == "2":
           view_students()
        elif choice == "3":
           search_student()
        elif choice == "4":
           update_student()
        elif choice == "5":
           delete_student()
        elif choice == "6":
           print("Thank you for using student management😍")
           break
        else:
           print("Invalid choice. please try again🔁")

if __name__ == "__main__":
    main()