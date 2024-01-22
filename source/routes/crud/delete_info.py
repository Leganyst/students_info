import sqlalchemy as sa

from database.base import students_table, engine
from source.web_init import app

@app.delete("/info")
def delete_info(name: str, group: str, phone: str):
    conn = engine.connect()
    query = students_table.delete().where(
        sa.and_(students_table.c.name == name, students_table.c.group == group, students_table.c.phone == phone)
    )
    try:
        conn.execute(query)
        conn.commit()
        conn.close()
        return {"ok": True}
    except Exception as e:
        print(e)
        conn.close()
        return {"error": str(e)}