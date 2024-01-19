from flask import Flask, request
import requests

app = Flask(__name__)

posting_url = 'https://api.groupme.com/v3/bots/post'
testing_url = 'http://127.0.0.1:5000/'

sample_text_1 = {
    'bot_id':'5e351616af1e103a36be24f653',
    'text':'The groups are as follows: '
}

sample_text_2 = {
    'bot_id':'5e351616af1e103a36be24f653',
    'text':'Positioning System: Javon Thompson, Mason Pruitte, Alisa McBryde'
}

sample_text_3 = {
    'bot_id':'5e351616af1e103a36be24f653',
    'text':'Span Connector: Noah Hackworth, Mark Lee, Chloe Sims'
}

sample_text_4 = {
    'bot_id':'5e351616af1e103a36be24f653',
    'text':'Main Systems Control: Cory Howlette, Jalani Eanochs, Kayla Hamilton'
}

sample_text_5 = {
    'bot_id':'5e351616af1e103a36be24f653',
    'text':'Window Interface System: Tyriq Turner, Landry Samuels, Issac Thomas'
}


@app.route("/", methods=['POST'])
def main():
    data = request.get_json()
    print(data)

    if data['name'] != 'Capstobot' and data['text'] == ':group_status':
        requests.post(posting_url, json=sample_text_1)
        requests.post(posting_url, json=sample_text_2)
        requests.post(posting_url, json=sample_text_3)
        requests.post(posting_url, json=sample_text_4)
        requests.post(posting_url, json=sample_text_5)

    return 'Success'

