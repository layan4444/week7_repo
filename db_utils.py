from sqlalchemy import select

from database import engine

from models import users, skills, user_skills, courses

 

 

# get user skills from DB

def get_user_skills(user_id):
    with engine.connect() as conn:

        query = (

            select(skills.c.name)
            .select_from(user_skills.join(skills))
            .where(user_skills.c.user_id == user_id)

        )

        result = conn.execute(query)
        return [row[0] for row in result.fetchall()]


# get all courses

def get_all_courses():
    with engine.connect() as conn:

        result = conn.execute(select(courses))
        return result.fetchall()