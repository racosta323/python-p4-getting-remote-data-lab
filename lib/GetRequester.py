import requests
import json
import ipdb

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response(self):
        response = requests.get(self.url)
        return response

    def get_response_body(self):
        response_body = self.get_response()
        #.content gets body of resp
        return response_body.content

    def load_json(self):
        json_response = self.get_response().json()
        return json_response
        # return json.dumps(json_response, indent=1)

   
# ipdb.set_trace()