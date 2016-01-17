from DRApp import app
from flask import request, make_response
import json
from DRApp.dr_app.utils.mongo_helper import MongoHelper as mh


@app.route('/grab', methods=['GET'])
def grab():

    uid_ = request.args.get('uid')
    d_ = request.args.get('date')


    result = mh().grab(uid_, d_)
    content = {"Occurrences by given day": result}

    if result:
        resp = make_response(json.dumps(content), 200)
    else:
        resp = make_response(json.dumps(content), 400)
    return resp