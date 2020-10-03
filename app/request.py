from app import app
import urllib.request,json
from .models import Food


# getting the api key
api_key=app.config['FOOD_API_KEY']
base_url=app.config["FOOD_API_BASE_URL"]


def get_foods(category):
    '''
    Function that gets the json response to our url request
    '''
    get_foods_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_foods_url) as url:
        get_foods_data = url.read()
        get_foods_response = json.loads(get_foods_data)

        food_results = None

        if get_foods_response['results']:
            food_results_list = get_foods_response['results']
            food_results = process_results(food_results_list)


    return food_results