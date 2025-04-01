from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/messages", methods=["GET"])
def ad_messenger():
    if request.method == "GET":
        return "I'm not implemented yet ^_^"
    else:
        return jsonify("Method Not Allowed"), 405


if __name__ == "__main__":
    app.run(port=8082)
