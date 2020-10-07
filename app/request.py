# from app import app
import urllib.request,json
from .models import Giphy

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['GIPHY_API_KEY']
    base_url=app.config["GIPHY_API_BASE_URL"]


def get_giphys():
    '''
    Function that gets the json response to our url request
    '''
    get_giphys_url = base_url.format(api_key)

    with urllib.request.urlopen(get_giphys_url) as url:
        get_giphys_data = url.read()
        get_giphys_response = json.loads(get_giphys_data)

        giphy_results = None

        if get_giphys_response['data']:
            giphy_results_list = get_giphys_response['data']
            giphy_results = process_results(giphy_results_list)


    return giphy_results


def process_results(giphy_list):
    '''
    Function  that processes the food result and transform them to a list of Objects

    Args:
        food_list: A list of dictionaries that contain food details

    Returns :
        food_results: A list of food objects
    '''
    giphy_results = []
    for giphy_item in giphy_list:
        id = giphy_item.get('id')
        url=giphy_item.get('url')
        title=giphy_item.get('title')
        images=giphy_item.get('images').get('downsized').get('url')


        if id:
            giphy_object = Giphy(id,url,title,images)
            giphy_results.append(giphy_object)

    return giphy_results


def get_giphy(id):
    get_giphy_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_giphy_details_url) as url:
        giphy_details_data = url.read()
        giphy_details_response = json.loads(giphy_details_data)

        giphy_object = None
        if giphy_details_response:
            id = giphy_details_response.get('id')
            url=giphy_details_response.get('url')
            title=giphy_details_response.get('url')
            images=giphy_details_response.get('images')
            

            giphy_object = Giphy(id,url,title,images)

    return giphy_object


def search_giphy(movie_name):
    search_giphy_url = 'https://api.giphy.com/v1/gifs/search?api_key={}&q={}'.format(api_key,giphy_name)

    with urllib.request.urlopen(search_giphy_url) as url:
        search_giphy_data = url.read()
        search_giphy_response = json.loads(search_giphy_data)

        search_giphy_results = None

        if search_giphy_response['data']:
            search_giphy_list = search_giphy_response['data']
            search_giphy_results = process_results(search_giphy_list)


    return search_giphy_results


        