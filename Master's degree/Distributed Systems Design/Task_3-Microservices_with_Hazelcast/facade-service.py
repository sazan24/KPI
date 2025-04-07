from time import sleep, strftime

import requests, random
from uuid import uuid4

from flask import Flask, request, jsonify
from tenacity import retry, stop_after_attempt, wait_exponential, RetryError

app = Flask(__name__)
attempt = 0

config_server = "http://localhost:8888/services"


def get_random_service(service_name):
    response = requests.get(f"{config_server}/{service_name}", timeout=3)
    services = response.json()

    return random.choice(services) if services else None


@retry(stop=stop_after_attempt(3),
       wait=wait_exponential(min=1, max=2))  # Wait 1 and 2 sec
def sending_with_retry(data):
    """
        Для випадків, коли присутні затримки у зв'язку або відсутні відповіді, реалізовано
        механізм 'retry', який пробує повторити цю саму операцію по передачі повідомлення.
    """
    global attempt
    attempt += 1

    try:
        logging_service = get_random_service("logging-service")
        response = requests.post(logging_service, json=data, timeout=5)  # Also plus 5 sec
        return response
    except requests.exceptions.RequestException as ret_err:
        print(f"№{attempt} POST-request with {data} at {strftime('%H:%M:%S')}")
        print(f"↑ RetryError: {ret_err}\n")
        sleep(1)
        raise


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=2))  # Wait 1 and 2 sec
def receiving_with_retry(log_endpoint, msg_endpoint):
    """
        Функція з механізмом 'retry' для повторення GET-запиту по отриманні даних.
    """
    global attempt
    attempt += 1

    try:
        logging_service = get_random_service(log_endpoint)
        logging_response = requests.get(logging_service, timeout=5)

        messages_service = get_random_service(msg_endpoint)
        messages_response = requests.get(messages_service)
        return logging_response, messages_response
    except requests.exceptions.RequestException as ret_err:
        print(f"№{attempt} GET-request from '/{{api-endpoint}}' at {strftime('%H:%M:%S')}")
        print(f"↑ RetryError: {ret_err}\n")
        sleep(1)
        raise


@app.route("/facade", methods=["POST", "GET"])
def request_handler():
    global attempt

    if request.method == "POST":
        msg = request.form.get("msg")
        if not msg: return jsonify({"error": "No Message in Request"}), 400

        uuid = str(uuid4())
        data = {"uuid": uuid, "msg": msg}

        try:
            response = sending_with_retry(data)  # 201 OR 409
            return jsonify({"response": response.json(),
                            "message": data}), response.status_code
        except RetryError:
            return jsonify({"error": "Logging-Service Unavailable"}), 500
        finally:
            attempt = 0

    elif request.method == "GET":
        try:
            logging_response, messages_response = receiving_with_retry("logging-service", "messages-service")
            return jsonify([f"logging-service: {logging_response.text}",
                            f"messages-service: {messages_response.text}"]), 200
        except RetryError:
            return jsonify({"error": "MSG or LOG services are Unavailable"}), 500
        finally:
            attempt = 0

    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    app.run(port=8080)
