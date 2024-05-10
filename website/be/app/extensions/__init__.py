from flask_restx import Api
from tensorflow.keras.models import load_model
from app.config import MODEL

model= load_model(MODEL)
api = Api()

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}