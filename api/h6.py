from flask import Blueprint, jsonify
from flask import request

bp_h6 = Blueprint("h6", __name__)

@bp_h6.route("/h6", methods=["GET", "POST", "DELETE"])
def fn_h6():

    type = request.method

    return jsonify({
        "method":type, "payload":"success", "error":False
    })


@bp_h6.route("/h6", methods=["PUT"])
def fn_h61():

    type = request.method

    return jsonify({
        "method":type, "payload":None, "error":False
    })
