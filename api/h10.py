from flask import Blueprint, jsonify
from flask import request

bp_h10 = Blueprint("h10", __name__)



@bp_h10.route("/h10", methods=["POST"])
def fn_h10():

    Lista = ["foo","bar","baz","qux","fred"]

    data = request.json
    buscar = False
    alias = data.get("alias")

    for x in Lista:
        if x == alias:
            buscar = True
    if buscar == True:
        return jsonify({
        "payload":alias,
        "error":{"available":False,"err_msg":None},
        "status":200
    })
    else:
        return jsonify({
        "payload":"not found",
        "error":{"available":False,"err_msg":None},
        "status":404
    })