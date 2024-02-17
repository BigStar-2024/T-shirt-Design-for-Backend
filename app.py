from flask import Flask, request, send_file, jsonify
import pyautogui
import time
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

stored_url = ""  # Variable to store the URL temporarily



@app.route('/save-images', methods=['POST'])
def save_images():
    data = request.json
    customer_name = data.get('customerName')
    
    # Create a folder with the customer's name if it doesn't exist
    folder_path = os.path.join(os.getcwd(), customer_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Save the sample image
    sample_image_data = request.files['sampleImage']
    sample_image_path = os.path.join(folder_path, 'sample_image.png')
    sample_image_data.save(sample_image_path)
    
    # Save the screenshot image
    screenshot_image_data = request.files['screenshotImage']
    screenshot_image_path = os.path.join(folder_path, 'screenshot_image.png')
    screenshot_image_data.save(screenshot_image_path)
    
    return jsonify(message="Images saved successfully")
    
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