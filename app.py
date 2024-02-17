from flask import Flask, request, send_file, jsonify
import pyautogui
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

stored_url = ""  # Variable to store the URL temporarily

@app.route('/capture-screenshot', methods=['GET', 'POST'])

# Define and store the current time

def capture_screenshot():
    if request.method == 'POST':
        customer_name = request.json['customerName']
        # customer_name = request.form.get('customerName') # Get the customer name from the form input
        current_time = time.strftime("%Y%m%d%H%M%S")
        print(customer_name)
        # Define the coordinates and size of the region to capture
        left = 695  # X-coordinate of the top-left corner of the region
        top = 260   # Y-coordinate of the top-left corner of the region
        width = 525  # Width of the region
        height = 525  # Height of the region
        
        # Capture the screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        file_name = f"{current_time}-2{customer_name}.png"
        print(file_name)
        screenshot.save(file_name)
        
        # Return the screenshot file as an attachment
        return send_file(file_name, as_attachment=True)
    else:
        return 'Method Not Allowed', 405
    
@app.route('/store-url', methods=['POST'])
def store_url():
    global stored_url
    data = request.json
    stored_url = data.get('url')
    return jsonify(message="URL stored successfully")

@app.route('/get-url', methods=['GET'])
def get_url():
    return jsonify(url=stored_url)

@app.route('/')
def hello():
       return 'Hello, World!'
   
if __name__ == '__main__':
       app.run()