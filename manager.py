from flask_script import Manager, Server
from server import app, db

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def test():
    return 1

if __name__ == "__main__":
    manager.run()
