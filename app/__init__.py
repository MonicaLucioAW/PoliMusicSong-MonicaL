from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Verificar variables (¡NUEVO! Esto mostrará los valores en consola)
print("[DEBUG] Variables de entorno cargadas:")
print(f"DB_SERVER: {os.getenv('DB_SERVER')}")
print(f"DB_PORT: {os.getenv('DB_PORT')}")
print(f"DB_USER: {os.getenv('DB_USER')}")

# Crear aplicación Flask
app = Flask(__name__)

# Configurar SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mssql+pyodbc://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_SERVER')},{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}?"
    "driver=ODBC+Driver+17+for+SQL+Server"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar rutas DESPUÉS de crear la app y db (¡IMPORTANTE!)
from app import routes

# Registrar blueprint
app.register_blueprint(routes.bp, url_prefix='/api')