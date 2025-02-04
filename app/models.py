from app import db

class Song(db.Model):
    __tablename__ = 'TBL_SONG'  # Nombre de la tabla en la base de datos
    ID_SONG = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SONG_NAME = db.Column(db.String(50), nullable=False)
    SONG_PATH = db.Column(db.String(255), nullable=False)
    PLAYS = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Song {self.SONG_NAME}>"