# from crypt import methods
import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from selenium import webdriver
import json

load_dotenv()

store=['humor']
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
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
        # driver = webdriver.Chrome(
        # executable_path="C:/Users/uzair/Chrome Driver/chromedriver_win32/chromedriver")
        driver.get('https://www.powerlanguage.co.uk/wordle/')
        
        data = json.loads(driver.execute_script("return localStorage.getItem('gameState')"))
        ans = data['solution']
        if store[-1]!=ans:
            store.append(ans)
            if len(store)==3:
                store.pop(0)
        return respond(f"Today's Wordle Answer could either be *{store[1]}* or *{store[0]}* depending on your current timezone🙈. Countries such as India, KSA, UAE might have to wait for a few hours after 12 midnight to get the correct answer. This chatbot has been developed primarily for US residents.")
    else:
        return respond(f"Wordle ka answer chahiye toh maango, warna jaao😒. Send *wordle* to get your answer.😌")