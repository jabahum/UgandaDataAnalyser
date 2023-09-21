import re
from time import sleep
import pandas as pd

import requests
from flask import Blueprint, request, jsonify
import json

from api.utils import Responses
from api.utils.Responses import response_with, SUCCESS_200, SERVER_ERROR_500
from config.config import DevelopmentConfig
from requests.auth import HTTPBasicAuth
import pdb

patient_routes = Blueprint("patient_routes", __name__)
# offset = 200
jsonArray = []

path = "&_sort=-_lastUpdated"


@patient_routes.route("/", methods=["GET"])
def get_patients(inputURL=None):
    # global offset
    global jsonArray
    try:
        args = request.args
        count = args.get("count")
        offset = args.get("offset")
        auth = HTTPBasicAuth('postman', 'password')
        if inputURL:
            response = requests.get(inputURL, auth=auth).json()
        else:
            response = requests.get(DevelopmentConfig.SERVER_URL + count + path, auth=auth).json()

        jsonArray.append(response['entry'])

        print("############################")
        jsonToPandasToCsv(jsonArray)         # just going to make it rewrite the file every time for now,
                                                    # we can make it better later on
        print(response['link'])

        url = ""
        for item in response['link']:
            if item['relation'] == 'self':
                pass
            elif item['relation'] == 'next':
                url = item['url']
                try:
                    url = url.replace("localhost:8080", "100.66.44.100:7080")
                    # url = updateURL(url, offset=offset, count=count)
                    # offset += count
                    print(url)
                except:
                    print("Wrong format")
                print("Sleep")
                # sleep(2)
                get_patients(url)
                print(count)
                # pdb.set_trace()
            else:
                print("weird")

        return response_with(Responses.SUCCESS_200, value={"patients": response})
    except Exception as e:
        print(e)
        return response_with(Responses.SERVER_ERROR_500)


def updateURL(url, offset, count):

    url = re.sub(r"getpagesoffset=\d+", f"getpagesoffset={offset}", url)
    url = re.sub(r"count=\d+", f"count={count}", url)

    return url


def jsonToPandasToCsv(jsonInput):

    outputArray = []
    # going to iterate through each batch of 100 records that were added to the array of json objects
    for jsons in jsonInput:
        print(jsons)
        for item in jsons:
            row = [""] * 2
        
            try:
                row[0] = item['resource']['managingOrganization']['display']        # Managing Organization Display Name
            except Exception as e:
                print(e)
            try:
                row[1] = item['resource']['managingOrganization']['identifier']['value']    # Managing Organisation Identifier Value
            except Exception as e:
                print(e)

    
            outputArray.append(row)

    df = pd.DataFrame(outputArray, columns=["facilityName", "facilityIdentifier" ])
    df.to_csv("resources/results.csv")