import sqlalchemy as sa

from database.base import students_table, engine
from source.web_init import app

@app.put("/info/{id}")
def update_info(id: int, name: str = None, age: int = None, group: str = None, phone: str = None):
    conn = engine.connect()
    stored_item_data = {}
    if name is not None:
        stored_item_data["name"] = name
    if age is not None:
        stored_item_data["age"] = age
    if group is not None:
        stored_item_data["group"] = group
    if phone is not None:
        stored_item_data["phone"] = phone
    query = students_table.update().where(students_table.c.id == id).values(**stored_item_data)
    try:
        conn.execute(query)
        conn.commit()
        conn.close()
        return {"ok": True}
    except Exception as e:
        print(e)
        conn.close()
        return {"error": str(e)}
