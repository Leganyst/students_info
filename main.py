from database.base import metadata, engine
from source.web_init import app 
from source.routes.crud import update_info, get_info, delete_info, add_info


# number = int(input("1 - удалить, 0 - воссоздать таблицы: "))
# if number:
#     metadata.drop_all(engine)
# else:
#     metadata.create_all(engine)

