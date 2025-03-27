 
from Database import Database
 
class Config:
    DATABASE_URI = 'sqlite:///people.db'


class Container:
    def __init__(self):
        self.db = Database(Config.DATABASE_URI)


class AppCreator:
    def __init__(self):
        # set db and container
        self.container = Container()
        self.db = self.container.db
        # self.db.create_database()
 


app_creator = AppCreator()
db = app_creator.db
print(db)
container = app_creator.container
print(container)