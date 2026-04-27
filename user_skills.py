from sqlalchemy import Table, Column, Integer, ForeignKey

from database import metadata

 

user_skills = Table(

    "user_skills",

    metadata,

    Column("user_id", Integer, ForeignKey("users.id")),

    Column("skill_id", Integer, ForeignKey("skills.id"))

)