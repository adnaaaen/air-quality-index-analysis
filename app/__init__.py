from flask import Flask
from app.routes import core_bp, app_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(app_bp)
    app.register_blueprint(core_bp)
    return app


