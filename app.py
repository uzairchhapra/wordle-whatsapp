# from crypt import methods
import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

load_dotenv()

app = Flask(__name__)
client = Client()

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/wordle',methods=['POST'])
def get_wordle_answer():
    message = request.form.get('Body').lower()
    print(message)
    print('XXXXXXXXXXXX')
    if message=='wordle':
        driver = webdriver.Chrome(
        executable_path="C:/Users/uzair/Chrome Driver/chromedriver_win32/chromedriver")
        driver.get('https://www.powerlanguage.co.uk/wordle/')
        
        data = json.loads(driver.execute_script("return localStorage.getItem('gameState')"))
        ans = data['solution']
        return respond(f"Today's Wordle Answer👀: {ans}")
    else:
        return respond(f"Wordle ka answer chahiye toh maango, warna jaao.😒")