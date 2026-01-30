from flask import Flask, request, jsonify
from datetime import datetime

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
    app.run()