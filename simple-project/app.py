from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    count = r.incr('visits')
    return f"🚀 Day 3: Simple Flask Visit Counter (with Redis!)<br><h1>You are visitor #{count}!</h1>"

@app.route('/reset')
def reset():
    r.delete('visits')
    return "✅ Counter has been reset to 0!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
