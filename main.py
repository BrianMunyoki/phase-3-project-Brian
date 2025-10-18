#main
from lib.database import create_tables
from lib.cli import main_menu
from lib.models.student import Student

if __name__=="__main__":
    create_tables()

    brian=Student("Brianna",23, "brianmunyoki8@gmail.com")
    brian.save()
    print(f"Student saved with ID{brian.id}")


    all_students=Student.all()
    for s in all_students:
        print(s.id, s.name, s.age, s.email)