import sqlalchemy as sa

from database.models import students

engine = sa.create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/students_web")
metadata = sa.MetaData()

students_table = students.create_students_table(metadata)