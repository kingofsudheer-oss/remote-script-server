from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

device_logs = []

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    data["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    device_logs.append(data)

    return jsonify({
        "status": "success",
        "action": "ALLOW"
    })

@app.route("/logs", methods=["GET"])
def logs():
    return jsonify(device_logs)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
