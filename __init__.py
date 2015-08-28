from flask import Flask
from flask import request, jsonify
import json
import log
from storage import Redis



app = Flask(__name__)
@app.route("/echo/api/v1.0", methods=['POST'])

def ReqHandler():
    '''
    Handles POST requests
    '''    


    # Validates request

    headers = request.headers

    # Updates session object, create if not present

    body = request.get_json()

    # Logic


    # Build response
    
    app.logger.addHandler(log.fh)

    x = {'version': '1.0', 'response': {'outputSpeech': {'text': 'Your favorite color is blue, goodbye', 'type': 'PlainText'}, 'shouldEndSession': 'true', 'reprompt': {'outputSpeech': {'text': 'null', 'type': 'PlainText'}}, 'card': {'content': 'SessionSpeechlet - Your favorite color is blue, goodbye', 'type': 'Simple', 'title': 'SessionSpeechlet - WhatsMyColorIntent'}}, 'sessionAttributes': {}}
    x['response']['shouldEndSession'] = 'false'
    x = json.dumps(x)
    head = {}

    head['Content-Type'] = 'application/json'
    return x, 200, head

if __name__ == "__main__":
    app.run()
