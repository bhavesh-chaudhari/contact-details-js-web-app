import numpy as np

bank_list = ["HDFC", "SBI", "KTK", "AXS", "ICICI"]


def get_ifsc():
    index = np.random.randint(0, len(bank_list))
    bank_name = bank_list[index]
    branch_detail = np.random.randint(10000, 99999)
    return bank_name + str(branch_detail)


def get_bank_account_number():
    return "".join([str(np.random.randint(0, 10)) for i in range(10)])


def get_details():
    return {"ifsc": get_ifsc(), "account_number": get_bank_account_number()}


from flask import Flask, abort, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/get_bank_details", methods=["POST"])
def get_bank_details():
    response = get_details()
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", threaded=True)
