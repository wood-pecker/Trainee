from flask import Flask
from routers.notes import notes_bp
from routers.boards import boards_bp
from routers.errors import errors_bp
from models.database import Base


app = Flask(__name__)

app.register_blueprint(notes_bp, name="notes_bp")
app.register_blueprint(boards_bp, name="boards_bp")
app.register_blueprint(errors_bp, name="errors_bp")
 

if __name__ == '__main__':
    app.run(debug=True)
