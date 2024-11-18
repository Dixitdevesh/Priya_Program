STUDENT_FILE = 'students.txt'

def add_student():
    try:
        with open(STUDENT_FILE, 'a') as file:
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            marks_math = int(input("Enter Marks in Math: "))
            marks_science = int(input("Enter Marks in Science: "))
            marks_english = int(input("Enter Marks in English: "))
            marks_history = int(input("Enter Marks in History: "))
            marks_geography = int(input("Enter Marks in Geography: "))

            total_marks = marks_math + marks_science + marks_english + marks_history + marks_geography
            percentage = (total_marks / 500) * 100
            record = f"{roll_number},{name},{marks_math},{marks_science},{marks_english},{marks_history},{marks_geography},{total_marks},{percentage}\n"
            file.write(record)
            print(f"Student {name} added successfully!\n")
    except Exception as e:
        print("Error while adding student:", e)

def view_students():
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            if len(records) == 0:
                print("No student records found.\n")
            else:
                print("All Student Records:\n")
                print("Roll No, Name, Math, Science, English, History, Geography, Total Marks, Percentage")
                for record in records:
                    print(record.strip())
                print()
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while viewing students:", e)

def search_student():
    roll_number = input("Enter Roll Number to search: ")
    found = False
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == roll_number:
                    print(f"\nStudent Found:\nRoll Number: {fields[0]}\nName: {fields[1]}\nMath: {fields[2]}\nScience: {fields[3]}\nEnglish: {fields[4]}\nHistory: {fields[5]}\nGeography: {fields[6]}\nTotal Marks: {fields[7]}\nPercentage: {fields[8]}\n")
                    found = True
                    break
            if not found:
                print("Student not found.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while searching for student:", e)

def delete_student():
    roll_number = input("Enter Roll Number to delete: ")
    updated_records = []
    found = False
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] != roll_number:
                    updated_records.append(record)
                else:
                    found = True
        if found:
            with open(STUDENT_FILE, 'w') as file:
                file.writelines(updated_records)
            print(f"Student with Roll Number {roll_number} deleted successfully.\n")
        else:
            print("Student Roll Number not found.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while deleting student:", e)

def update_student():
    roll_number = input("Enter Roll Number to update: ")
    updated_records = []
    found = False
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == roll_number:
                    found = True
                    print("Enter new details for the student (Leave blank to keep current value):")
                    new_name = input(f"Name [{fields[1]}]: ") or fields[1]
                    new_marks_math = input(f"Math Marks [{fields[2]}]: ") or fields[2]
                    new_marks_science = input(f"Science Marks [{fields[3]}]: ") or fields[3]
                    new_marks_english = input(f"English Marks [{fields[4]}]: ") or fields[4]
                    new_marks_history = input(f"History Marks [{fields[5]}]: ") or fields[5]
                    new_marks_geography = input(f"Geography Marks [{fields[6]}]: ") or fields[6]
                    total_marks = int(new_marks_math) + int(new_marks_science) + int(new_marks_english) + int(new_marks_history) + int(new_marks_geography)
                    percentage = (total_marks / 500) * 100
                    updated_record = f"{roll_number},{new_name},{new_marks_math},{new_marks_science},{new_marks_english},{new_marks_history},{new_marks_geography},{total_marks},{percentage}\n"
                    updated_records.append(updated_record)
                else:
                    updated_records.append(record)
        if found:
            with open(STUDENT_FILE, 'w') as file:
                file.writelines(updated_records)
            print(f"Student with Roll Number {roll_number} updated successfully.\n")
        else:
            print("Student Roll Number not found.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while updating student:", e)

def calculate_total_percentage():
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            print("Total Marks and Percentage of Students:\n")
            print("Roll No, Name, Total Marks, Percentage")
            for record in records:
                fields = record.strip().split(',')
                print(f"{fields[0]}, {fields[1]}, {fields[7]}, {fields[8]}%")
            print()
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while calculating total and percentage:", e)

def rank_students():
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            students = [record.strip().split(',') for record in records]
            ranked_students = sorted(students, key=lambda x: int(x[7]), reverse=True)
            print("Ranked Students:\n")
            print("Rank, Roll No, Name, Total Marks, Percentage")
            for rank, student in enumerate(ranked_students, start=1):
                print(f"{rank}, {student[0]}, {student[1]}, {student[7]}, {student[8]}%")
            print()
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while ranking students:", e)

def top_students():
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            students = [record.strip().split(',') for record in records]
            top_students = sorted(students, key=lambda x: int(x[7]), reverse=True)[:3]
            print("Top 3 Students:\n")
            print("Roll No, Name, Total Marks, Percentage")
            for student in top_students:
                print(f"{student[0]}, {student[1]}, {student[7]}, {student[8]}%")
            print()
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while displaying top students:", e)

def backup_data():
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
        with open('students_backup.txt', 'w') as backup_file:
            backup_file.writelines(records)
        print("Backup created successfully.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while creating backup:", e)

def generate_report_card():
    roll_number = input("Enter Roll Number to generate report card: ")
    found = False
    try:
        with open(STUDENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == roll_number:
                    print("\n----- Report Card -----")
                    print(f"Roll Number: {fields[0]}")
                    print(f"Name: {fields[1]}")
                    print(f"Math: {fields[2]}")
                    print(f"Science: {fields[3]}")
                    print(f"English: {fields[4]}")
                    print(f"History: {fields[5]}")
                    print(f"Geography: {fields[6]}")
                    print(f"Total Marks: {fields[7]}")
                    print(f"Percentage: {fields[8]}%")
                    print("-----------------------\n")
                    found = True
                    break
            if not found:
                print("Student not found.\n")
    except FileNotFoundError:
        print("No student records found.\n")
    except Exception as e:
        print("Error while generating report card:", e)

def main():
    while True:
        print("------------Report Card Management System-----")
        print("------------Created By:Devesh Dixit-----------")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Calculate Total and Percentage")
        print("7. Rank Students")
        print("8. Top Students")
        print("9. Backup Data")
        print("10. Generate Report Card")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            calculate_total_percentage()
        elif choice == '7':
            rank_students()
        elif choice == '8':
            top_students()
        elif choice == '9':
            backup_data()
        elif choice == '10':
            generate_report_card()
        elif choice == '11':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
