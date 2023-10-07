import logging
import os
from flask import Flask
from flask_cors import CORS

from API.CategoryRoutes.CreateCategoryBlueprint import create_category_route
from API.CategoryRoutes.GetAllCategoriesBlueprint import get_all_categories_route
from API.CategoryRoutes.UpdateCategoryBlueprint import update_category_route
from API.CategoryRoutes.DeleteCategoryBlueprint import delete_category_route

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

    app.register_blueprint(create_category_route)
    app.register_blueprint(get_all_categories_route)
    app.register_blueprint(update_category_route)
    app.register_blueprint(delete_category_route)

    return app
