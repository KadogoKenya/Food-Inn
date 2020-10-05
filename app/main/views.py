from flask import render_template,request,redirect,url_for,about
from . import main
from ..request import get_giphys,get_giphy,search_giphy
from ..models import Giphy
# from flask_login import login_required
from flask_login import login_user,logout_user,login_required


# Viewsout
@main.route('/')
def homepage():
    return render_template('homepage.html')

@main.route('/index')
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

@main.route('/giphy/<int:url>')
def giphy(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    giphy = get_giphy(url)
    title = f'{giphy.title}'

    return render_template('giphy.html',title = title,giphy = giphy)

@main.route('/search/<search_name>')
def search(giphy_name):
    '''
    View function to display the search results
    '''
    giphy_name_list = giphy_name.split(" ")
    giphy_name_format = "+".join(movie_name_list)
    searched_giphys = search_giphy(giphy_name_format)
    title = f'search results for {giphy_name}'
    return render_template('search.html', giphys = searched_giphys)


@main.route('/comment/<int:id>', methods = ['GET','POST'])
@login_required
def comment(role_id):
    form = CommentForm()
    role = Role.query.get(role_id)
    all_comments = Comment.query.filter_by(role_id = role_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        role_id = role_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', role_id = role_id))
    return render_template('comment.html', form =form, role = role,all_comments=all_comments)
