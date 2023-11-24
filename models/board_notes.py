from sqlalchemy import Column, ForeignKey, Integer
from models.database import Base


class BoardNote(Base):
    __tablename__ = 'board_notes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # board_id = Column(ForeignKey("boards.id"))
    # note_id = Column(ForeignKey("notes.id"))
    board_id = Column(Integer)
    note_id = Column(Integer)
   
   
    def __init__(self, board_id, note_id):
        self.board_id = board_id
        self.note_id = note_id
