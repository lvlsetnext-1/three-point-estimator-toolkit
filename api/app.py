from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

@app.route("/estimate", methods=["POST"])
def estimate():
    try:
        O = float(request.form.get("optimistic"))
        M = float(request.form.get("most_likely"))
        P = float(request.form.get("pessimistic"))
        TE = (O + 4 * M + P) / 6
        return jsonify({"expected_time": round(TE, 2)})
    except:
        return jsonify({"error": "Invalid input."}), 400

@app.route("/what-if", methods=["POST"])
def what_if():
    try:
        O = float(request.form.get("optimistic"))
        M = float(request.form.get("most_likely"))
        P = float(request.form.get("pessimistic"))
        R = int(request.form.get("resources"))
        TE = (O + 4 * M + P) / 6 / R
        return jsonify({
            "optimistic": round(O / R, 2),
            "most_likely": round(M / R, 2),
            "pessimistic": round(P / R, 2),
            "expected_time": round(TE, 2)
        })
    except:
        return jsonify({"error": "Invalid input."}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
