from flask import Blueprint, jsonify
from flask import request

bp_h8 = Blueprint("h8", __name__)

@bp_h8.route("/h8", methods=["POST"])
def fn_h8():
    data = request.json
    email = data.get("email")
    alias = data.get("alias")
    

    return jsonify({
        "payload":{"email":email, "name":alias},
        "error":{"available":False,"err_msg":None},
        "status":200
    })
