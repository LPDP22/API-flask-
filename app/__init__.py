from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_project(Config)
    db.init_app(app)

    return app