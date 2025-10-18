class Course:
    def __init__(self,course_name,code,instructor,id=None):
        self.id=id
        self.course_name=course_name
        self.code=code
        self.instructor=instructor
    def save(self):
        """Save new courses to database"""
        CURSOR.execute(
            "INSERT INTO courses(course_name, code,instructor) VALUES(?,?,?)",
            (self.course_name,self.code,self.instructor)
        )
        CONN.commit()
        self.id=CURSOR.lastrowid
        return self
    @classmethod
    def all(cls):
        """Return all courses as cours objects"""
        rows=CURSOR.execute("SELECT FROM courses").fetchall()
        return [cls(id=row[0],course_name=row[1],code=row[2],instructor=row[3])]
    def update(self)
    """Update an existing course data"""
        if not self.id:
            raise ValueError("Course must exist in the data base before update")
        CURSOR.execute(
            "UPDATE Courses SET course_name=?, code=?, instructor=? , WHERE id=?",
            (self.course_name,self.code,self.instructor,self.id)
        )
        CONN.commit()
        return self
    def delete(self):
        """Deleting an existing course data"""
        if not self.id:
            raise ValueError("Course must exist in the data base before delete")
        CURSOR.execute(
            "DELETE FROM Courses WHERE id=?",(self.id)
        )
        CONN.commit()