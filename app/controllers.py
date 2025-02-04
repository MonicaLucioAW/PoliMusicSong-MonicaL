from flask import jsonify, request
from app import db
from app.models import Song

def get_songs():
    songs = Song.query.all()
    return jsonify([{
        'id': song.ID_SONG,
        'name': song.SONG_NAME,
        'path': song.SONG_PATH,
        'plays': song.PLAYS
    } for song in songs])

def get_song(id):
    song = Song.query.get_or_404(id)
    return jsonify({
        'id': song.ID_SONG,
        'name': song.SONG_NAME,
        'path': song.SONG_PATH,
        'plays': song.PLAYS
    })

def create_song():
    data = request.get_json()
    new_song = Song(
        SONG_NAME=data['name'],
        SONG_PATH=data['path'],
        PLAYS=data.get('plays', 0)
    )
    db.session.add(new_song)
    db.session.commit()
    return jsonify({'message': 'Canción creada'}), 201

def update_song(id):
    song = Song.query.get_or_404(id)
    data = request.get_json()
    song.SONG_NAME = data.get('name', song.SONG_NAME)
    song.SONG_PATH = data.get('path', song.SONG_PATH)
    song.PLAYS = data.get('plays', song.PLAYS)
    db.session.commit()
    return jsonify({'message': 'Canción actualizada'})

def delete_song(id):
    song = Song.query.get_or_404(id)
    db.session.delete(song)
    db.session.commit()
    return jsonify({'message': 'Canción eliminada'})