from flask import Blueprint, jsonify
from flask import request

bp_h9 = Blueprint("h9", __name__)



@bp_h9.route("/h9", methods=["GET"])
def fn_h9():

    Lista = ["foo","bar","baz","qux","fred"]

    buscar = False
    alias = request.args.get("alias")

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
