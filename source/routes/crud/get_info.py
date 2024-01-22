import sqlalchemy as sa

from database.base import students_table, engine
from source.web_init import app

@app.get("/info/all")
def get_info_all():
    conn = engine.connect()
    query = students_table.select()
    try:
        result = conn.execute(query).fetchall()
        conn.close()
        return {"ok": True, "result": result}
    except Exception as e:
        print(e)
        conn.close()
        return {"error": str(e)}
        
@app.get("/info/one")
def get_info_one(phone: str):
    conn = engine.connect()
    query = students_table.select().where(
        students_table.c.phone == phone
    )
    try:
        result = conn.execute(query).fetchone()
        conn.close()
        return {"ok": True, "result": result}
    except Exception as e:
        print(e)
        conn.close()
        return {"error": str(e)}


@app.get("/info/group")
def get_info_group(group: str):
    conn = engine.connect()
    query = students_table.select().where(
        students_table.c.group == group
    )
    try:
        result = conn.execute(query).fetchall()
        conn.close()
        return {"ok": True, "result": result}
    except Exception as e:
        print(e)
        conn.close()
        return {"error": str(e)}
