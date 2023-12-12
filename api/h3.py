from flask import Blueprint, jsonify

bp_h3 = Blueprint("h3", __name__)

@bp_h3.route("/h3", methods=["PUT"])
def fn_h2():

    return jsonify({
        "payload": "PUT"
    })
