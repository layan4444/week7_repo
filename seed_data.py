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

    conn.execute(skills.insert(), [

        {"name": "python"},

        {"name": "machine learning"},

        {"name": "sql"},

        {"name": "deep learning"}

    ])

 

    conn.commit()

 

print("Database seeded successfully!")