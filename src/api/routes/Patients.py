from time import sleep

import requests
from flask import Blueprint, request, jsonify
import json

from src.api.utils import Responses
from src.api.utils.Responses import response_with, SUCCESS_200, SERVER_ERROR_500
from src.config.config import DevelopmentConfig
from requests.auth import HTTPBasicAuth


patient_routes = Blueprint("patient_routes", __name__)

path = "&_sort=-_lastUpdated"


@patient_routes.route("/", methods=["GET"])
def get_patients(inputURL=None):
    try:
        args = request.args
        count = args.get("count")
        auth = HTTPBasicAuth('postman', 'password')
        if inputURL:
            response = requests.get(inputURL, auth=auth).json()
        else:
            response = requests.get(DevelopmentConfig.SERVER_URL + count + path, auth=auth).json()
        # print(response['link'])

        print(response)

        url = ""
        for item in response['link']:
            if item['relation'] == 'self':
                pass
            elif item['relation'] == 'next':
                url = item['url']
                try:
                    url = url.replace("localhost:8080", "100.66.44.100:7080")
                    print(url)
                except:
                    print("Wrong format")
                print("Sleep")
                sleep(2)
                get_patients(url)
            else:
                print("weird")

        return response_with(Responses.SUCCESS_200, value={"patients": response})
    except Exception as e:
        print(e)
        return response_with(Responses.SERVER_ERROR_500)
