from flask import abort
from flask_restx import Api, Resource,Namespace
from flask_restx import reqparse
from app.services.DetectService import DetectService
from werkzeug.datastructures import FileStorage




Detect_ns = Namespace('api/', description='Detect operations')
upload_parser = Detect_ns.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)
@Detect_ns.route('/Detect')
@Detect_ns.expect(upload_parser)
@Detect_ns.response(200, 'Success')
@Detect_ns.response(400, 'Bad request')
@Detect_ns.response(401, 'Unauthorized')
@Detect_ns.response(404, 'Not found')
@Detect_ns.response(500, 'Internal Server Error')
class Detect(Resource):
    @Detect_ns.doc(description='Detect')
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        return DetectService.Detect(uploaded_file)
    
@Detect_ns.route('/Get-treatment/<disease>')
@Detect_ns.response(200, 'Success')
@Detect_ns.response(400, 'Bad request')
@Detect_ns.response(401, 'Unauthorized')
@Detect_ns.response(404, 'Not found')
@Detect_ns.response(500, 'Internal Server Error')
class GetTreatment(Resource):
    @Detect_ns.doc(description='Get treatment')
    def get(self,disease):
        return DetectService.GetTreatment(disease)

    