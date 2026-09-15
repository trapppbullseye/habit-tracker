from flask import Flask, jsonify, render_template
app = Flask(__name__)
@app.route('/') def index(): return render_template('index.html', name="habit-tracker", desc="Daily habit tracker with streak calendar")
@app.route('/api/health') def health(): return jsonify({"app":"habit-tracker","status":"ok"})
if __name__ == '__main__': app.run(port=5000)
