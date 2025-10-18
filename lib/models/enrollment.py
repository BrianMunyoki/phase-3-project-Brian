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
