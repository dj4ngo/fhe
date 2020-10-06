#!/usr/bin/env python3

import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/sensor/sync', methods = ['POST'])
def run_app():
    mac = request.form['mac_address']
    ip = request.form['address_ip']

    data = {"result": {"status":"OK", "address_ip":ip}}

    return Response(json.dumps(data), \
            content_type='application/json; charset=UTF-8')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
