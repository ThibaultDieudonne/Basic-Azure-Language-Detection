# -*- coding: utf-8 -*-

# This simple app uses the '/detect' resource to identify the language of
# the provided text or texts.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json, sys, csv

class Detector:
    def __init__(self):
        self.label_to_str = {}
        self.wiki_to_str = {}
        with open('labels.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for id, row in enumerate(spamreader):
                if id:
                    data = ''.join(row).split(';')
                    self.label_to_str[data[0]] = data[1]
                    self.wiki_to_str[data[2]] = data[1]

        key_var_name = 'AZUREKEY'
        if not key_var_name in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
        subscription_key = os.environ[key_var_name]

        endpoint_var_name = 'AZUREEDP'
        if not endpoint_var_name in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
        endpoint = os.environ[endpoint_var_name]

        path = '/Detect?api-version=3.0'
        self.constructed_url = endpoint + path

        self.headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4()),
            'Ocp-Apim-Subscription-Region': 'francecentral'
        }

    def get_language(self, text):
        if text.upper() == "X":
            sys.exit()
        body = [{
            'text': text
        }]
        request = requests.post(self.constructed_url, headers=self.headers, json=body)
        response = request.json()
        return self.wiki_to_str[response[0]["language"]]


if __name__=='__main__':
    detector = Detector()
    while 1:
        print(detector.get_language(input()))
