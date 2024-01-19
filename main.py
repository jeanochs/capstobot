from flask import Flask, request
import requests

app = Flask(__name__)

posting_url = 'https://api.groupme.com/v3/bots?token=ptv1teC42pktfUWGNKWUsfDJcisRIHaN5yJv8eZX'

sample_text = {
    'bot_id':'5e351616af1e103a36be24f653',
    'text':'This is a sample message.'
}

@app.route("/", methods=['POST'])
def main():
    data = request.get_json()
    print(data)

    if data['name'] != 'Capstobot':
        requests.post(posting_url, json=sample_text)

    return 'Success'

