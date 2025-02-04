from flask import Blueprint
from app.controllers import get_songs, get_song, create_song, update_song, delete_song

# Crear un Blueprint para las rutas
bp = Blueprint('routes', __name__)

# Definir las rutas
bp.route('/songs', methods=['GET'])(get_songs)
bp.route('/songs/<int:id>', methods=['GET'])(get_song)
bp.route('/songs', methods=['POST'])(create_song)
bp.route('/songs/<int:id>', methods=['PUT'])(update_song)
bp.route('/songs/<int:id>', methods=['DELETE'])(delete_song)