import os
from flask import Flask

app = Flask(__name__)

# Environment variables (with sensible fall-backs)
DESIRED_PATH = os.getenv("DESIRED_PATH", "/")          # e.g. "/hello"
PORT         = int(os.getenv("PORT", 8080))              # e.g. "8080"
NUMBER       = os.getenv("NUMBER", "0")                # e.g. "1"

# Main endpoint — path is dynamic
@app.route(DESIRED_PATH)
def greeting():
    return f"<h1>Hello from serverino {DESIRED_PATH} number {NUMBER}!</h1>"

# Simple health-check (always on /healthcheck)
@app.route("/healthcheck")
def healthcheck():
    return "It works! AGAIN", 200

if __name__ == "__main__":
    # 0.0.0.0 lets Docker expose the service
    app.run(host="0.0.0.0", port=PORT)

# from flask import Flask

# app = Flask(__name__)

# @app.route('/healthcheck')
# def healthcheck():
#     return "It works!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
