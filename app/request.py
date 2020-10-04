from app import app
import urllib.request,json
from .models import Food

# url = "http://quotes.stormconsultancy.co.uk/random.json"
# getting the api key
api_key=app.config['FOOD_API_KEY']
base_url=app.config["FOOD_API_BASE_URL"]


def get_foods():
    '''
    Function that gets the json response to our url request
    '''
    get_foods_url = base_url.format(api_key)

    with urllib.request.urlopen(get_foods_url) as url:
        get_foods_data = url.read()
        get_foods_response = json.loads(get_foods_data)

        food_results = []

        if get_foods_response[results.name]:
            food_results_list = get_foods_response[results.name]
            food_results = process_results(food_results_list)


    return food_results


def process_results(food_list):
    '''
    Function  that processes the food result and transform them to a list of Objects

    Args:
        food_list: A list of dictionaries that contain food details

    Returns :
        food_results: A list of food objects
    '''
    food_results = []
    for food_item in food_list:
        fcId = food_item.get('fcId')
        description = food_item.get('description')
        publicationDate = food_item.get('publicationDate')

    return food_results
