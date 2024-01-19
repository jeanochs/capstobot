from flask import Flask, request
from time import sleep
import requests
import os

BOT_KEY = os.environ['BOT_KEY']

app = Flask(__name__)

posting_url = 'https://api.groupme.com/v3/bots/post'
testing_url = 'http://127.0.0.1:5000/'

group_list_text = 'The groups are as follows: '+chr(10)+chr(10)+'Positioning System: Javon Thompson, Mason Pruitte, Alisa McBryde'+chr(10)+chr(10)+'Span Connector: Noah Hackworth, Mark Lee, Chloe Sims'+chr(10)+chr(10)+'Main Systems Control: Cory Howlette, Jalani Eanochs, Kayla Hamilton'+chr(10)+chr(10)+'Window Interface System: Tyriq Turner, Landry Samuels, Issac Thomas'

help_text = 'The purpose of this bot is to keep track of project developments in the Capstone class.'+chr(10)+'Its secondary purpose is to act as a beta testing ground for larger general purpose bot projects.'+chr(10)+'Feel free to make any suggestions.'+chr(10)+chr(10)+'Current commands for this bot: '+chr(10)+':group_list -- Lists the groups and their members.'+chr(10)+':help -- Show this dialogue box.'


def compose_message(message):
    data = {
        'name':'Capstobot',
        'text':message,
        'bot_id':BOT_KEY
    }
    return data

group_list = compose_message(group_list_text)
help_menu = compose_message(help_text)


@app.route("/", methods=['POST'])
def main():
    data = request.get_json()
    print(data)

    if data['name'] != 'Capstobot' and data['text'] == ':group_status':
        requests.post(posting_url, json=group_list)
    elif data['name'] != 'Capstobot' and data['text'] == ':help':
        requests.post(posting_url, json=help_menu)

    return 'Success'

