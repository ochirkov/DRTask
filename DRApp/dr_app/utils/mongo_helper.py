from pymongo import MongoClient
from DRApp.dr_app.utils.checks import check_md5
from dateutil import parser


client = MongoClient()
db = client.datarobot


class MongoHelper():


    def __init__(self):
        pass


    def store(self, doc):

        raw_doc = {k:v for k,v in doc.iteritems() if k != 'md5checksum'}

        if check_md5(raw_doc, doc['md5checksum']):
            result = db.datarobot.insert_one(doc)
        else:
            return False

        return result.acknowledged


    def grab(self, id_, d_):

        res = 0

        curr_d = parser.parse(d_)

        occ_ = db.datarobot.find({"uid":id_})

        for i in occ_:
            occ_d = parser.parse(i['date'])
            if occ_d.year == curr_d.year and occ_d.day == curr_d.day:
                res += 1

        return res


