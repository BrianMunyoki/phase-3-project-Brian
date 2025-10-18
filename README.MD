# Student Management System (CLI Project)

A Python-based **Command-Line Interface (CLI)** application designed to manage students, courses, and enrollments efficiently.  
This project demonstrates the use of **Object-Oriented Programming (OOP)**, **SQLite3**, and **CRUD operations**, built entirely without external ORM libraries.

##Project Overview

The **Student Management System** helps users:

- Add, view, update, and delete students.
- Manage courses and instructors.
- Enroll students in one or more courses.
- View which students are in each course.
- Store all data persistently using **SQLite3**.

Developed by **Brian Muema** as part of the Phase 3 Python Project.

## Technologies Used

- Python 3
- SQLite3 (built-in module)
- Object-Oriented Programming (OOP)
- Command-Line Interface (CLI)
- Virtual Environment (`venv`)

## Project Structure

phase-3-project-Brian/
│
├── lib/
│ ├── cli.py # CLI logic and menus
│ ├── database.py # Database connection and setup
│ └── models/
│ ├── student.py # Student model (CRUD operations)
│ ├── course.py # Course model (CRUD operations)
│ └── enrollment.py # Enrollment model (many-to-many link)
│
├── db/
│ └── database.db # SQLite database file
│
├── main.py # Entry point of the application
├── README.md # Project documentation
└── .gitignore # Files to ignore in Git

---

## 💡 Features

### 👩‍🎓 Student Management

- Add a new student with name, age, and email.
- View all registered students.
- Update or delete existing students.

### 📚 Course Management

- Add new courses with name, code, and instructor.
- View, update, or delete courses.

### 🔗 Enrollment Management

- Enroll students into one or more courses.
- View all courses a student is enrolled in.
- View all students in a specific course.
- Remove or update enrollments if needed.

---

## 🧩 Database Design

### **students**

| Column | Type          | Description       |
| ------ | ------------- | ----------------- |
| id     | INTEGER (PK)  | Unique student ID |
| name   | TEXT          | Student name      |
| age    | INTEGER       | Student age       |
| email  | TEXT (UNIQUE) | Student email     |

### **courses**

| Column      | Type         | Description      |
| ----------- | ------------ | ---------------- |
| id          | INTEGER (PK) | Unique course ID |
| course_name | TEXT         | Course name      |
| code        | TEXT         | Course code      |
| instructor  | TEXT         | Instructor name  |

### **enrollments**

| Column     | Type         | Description             |
| ---------- | ------------ | ----------------------- |
| id         | INTEGER (PK) | Unique enrollment ID    |
| student_id | INTEGER (FK) | References students(id) |
| course_id  | INTEGER (FK) | References courses(id)  |

---

## 🚀 How to Run the Project

### 1️ Clone the repository

```bash
git clone https://github.com/your-username/phase-3-project-Brian.git
cd phase-3-project-Brian

### 2️ Create and activate a virtual environment

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv  source venv/bin/activate     # On Mac/Linux  venv\Scripts\activate        # On Windows   `

### 3️ Run the program

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python main.py   `

### 4 Follow the menu prompts to interact with the system.

Learning Objectives
----------------------

This project demonstrates your ability to:

*   Design and implement **database schemas** manually.

*   Link Python classes to database records using SQL queries.

*   Apply **OOP principles** (classes, methods, instances).

*   Organize a real-world project with clear file structure.

*   Communicate technical ideas clearly and professionally.


License
----------

This project was created for educational purposes as part of the **Phase 3 Python Curriculum**.Feel free to use and adapt it for learning.

Author
---------

**Brian Muema**Python Developer & Student📧 brian.muema@example.com GitHub: [github.com/your-username](https://github.com/your-username)
```
