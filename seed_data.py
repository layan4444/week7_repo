from database import engine, metadata
from models import users, skills, user_skills, courses

metadata.create_all(engine)

with engine.connect() as conn:

    # USERS

    conn.execute(users.insert(), [

        {"name": "Layan"},
        {"name": "Ahmed"}

    ])

    # SKILLS

    conn.execute(courses.insert(), [
   {"title": "Python Basics", "description": "Learn Python from scratch"},
   {"title": "Machine Learning", "description": "Introduction to ML"},
   {"title": "Deep Learning", "description": "Neural networks and AI"},
])
    conn.commit()

 

print("Database seeded successfully!")