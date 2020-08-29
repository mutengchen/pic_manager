import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_restful import Api

from app.routes import frontend
from core.settings import Setting as ST
from utils.my_logger import get_logger
app = Flask(__name__)
logger = get_logger()
def start_server():
    if ST.DEBUG:
        create_app().run(port=ST.SERVER_PORT, use_reloader=False, threaded=True)
    else:
        create_app().run(host='0.0.0.0', port=ST.SERVER_PORT, threaded=True)
        logger.info("start_server")


def create_app():
    app.config.from_object(__name__)
    Bootstrap(app)
    api = Api()
    api.init_app(app)
    ST.SERVERSTATICROOT = os.path.join(app.root_path, 'static')
    app.register_blueprint(frontend)
    return app
