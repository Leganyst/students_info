import sqlalchemy as sa

from database.base import students_table, engine
from source.web_init import app

@app.post("/info")
def add_info(name: str, age: int, group: str, phone: str):
    conn = engine.connect()
    query = students_table.insert().values(
        name=name, age=age, group=group, phone=phone
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

