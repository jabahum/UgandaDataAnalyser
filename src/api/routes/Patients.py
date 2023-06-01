import requests
from flask import Blueprint, request

from src.api.utils import Responses
from src.api.utils.Responses import response_with, SUCCESS_200, SERVER_ERROR_500
from src.config.config import DevelopmentConfig
from requests.auth import HTTPBasicAuth


patient_routes = Blueprint("patient_routes", __name__)

path = "&_sort=-_lastUpdated"


@patient_routes.route("/", methods=["GET"])
def get_patients():
    try:
        args = request.args
        count = args.get("count")
        auth = HTTPBasicAuth('postman', 'password')
        response = requests.get(DevelopmentConfig.SERVER_URL + count + path, auth=auth)
        return response_with(Responses.SUCCESS_200, value={"patients": response.json()})
    except Exception as e:
        print(e)
        return response_with(Responses.SERVER_ERROR_500)
