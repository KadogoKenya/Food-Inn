from flask import render_template,request,redirect,url_for
from app import app
from .request import get_giphys,get_giphy,search_giphy

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to Giphy online'
    
    giphy=get_giphys()


    # return render_template('index.html', title=title, giphys=giphy)
    search_giphy = request.args.get('giphy_query')

    if search_giphy:
        return redirect(url_for('search',giphy_name=search_giphy))
    else:
        return render_template('index.html', title = title, giphys=giphy)

@app.route('/giphy/<int:url>')
def giphy(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    giphy = get_giphy(url)
    title = f'{giphy.title}'

    return render_template('giphy.html',title = title,giphy = giphy)

@app.route('/search/<movie_name>')
def search(giphy_name):
    '''
    View function to display the search results
    '''
    giphy_name_list = giphy_name.split(" ")
    giphy_name_format = "+".join(movie_name_list)
    searched_giphys = search_movie(giphy_name_format)
    title = f'search results for {giphy_name}'
    return render_template('search.html', giphys = searched_giphys)


# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting giphys
#     giphy=get_giphys()

#     title = 'Home - Welcome to The giphy zone'

#     search_giphy = request.args.get('giphy_query')

#     if search_giphy:
#         return redirect(url_for('search',giphy_name=search_giphy))
#     else:
#         return render_template('index.html', title = title, giphys=giphy)