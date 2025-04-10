import consulver

import sys, argparse
import hazelcast, threading

from flask import Flask, request, jsonify

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
args = parser.parse_args()

service_id = consulver.service_register("messages-service", args.port)
consul_settings = consulver.get_settings("lab_settings")

received_messages = []


def queue_listener():
    while True:
        try:
            msg = msg_queue.take()
            received_messages.append(msg)
            print(f"- Message Was Received: '{msg}'")

        except Exception as any_err:
            print(f"[ERROR] Queue read failed: '{any_err}'")
            hz.shutdown()
            sys.exit(1)


@app.route("/messages", methods=["GET"])
def ad_messenger():
    if request.method == "GET":
        return jsonify(received_messages), 200
    else:
        return jsonify("Method Not Allowed"), 405


if __name__ == "__main__":
    messages_ports = [8082, 8084]
    if args.port not in messages_ports:
        print(f"[ERROR] Port '{args.port}' is not in the"
              f" list of logging ports: {messages_ports}")
        sys.exit(1)

    hz = hazelcast.HazelcastClient(cluster_name=consul_settings["cluster_name"])
    msg_queue = hz.get_queue(consul_settings["queue_name"]).blocking()

    thread_msg = threading.Thread(target=queue_listener)
    thread_msg.start()

    try:
        app.run(port=args.port)

    finally:
        hz.shutdown()
        consulver.service_deregister(service_id)
