from student_manager import StudentManager
from analytics import Analytics
from storage import Storage


manager = StudentManager()

storage = Storage("data/students.json")

manager.students = storage.load_students()

analytics = Analytics(manager.students)


while True:

    print("\n" + "=" * 45)
    print("       STUDENT PERFORMANCE SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Analytics")
    print("7. Save Students")
    print("8. Exit")
    print("9. About")

    choice = input("\nEnter your choice: ")

    try:

        if choice == "1":

            name = input("Enter student name: ")

            marks = float(input("Enter marks: "))

            manager.add_student(name, marks)

            print("Student added successfully.")


        elif choice == "2":

            manager.view_students()


        elif choice == "3":

            name = input("Enter student name to search: ")

            manager.search_student(name)


        elif choice == "4":

            name = input("Enter student name: ")

            new_marks = float(input("Enter new marks: "))

            manager.update_student(name, new_marks)


        elif choice == "5":

            name = input("Enter student name to delete: ")

            manager.delete_student(name)


        elif choice == "6":

            print("\n===== ANALYTICS =====")

            average = analytics.calculate_average()

            print(f"Average Marks: {average:.2f}")

            highest = analytics.highest_marks()

            print("\nHighest Marks:")
            highest.display()

            lowest = analytics.lowest_marks()

            print("\nLowest Marks:")
            lowest.display()

            passed, failed = analytics.pass_fail_count()

            print(f"\nPassed Students: {passed}")
            print(f"Failed Students: {failed}")

            print("\nGrade Statistics:")

            grade_counts = analytics.grade_statistics()

            for grade, count in grade_counts.items():
                print(f"{grade}: {count}")


        elif choice == "7":

            storage.save_students(manager.students)

            print("Students saved successfully.")


        elif choice == "8":

            storage.save_students(manager.students)

            print("Students saved successfully.")
            print("Thank you for using Student Performance System!")
        elif choice == "9":
            print("Student Performance System")
            print("Built using Python")
            break


        else:

            print("Invalid choice. Please enter 1-8.")


    except ValueError as error:

        print(f"Error: {error}")