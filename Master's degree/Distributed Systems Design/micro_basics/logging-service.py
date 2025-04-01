from flask import Flask, request, jsonify

app = Flask(__name__)

msg_store = {}  # {UUID: Message}


@app.route("/logging", methods=["POST", "GET"])
def data_logger():
    if request.method == "POST":
        data = request.get_json()
        uuid, msg = data.get("uuid"), data.get("msg")

        if not uuid or not msg:
            return jsonify({"error": "No ID or Text in Request"}), 400

        if (uuid in msg_store) or (msg in msg_store.values()):
            """
                Для перевірки того, що одне й те саме повідомлення не повторилось 
                декілька разів, реалізовано механізм 'deduplication' (once delivery).
            """
            return jsonify({"error": "Conflict due Duplication"}), 409

        msg_store[uuid] = msg
        print("- Message Was Logged:", msg)
        return jsonify({"success": "Message Was Logged"}), 201

    elif request.method == "GET":
        return jsonify(list(msg_store.values()))

    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    app.run(port=8081)
