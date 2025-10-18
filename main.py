#main
from lib.database import create_tables
from lib.cli import main_menu
from lib.models.student import Student
from lib.models.course import Course

if __name__=="__main__":
    create_tables()

    brian=Student("Brianhnfaky",2808, "brianmunyokoiio68t9@gmail.com")
    brian.save()
    print(f"Student saved with ID{brian.id}")

    Biology=Course("Bioplokgpy",189971,"Dr.pJkoly")
    from lib.models.enrollment import Enrollment

# Add a test enrollment
    enrollment = Enrollment(student_id=1, course_id=1)
    enrollment.save()

# View all enrollments
    for e in Enrollment.all():
        print(e.id, e.student_id, e.course_id)


    all_students=Student.all()
    for s in all_students:
        print(s.id, s.name, s.age, s.email)
