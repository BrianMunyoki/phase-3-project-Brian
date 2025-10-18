#main
from lib.database import create_tables
from lib.cli import main_menu
from lib.models.student import Student
from lib.models.course import Course

if __name__=="__main__":
    create_tables()

    brian=Student("Brianhnfak",2808, "brianmunyokoii89@gmail.com")
    brian.save()
    print(f"Student saved with ID{brian.id}")

    Biology=Course("Bioplokgpy",189971,"Dr.pJkoly")
    Biology.save()


    all_students=Student.all()
    for s in all_students:
        print(s.id, s.name, s.age, s.email)