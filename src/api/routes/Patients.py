import re
from time import sleep
import pandas as pd

import requests
from flask import Blueprint, request, jsonify
import json

from src.api.utils import Responses
from src.api.utils.Responses import response_with, SUCCESS_200, SERVER_ERROR_500
from src.config.config import DevelopmentConfig
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
        for item in jsons:
            row = [""] * 12
            try:
                row[0] = item['resource']['name'][0]['given'][0]        # given name
            except Exception as e:
                print(e)
            try:
                row[1] = item['resource']['name'][0]['family']          # family name
            except Exception as e:
                print(e)
            try:
                row[2] = item['resource']['gender']                  # gender
            except Exception as e:
                print(e)
            try:
                row[3] = item['resource']['birthDate']               # DOB
            except Exception as e:
                print(e)
            try:
                row[4] = item['resource']['telecom'][0]['value']        # phone number
            except Exception as e:
                print(e)
            try:
                row[5] = item['resource']['address'][0]['city']               # City
            except Exception as e:
                print(e)
            try:
                row[6] = item['resource']['address'][0]['country']            # Country
            except Exception as e:
                print(e)
            try:
                row[7] = item['resource']['address'][0]['postalCode']         # Postal code
            except Exception as e:
                print(e)
            try:
                for value in item['resource']['address'][0]['extension'][0]['extension']:
                    if "subcounty" in value['url']:              # county
                        row[8] = value['valueString']
                    elif "parish" in value['url']:                 # parish
                        row[9] = value['valueString']
                    elif "village" in value['url']:                # village
                        row[10] = value['valueString']
                    else:
                        print("WEIRD")
            except Exception as e:
                print(e)
            try:
                for id in item['resource']['identifier']:                   # finding National ID No
                    if id['type']['text'] == "National ID No.":
                        row[11] = id['value']
            except Exception as e:
                print(e)

            outputArray.append(row)

    df = pd.DataFrame(outputArray, columns=["givenName", "familyName", "gender", "birthDate", "phoneNumber", "city",
                                            "country", "postalCode", "county", "parish", "village", "nationalID"])
    df.to_csv("resources/results.csv")
