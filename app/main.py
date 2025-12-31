import os
import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    port = os.getenv("PORT")
    return jsonify({
        "app": "Containerized Flask App",
        "port": int(port)
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    port = os.getenv("PORT")

    if not port:
        print("ERROR: PORT environment variable is not set", file=sys.stderr)
        sys.exit(1)

    print(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=int(port))
