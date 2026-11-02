import json
import os
import time
import urllib.request


url = os.getenv("INVENTORY_URL", "http://inventory:8080/")
interval = float(os.getenv("REQUEST_INTERVAL_SECONDS", "2"))

print(f"client target={url}", flush=True)
while True:
    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            body = json.loads(response.read())
            print(
                f"status={response.status} service={body['service']} pod={body['pod']} timestamp={body['timestamp']}",
                flush=True,
            )
    except Exception as exc:
        print(f"request-error={exc}", flush=True)
    time.sleep(interval)
