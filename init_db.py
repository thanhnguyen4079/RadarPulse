"""Run once to create tables on DB """

from app.db.session import engine, Base
from app.db.models import Vulnerability

def init_database():
    print("Connecting to DB")
    try:
        Base.metadata.create_all(bind = engine)
        print("Tables created successfully")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    init_database()
