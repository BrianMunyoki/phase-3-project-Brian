class Student:
    def __init__(self, name, age, email, id=None)
        self.id=id
        self.name=name
        self.age=age
        self.email=email
    def save(self):
        """Save a new student to the database."""
        CURSOR.execute(
            "INSERT INTO students (name, age, email) VALUES(?,?,?)",
        )
        
