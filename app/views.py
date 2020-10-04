from flask import render_template
from app import app
from .request import get_foods

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to Food-Inn online based meals'
    
    foodNutrients=get_foods()

    print(foodNutrients)

    return render_template('index.html', title=title, foodNutrients=foodNutrients)