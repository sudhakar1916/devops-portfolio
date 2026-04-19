from flask import Flask
app = Flask(__name__)

# In-memory counter (we'll replace with Redis later)
visit_count = 0

@app.route('/')
def home():
    global visit_count
    visit_count += 1
    return f"🚀 Day 2: Simple Flask Visit Counter<br><h1>You are visitor #{visit_count}!</h1>"

@app.route('/reset')
def reset():
    global visit_count
    visit_count = 0
    return "✅ Counter has been reset!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
