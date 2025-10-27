from flask import Flask, request, jsonify
from mqtt_client import publish_command
from firebase_client import get_sensor_data
from automation import apply_automation

app = Flask(__name__)

@app.route('/devices', methods=['GET'])
def get_devices():
    data = get_sensor_data()
    return jsonify(data)

@app.route('/control', methods=['POST'])
def control_device():
    payload = request.json
    device_id = payload.get("device_id")
    action = payload.get("action")
    publish_command(device_id, action)
    return jsonify({"status": "sent"})

@app.route('/automation', methods=['POST'])
def automation():
    rules = request.json.get("rules")
    result = apply_automation(rules)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)