# from flask import Blueprint, jsonify, redirect, render_template, request, url_for
# from main import app, Session
# from models.notes import Note


# notes_bp = Blueprint('route', __name__)

# @notes_bp.route('/note/<int:id>', methods=['GET'])
# def get_note(id):
#     session = Session()
#     note = session.query(Note).filter_by(id=id).first()
#     session.close()
#     if note:
#         return jsonify({'Note': note.content}), 200
#     return jsonify({'Error': 'Note not found'}), 404



# @notes_bp.route('/notes', methods=['GET'])
# def get_notes():
#     session = Session()
#     notes = session.query(Note).all()
#     session.close()
#     result = {}
#     for note in notes:
#         result[note.id] = note.content
#     if result:    
#         return jsonify(result), 200
#     return jsonify({'Error': 'Note not found'}), 404


# @notes_bp.route('/add-note', methods=['GET', 'POST'])
# def add_note():
#     if request.method == 'POST':
#         content = request.form.get('content')  
#         if not content:
#             return jsonify({'Error': 'Content must exist'}), 404
#         session = Session()
#         note = Note(content)
#         session.add(note)
#         session.commit()
#         return redirect(url_for('get_notes'))
    
#     if request.method == 'GET':
#         return render_template('note.html')
    