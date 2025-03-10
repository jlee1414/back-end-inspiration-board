from app import db


class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    
    cards = db.relationship("Card", back_populates="board")
    
    def to_dict(self):
        board_dict =  {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
            }
            
        card_list = []
        for card in self.cards:
            card_list.append(card.to_dict())

        if card_list:
            board_dict["cards"] = card_list
        return board_dict


    def to_small_dict(self):
        board_dict =  {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
            }
        return board_dict
