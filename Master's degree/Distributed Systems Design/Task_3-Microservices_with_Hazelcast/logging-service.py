import sys, os, argparse
import hazelcast, random

from flask import Flask, request, jsonify

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
args = parser.parse_args()


@app.route("/logging", methods=["POST", "GET"])
def data_logger():
    if request.method == "POST":
        data = request.get_json()
        uuid, msg = data.get("uuid"), data.get("msg")

        if not uuid or not msg:
            return jsonify({"error": "No ID or Text in Request"}), 400

        if msg_map.contains_key(uuid):
            """
                Для перевірки того, що одне й те саме повідомлення не повторилось 
                декілька разів, реалізовано механізм 'deduplication' (once delivery).
            """
            return jsonify({"error": "Conflict due Duplication"}), 409

        msg_map.put(uuid, msg)
        print("- Message Was Logged:", msg)
        return jsonify({"success": "Message Was Logged"}), 201

    elif request.method == "GET":
        return jsonify([msg_map.get(key) for key in msg_map.key_set()])

    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    logging_ports = [8081, 8083, 8085]
    if args.port not in logging_ports:
        print(f"[ERROR] Port '{args.port}' is not in the"
              f" list of logging ports: {logging_ports}")
        sys.exit(1)

    logging_containers = ["logging-service1", "logging-service2"]
    for cname in logging_containers:
        os.system(f"docker stop {cname} >nul 2>&1")

    containers = ["hazelcast-node1", "hazelcast-node2", "hazelcast-node3", "distmap-management-center"]

    for cname in containers:
        os.system(f"docker start {cname} >nul 2>&1")

    hz = hazelcast.HazelcastClient(cluster_name="distributed-map-cluster")
    msg_map = hz.get_map("message-distributed-map").blocking()

    app.run(port=args.port)

    print("++++++++++++++++++++++++|STOP-NODE|++++++++++++++++++++++++")
    os.system(f"docker stop {random.choice(containers[:-1])}")
