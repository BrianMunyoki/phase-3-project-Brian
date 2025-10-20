from lib.database import create_tables
from lib.models.student import Student
from lib.models.course import Course
from lib.models.enrollment import Enrollment

if __name__ == "__main__":
    #  Create the database tables
    create_tables()

    #  Add a student
    brian = Student("Brian Muema", 22, "brian.muema@upmention.com")
    brian.save()

    #  Add a course
    biology = Course("Biology", "BIO101", "Dr. Joy")
    biology.save()

    #  Enroll Brian into Biology
    enrollment = Enrollment(student_id=brian.id, course_id=biology.id)
    enrollment.save()

    #  Show all courses Brian is enrolled in
    print("\n--- Courses for Brian ---")
    Enrollment.for_student(brian.id)

    # Show all students in Biology
    print("\n--- Students in Biology ---")
    Enrollment.for_course(biology.id)

    #  View all enrollments (just to confirm)
    print("\n--- All Enrollments ---")
    all_enrollments = Enrollment.all()
    for e in all_enrollments:
        print(f"Enrollment ID: {e.id}, Student ID: {e.student_id}, Course ID: {e.course_id}")
