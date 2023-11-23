from flask import (
    Blueprint, jsonify, redirect, render_template, request, url_for
)
from models.database import Session
from models.boards import Board


boards_bp = Blueprint('route', __name__)


@boards_bp.route('/board/<int:id>', methods=['GET'])
def get_board(id):
    session = Session()
    board = session.query(Board).filter_by(id=id).first()
    session.expunge_all()   # It works, but I don't know how
    if board:
        session.query(Board).filter(Board.id==id).update({Board.views_amount: Board.views_amount + 1})
        session.commit()
        session.close()
        return jsonify(
            {
            board.id: [board.content, board.created_at, board.updated_at, board.views_amount+1]
            }
                    ), 200
    
    session.close()
    return jsonify({'Error': 'Not found'}), 404


@boards_bp.route('/boards', methods=['GET'])
def get_boards():
    session = Session()
    boards = session.query(Board).all()
    session.close()
    result = {}
    for board in boards:
        result[board.id] = [
            board.content, board.created_at, board.updated_at, board.views_amount
        ]
    if result:    
        return jsonify(result), 200
    return jsonify({'Error': 'Board is not found'}), 404


@boards_bp.route('/add-board', methods=['GET', 'POST'])
def add_board():
    if request.method == 'POST':
        content = request.form.get('content')  
        if not content:
            return jsonify({'Error': 'Content must exist'}), 404
        session = Session()
        board = Board(content)
        session.add(board)
        session.commit()
        return redirect(url_for('boards_bp.get_boards'))
    
    if request.method == 'GET':
        return render_template('note.html')


@boards_bp.route('/del-board/<int:id>')
def delete_board(id):
    session = Session()
    session.query(Board).filter(Board.id==id).delete()
    session.commit()
    session.close()
    return redirect(url_for('boards_bp.get_boards'))


@boards_bp.route('/edit-board/<int:id>', methods=['GET', 'POST'])
def update_board(id):
    # session = Session()
    # note = session.query(Note).filter_by(id=id).first()
    # session.close()
    # yield jsonify({'Current content': note.content}), 200
    if request.method == 'POST':
        new_content = request.form.get('content')  
        if not new_content:
            return jsonify({'Error': 'Content must exist'}), 404
        session = Session()
        session.query(Board).filter(Board.id==id).update({Board.content: new_content})
        session.commit()
        session.close()
        return redirect(url_for('boards_bp.get_boards'))
    
    if request.method == 'GET':
        return render_template('note.html')
