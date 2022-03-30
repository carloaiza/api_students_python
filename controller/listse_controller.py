from service.list_se_service import ListSEService
from flask import Response,json,jsonify,Blueprint
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

@app_list_se.route('/list_se/all')
def get_all_users():
    list_se_service = ListSEService()
    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

