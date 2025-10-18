#main
from lib.database import create_tables
from lib.cli import main_menu

if __name__=="__main__":
    create_tables()
    print("Database and tables created successfully!")