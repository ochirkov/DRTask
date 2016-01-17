from DRApp import app
from flask import request, make_response
import json
from DRApp.dr_app.utils.mongo_helper import MongoHelper as mh


@app.route('/store', methods=['POST'])
def store():


    data  = request.get_json()
    tmp = {k.encode('utf-8'):v.encode('utf-8') for k,v in data.iteritems()}

    result = mh().store(tmp)

    if result:
        content = {"Success": "Document stored sucessfully"}
        resp = make_response(json.dumps(content), 200)
    else:
        content = {"Failure": "Checksum is not correct"}
        resp = make_response(json.dumps(content), 400)
    return resp