import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def num_primo():
    count = 0
    num = 2
    primo = '1,'

    while (count <= 100):
        normal = False
        for i in range(2, num):
            if (num % i == 0):
                normal = True
                break

        if (not normal):
            count += 1
            primo = primo + str(num) + ','

        num += 1
    return primo

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

