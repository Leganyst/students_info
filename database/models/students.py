import sqlalchemy as sa

def create_students_table(metadata):
    students = sa.Table(
        "students",
        metadata,
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(100)),
        sa.Column("age", sa.Integer),
        sa.Column("group", sa.String(100)),
        sa.Column("phone", sa.String(20)),
    )

    return students