import json
from flask import Flask, jsonify

app = Flask(__name__)


def load_config(file_path):
    with open(file_path, "r") as conf:
        return json.load(conf)


@app.route("/services/<service_name>")
def get_service_addresses(service_name):
    addresses = service_registry.get(service_name)
    if addresses:
        return jsonify(addresses)
    return jsonify({"error": f"No Service: '{service_name}'"}), 404


if __name__ == "__main__":
    service_registry = load_config("./service-config.json")

    app.run(port=8888)


