import requests
import json

class c_bls_data_api:

    def __init__(self, parameters, json_file_nm):

        # Open the output JSON file, get the report from api.bls.gov, and close the output file.

        json_file = open(json_file_nm, 'w', encoding='utf-8')
        self.get_report(parameters, json_file)
        json_file.close()

    def get_report(self, parameters, json_file):

        # Call the API to get the report. Write it to a JSON file.

        headers = {'Content-type': 'application/json'}
 
        response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data = parameters, headers = headers)

        json.dump(response.json(), json_file, indent = 6)

        