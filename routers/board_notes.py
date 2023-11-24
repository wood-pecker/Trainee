from flask import (
    Blueprint, jsonify, redirect, render_template, request, url_for
)
from sqlalchemy import and_
from models.database import Session
from models.board_notes import BoardNote
from models.notes import Note


boardnote_bp = Blueprint('route', __name__)


@boardnote_bp.route('/content/<int:id>', methods=['GET'])
def get_board_content(id):
    session = Session()
    board_notes = session.query(BoardNote).filter(BoardNote.board_id == id).all()
    result = {id: []}
    if board_notes:
        for row in board_notes:
            note = session.query(Note).filter_by(id=row.note_id).first()
            result[id].append([
                note.id, note.content, note.created_at, note.updated_at, 
                note.views_amount
            ])
    session.close()
    return jsonify(result), 200
    

@boardnote_bp.route('/pin', methods=['GET', 'POST'])
def pin():
    if request.method == 'POST':
        board_id = int(request.form.get('board_id'))
        note_id = int(request.form.get('note_id'))
        if board_id and note_id:
            session = Session()
            bn = BoardNote(board_id, note_id)
            session.add(bn)
            session.commit()
            session.close()
            return redirect(url_for('boardnote_bp.get_board_content', id=board_id))
        else:
            return jsonify({'Error': 'Content must exist'}), 404
        
    if request.method == 'GET':
        return render_template('board_note.html')


@boardnote_bp.route('/unpin', methods=['GET', 'POST'])
def unpin():
    if request.method == 'POST':
        board_id = int(request.form.get('board_id'))
        note_id = int(request.form.get('note_id'))
        if board_id and note_id:
            session = Session()
            session.query(BoardNote).filter(and_(BoardNote.board_id==board_id,
                                             BoardNote.note_id==note_id)).delete()
            session.commit()
            session.close()
            return redirect(url_for('boardnote_bp.get_board_content', id=board_id))
        else:
            return jsonify({'Error': 'Content must exist'}), 404
        
    if request.method == 'GET':
        return render_template('board_note.html')