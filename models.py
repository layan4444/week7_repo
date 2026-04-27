from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text

from database import metadata

 

# USERS

users = Table(

    "users",

    metadata,

    Column("id", Integer, primary_key=True),

    Column("name", String)

)

 

# SKILLS

skills = Table(

    "skills",

    metadata,

    Column("id", Integer, primary_key=True),

    Column("name", String)

)

 

# USER_SKILLS (MANY TO MANY)

user_skills = Table(

    "user_skills",

    metadata,

    Column("user_id", Integer, ForeignKey("users.id")),

    Column("skill_id", Integer, ForeignKey("skills.id"))

)

 

# COURSES

courses = Table(

    "courses",

    metadata,

    Column("id", Integer, primary_key=True),

    Column("title", String),

    Column("description", Text)

)