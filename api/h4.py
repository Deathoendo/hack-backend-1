from flask import Blueprint, jsonify

bp_h4 = Blueprint("h4", __name__)

@bp_h4.route("/h4", methods=["DELETE"])
def fn_h4():

    return jsonify({
        "payload": "delete"
    })
