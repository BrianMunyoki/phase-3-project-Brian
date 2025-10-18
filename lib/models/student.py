from lib.database import CURSOR, CONN
from lib.database import CURSOR, CONN
class Student:
    def __init__(self, name, age, email, id=None):
        self.id=id
        self.name=name
        self.age=age
        self.email=email
    def save(self):
        """Save a new student to the database."""
        CURSOR.execute(
            "INSERT INTO students (name, age, email) VALUES(?,?,?)",
            (self.name,self.age, self.email)
        )
        CONN.commit() # saves on db
        self.id=CURSOR.lastrowid
        return self
    @classmethod
    def all(cls):
        """Return all students as student objects."""
        rows =CURSOR.execute("SELECT*FROM students").fetchall()
        return [cls(id=row[0],name=row[1],age=row[2],email=row[3]) for row in rows]
    def update(self):
        """Update an existing student's data."""
        if not self.id:
            raise ValueError("Student must exist in the database before update.")
        CURSOR.execute(
            "UPDATE students SET name=?,age=?,email=? WHERE id=?",
            (self.name, self.age,self.email,self.id)
        )
        CONN.commit()
        return self
    def delete(self):
        """Delete a student from the database."""
        if not self.id:
            raise ValueError("Student must exist in the database before delete.")
        CURSOR.execute("DELETE FROM students WHERE id=?", (self.id))
        CONN.commit()