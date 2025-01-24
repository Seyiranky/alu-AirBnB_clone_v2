#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from tests.test_models.test_engine.test_file_storage import test_FileStorage
from tests.test_models.test_engine.test_db_storage import test_DBStorage
from test_models.test_base_model import test_BaseModel
from test_models.test_user import test_User
from test_models.test_state import test_State
from test_models.test_city import test_City
from test_models.test_amenity import test_Amenity
from test_models.test_place import test_Place
from test_models.test_review import test_Review
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()