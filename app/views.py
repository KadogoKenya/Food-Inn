from flask import render_template,request
from app import app
from .request import get_giphys,get_giphy

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to Giphy online'
    
    giphy=get_giphys()


    return render_template('index.html', title=title, giphys=giphy)

@app.route('/giphy/<int:url>')
def giphy(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    giphy = get_giphy(url)
    title = f'{giphy.title}'

    return render_template('giphy.html',title = title,giphy = giphy)