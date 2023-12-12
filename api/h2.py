from flask import Blueprint, jsonify

bp_h2 = Blueprint("h2", __name__)

@bp_h2.route("/h2", methods=["POST"])
def fn_h2():

    return jsonify({
        "payload": "POST"
    })
