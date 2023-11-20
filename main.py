from flask import Flask, redirect, render_template, request, url_for, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)


SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/notes"
)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)

    def __init__(self, content):
        self.content = content


#@app.route('/notes', methods=['GET']) - должен возвращать HTML со всеми Notes
@app.route('/note/<int:id>', methods=['GET'])
def get_note(id):
    session = Session()
    note = session.query(Note).filter_by(id=id).first()
    session.close()
    if note:
        return jsonify({'Note': note.content}), 200
    return jsonify({'Error': 'Note not found'}), 404



@app.route('/notes', methods=['GET'])
def get_notes():
    session = Session()
    notes = session.query(Note).all()
    session.close()
    result = {}
    for note in notes:
        result[note.id] = note.content
    if result:    
        return jsonify(result), 200
    return jsonify({'Error': 'Note not found'}), 404


@app.route('/add-note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        content = request.form.get('content')  
        if not content:
            return jsonify({'Error': 'Content must exist'}), 404
        session = Session()
        note = Note(content)
        session.add(note)
        session.commit()
        return redirect(url_for('get_notes'))
    
    if request.method == 'GET':
        return render_template('note.html')

    
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
