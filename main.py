from flask import Flask, render_template, request, Response, url_for, jsonify
import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)


SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/trainee"
)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)

    def init(self, content):
        self.content = content


#@app.route('/notes', methods=['GET']) - должен возвращать HTML со всеми Notes
@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    session = Session()
    note = session.query(Note).filter_by(id=id).first()
    session.close()
    if note:
        return jsonify({'id': note.id, 'content': note.content})
    result = jsonify({'error': 'Note not found'}), 404
    return result



@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        data = request.json
        login = data['login']
        password = data['password']

        with open('C:/Users/Egor Grozny/PycharmProjects/Trainee/users.json') as db:
            users = json.load(db)

        if login in users and users[login] == password:
            print('OK')
            return Response(status=200)
        return Response(status=401)
    else:
        return "Через браузер не можно. Можно через client.py. Хотя GET-запрос обработан"


@app.route('/user/<user>')
def username(user):
    return f"Hello, {user}. Nice to meet you!"


@app.route('/usage/<int:usage>')
def userage(usage):
    if usage >= 18:
        return "You're welcome!"
    return "This page is not for minors"


if __name__ == '__main__':
    app.run(debug=True)
