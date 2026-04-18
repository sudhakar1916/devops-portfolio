from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Day 1: My first DevOps Flask app is running locally!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
