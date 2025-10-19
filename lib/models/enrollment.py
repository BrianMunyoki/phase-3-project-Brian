from lib.database import CURSOR, CONN
import sqlite3

class Enrollment:
    def __init__(self,student_id,course_id,id=None):
        self.id=id
        self.student_id=student_id
        self.course_id=course_id
    def save(self):
        """Enroll a student in a course."""
        try:
            CURSOR.execute(
                "INSERT INTO enrollments(student_id,course_id) VALUES(?,?)",
                (self.student_id,self.course_id)
            )
            CONN.commit()
            self.id=CURSOR.lastrowid
            print("Enrollment is a success!")
            return self
        except sqlite3.IntegrityError:
            print("The student is already enrolled in the course")
    @classmethod
    def all(cls):
        """Return all enrollments."""
        rows=CURSOR.execute("SELECT* FROM enrollments").fetchall()
        return[cls(id=row[0],student_id=row[1],course_id=row[2]) for row in rows]
    def delete(self):
        """Remove a student from a course"""
        if not self.id:
            raise ValueError("This enrollment must exist before deleting")
        CURSOR.execute("DELETE FROM enrollments WHERE id=?",(self.id,))
        CONN.commit()
        print("Enrollment removed")
    @classmethod
    def for_student(student_id):
        """show all courses  a student is enrolled in"""
        rows=CURSOR.execute(
            """ SELECT c.id, c.course_name, c.code, c.instructor
            FROM courses c
            JOIN enrollments e on e.course_id=c.id
            WHERE e.student_id=?;
        """,(student_id,)).fetchall()
        if not rows:
            print("This student is not enrolled in any courses.")
            return[]
        print("Courses for this student:")
        for row in rows:
            print(f"COURSE ID: {row[0]},Name:{row[1]}, code:{row[2]},Instructor:{row[3]}")
        return rows
    @classmethod
    def for_course(cls,course_id):
        """Return all students enrolled in a specific course."""
        rows=CURSOR.execute("""
        SELECT s.id,s.name,s.age,s.email
        FROM students s
        JOIN enrollments e ON e.student_id=s.id
        WHERE e.course_id=?;
        """,(course_id,)).fetchall()
        if not rows:
            print("No students are enrolled in this course.")
            return[]
        print("students in this course:")
        for row in rows:
            print(f"Student ID:{row[0]},Name:{row[1]},Age:{row[2]},Email:{row[3]}")
        return rows

