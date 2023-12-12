from flask import Blueprint, jsonify

bp_h5 = Blueprint("h5", __name__)

@bp_h5.route("/h5", methods=["GET"])
def fn_h5():

    return jsonify({
        "payload": "success", "error": False
    })


@bp_h5.route("/h5", methods=["POST", "DELETE", "PUT"])
def fn_h51():

    return jsonify({
        
    })
