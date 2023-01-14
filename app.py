import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
api_key = "YOUR_API"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phishing', methods=['POST'])
def detect_phishing():
    url = request.json["url"]
    response = requests.post(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}", json={
        "client": {
            "clientId":      "yourProjectName", # replace yourProjectName with the actual project name
            "clientVersion": "1.0.0"  # replace with the version of your application
        },
        "threatInfo": {
            "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes":    ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    })
    if 'matches' in response.json():
        return jsonify(is_phishing=True)
    else:
        return jsonify(is_phishing=False)

if __name__ == '__main__':
    app.run(debug=True)
