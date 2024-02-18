from flask import Flask, request, send_file, jsonify
import pyautogui
import time
from flask_cors import CORS
import os
import requests  # Import the requests module
import base64
from datetime import datetime
import time

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

stored_url = ""  # Variable to store the URL temporarily



@app.route('/save-images', methods=['POST'])
def save_images():
    data = request.json
    customer_name = data.get('customerName')
    # print(data)
    
    # Create a folder with the customer's name if it doesn't exist
    folder_path = os.path.join(os.getcwd(), customer_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print("server")
    # Save the sample image
    sample_image_data = data.get('sampleImage')
    print(sample_image_data)
    # sample_image_data = request.files['sampleImage']
    sample_image_path = os.path.join(folder_path, f"{datetime.now().strftime('%Y%m%d%H%M%S')}-1ssss.png")
    # sample_image_data.save(sample_image_path)
    download_and_save_image(sample_image_data, sample_image_path)
    
    # Save the screenshot image
    screenshot_image_data = data.get('screenshotImage')
    screenshot_image_path = os.path.join(folder_path, f"{datetime.now().strftime('%Y%m%d%H%M%S')}-2ssss.png")
    save_base64_image(screenshot_image_data, screenshot_image_path)
    
    return jsonify(message="Images saved successfully")
def download_and_save_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image saved successfully at: {save_path}")
        else:
            print("Failed to download the image. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def save_base64_image(base64_data, save_path):
    try:
        # Split the base64 string on comma if it includes the data URL scheme
        if ',' in base64_data:
            base64_data = base64_data.split(',')[1]
        image_data = base64.b64decode(base64_data)
        with open(save_path, 'wb') as file:
            file.write(image_data)
        print(f"Image saved successfully at: {save_path}")
    except Exception as e:
        print("An error occurred while saving the image:", e)

             
@app.route('/store-url', methods=['POST'])
def store_url():
    global stored_url
    data = request.json
    stored_url = data.get('url')
    print(stored_url)
    return jsonify(message="URL stored successfully")

@app.route('/get-url', methods=['GET'])
def get_url():
    return jsonify(url=stored_url)
    print(url)

@app.route('/')
def hello():
       return 'Hello, World!'
   
if __name__ == '__main__':
       app.run("localhost", 5000)