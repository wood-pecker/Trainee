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
    session.close()
    if board:
        return jsonify({'Board': board.content}), 200
    return jsonify({'Error': 'Not found'}), 404


@boards_bp.route('/boards', methods=['GET'])
def get_boards():
    session = Session()
    boards = session.query(Board).all()
    session.close()
    result = {}
    for board in boards:
        result[board.id] = board.content
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
