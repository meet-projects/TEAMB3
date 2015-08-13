from flask import Flask, render_template, request, redirect, url_for
from flask import session as web_session
app = Flask(__name__)

app.secret_key = 'TEAMB3'
#SQLAlchemy stuff
from database_setup import Base, User, Interests #<--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/profile/<int:user_id>')
def view_profile(user_id):
    inter = session.query(Interests).filter_by(id = user_id).first()
    person = session.query(User).filter_by(id = user_id).first()
    return render_template('view_profile.html', person = person, inter = inter)

@app.route('/signup', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:   
        new_firstname = request.form['firstname']
        new_lastname = request.form['lastname']
        new_username = request.form['username']
        new_password = request.form['password']
        new_bio = request.form['bio']
        new_background = request.form['background']
        person = User(first_name = new_firstname, last_name = new_lastname, username = new_username, password = new_password, bio = new_bio, background = new_background)
        
        new_book = request.form['fav_book']
        new_movie = request.form['fav_movie']
        new_hobby = request.form['fav_hobby']
        new_song = request.form['fav_song']
        new_other = request.form['other']
        inter = Interests(fav_book = new_book, fav_movie = new_movie, fav_hobby = new_hobby, fav_song = new_song, other = new_other)

        session.add(person)
        session.add(inter)
        session.commit()

        return redirect(url_for('view_profile', user_id = person.id))

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    inter = session.query(Interests).filter_by(id = user_id).first()
    person = session.query(User).filter_by(id=user_id).first()
    if request.method == 'GET':
        return render_template('edit_profile.html', person = person)
    else:
        new_username = request.form['username']
        new_password = request.form['password']
        new_bio = request.form['bio']
        new_background = request.form['background']

        person.username = new_username
        person.password = new_password
        person.bio = new_bio
        person.background = new_background

        new_book = request.form['fav_book']
        new_movie = request.form['fav_movie']
        new_hobby = request.form['fav_hobby']
        new_song = request.form['fav_song']
        new_other = request.form['other']
        inter.fav_book = new_book
        inter.fav_movie = new_movie
        inter.fav_hobby = new_hobby
        inter.fav_song = new_song
        inter.other = new_other

        session.commit()

        return redirect(url_for('view_profile', user_id = person.id))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'GET':
        return render_template('login_page.html')
    else:
        web_session['username'] = request.form['username']
        person = session.query(User).filter_by(username = request.form['username']).first()
        if person == None:
            error = 'User does not exist'
            return render_template('login_page.html', error = error)
        else:
            return redirect(url_for('view_profile', user_id = person.id))
        

@app.route('/delete/<int:user_id>', methods = ['GET', 'POST'])
def delete_profile(user_id):
    inter = session.query(Interests).filter_by(id = user_id).first()
    person = session.query(User).filter_by(id = user_id).first()
    if request.method == 'POST':    
        session.delete(person)
        session.delete(inter)
        session.commit()
        return redirect(url_for('main_page'))
    else:
        return render_template('delete_profile.html', person = person)


if __name__ == '__main__':
    app.run(debug=True)





