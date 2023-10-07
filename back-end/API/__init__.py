import logging
import os
from flask import Flask
from flask_cors import CORS

def create_back_end_api(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    log_level = logging.DEBUG
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    log_directory = os.path.join("Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file = os.path.join(log_directory, 'FinancialTrackingLogs.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    return app
