from flask_restx import Api
from tensorflow.keras.models import load_model
from app.config import MODEL
import json

model= load_model(MODEL)
api = Api()
treatmentDict = json.load(open('app/extensions/skin_disorder.json',encoding="utf8"))

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}