import os
import socket
import time

from flask import Flask, jsonify

app = Flask(__name__)
READY_FILE = "/tmp/ready"


def pod_name():
    return os.getenv("POD_NAME", socket.gethostname())


@app.get("/")
def inventory():
    return jsonify(
        service="inventory",
        pod=pod_name(),
        message="inventory response",
        timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    )


@app.get("/live")
def live():
    return jsonify(status="alive", pod=pod_name())


@app.get("/ready")
def ready():
    if os.path.exists(READY_FILE):
        return jsonify(status="ready", pod=pod_name()), 200
    return jsonify(status="not-ready", pod=pod_name()), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
