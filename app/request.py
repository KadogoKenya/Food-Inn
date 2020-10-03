from app import app
import urllib.request,json
from .models import Food


# getting the api key
api_key=app.config['FOOD_API_KEY']