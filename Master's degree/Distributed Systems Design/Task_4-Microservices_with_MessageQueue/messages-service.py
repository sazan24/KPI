import sys, argparse
import hazelcast, threading

from flask import Flask, request, jsonify

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
args = parser.parse_args()

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
    logging_ports = [8082, 8084]
    if args.port not in logging_ports:
        print(f"[ERROR] Port '{args.port}' is not in the"
              f" list of logging ports: {logging_ports}")
        sys.exit(1)

    hz = hazelcast.HazelcastClient(cluster_name="distributed-queue-cluster")
    msg_queue = hz.get_queue("message-distributed-queue").blocking()

    thread_msg = threading.Thread(target=queue_listener)
    thread_msg.start()

    app.run(port=args.port)
