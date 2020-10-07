from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_giphys,get_giphy,search_giphy
from ..models import Giphy,User
# from flask_login import login_required
from flask_login import login_user,logout_user,login_required
from .forms import UpdateProfile
from .. import db,photos
from flask import flash
import cloudinary
import cloudinary.uploader
import cloudinary.api




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
    giphy_name_format = "+".join(giphy_name_list)
    searched_giphys = search_giphy(giphy_name_format)
    title = f'search results for {giphy_name}'
    return render_template('search.html', giphys = searched_giphys)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename=request.files['photo']
        upload=cloudinary.uploader.upload(filename) 
        path = upload.get('url')
        user.profile_pic_path=path
        db.session.commit()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    # return render_template('profile/update.html',form =form)