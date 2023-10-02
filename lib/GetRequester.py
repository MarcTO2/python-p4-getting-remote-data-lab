import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

        response = requests.get(URL)
        return response.content
        pass

    def load_json(self):
        response_content = self.get_programs()
        try:
            # Attempt to decode the response content as JSON
            json_data = json.loads(response_content.decode('utf-8'))
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None
        pass