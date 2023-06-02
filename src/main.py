import os

from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from src.api.routes.Patients import patient_routes

from src.config.config import ProductionConfig, DevelopmentConfig

SWAGGER_URL = "/api/docs"
app = Flask(__name__)

if os.environ.get("WORK_ENV") == "PROD":
    app_config = ProductionConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

app.register_blueprint(patient_routes, url_prefix="/api/v1/patients")


@app.route("/api/spec")
def spec():
    swag = swagger(app, prefix="/api")
    swag["info"]["base"] = "http://localhost:5000"
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "ClientDataAnalyser"
    return jsonify(swag)


swaggerui_blueprint = get_swaggerui_blueprint(
    "/api/docs", "/api/spec", config={"app_name": "ClientDataAnalyser"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run( host="0.0.0.0/api/v1/", use_reloader=False)
