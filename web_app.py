from flask import Flask, render_template
app = Flask(__name__)

#SQLAlchemy stuff

from database_setup import Base, User #<--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()

#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main():
	return render_template('main_page.html')

@app.route('/profile/<int:user_id>')
def view_profile(user_id):
	person = session.query(User).filter_by(id=user_id).first()
	return render_template('view_profile.html', person = person)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
	person = session.query(User).filter_by(id=user_id).first()
	if request.method == 'GET':
		return render_template('edit_profile.html', person = person)
	else:
        	# read form data
        	new_firstname = request.form['firstname']
        	new_lastname = request.form['lastname']
        	new_username = request.form['username']
        	new_password = request.form['password']
		new_bio = request.form['bio']

        	# MISSING CODE HERE FOR UPDATING THE USER
		new_person = session.query(User).filter_by(id = user_id).first()
		person.first_name = new_firstname
		person.last_name = new_lastname
		person.username = new_username
		person.password = new_password
		person.bio = new_bio

        	# redirect user to the page that views the user's new profile
        	return redirect(url_for('view_profile'))

#fix login page after everything is done
@app.route('/login', methods=['GET', 'POST'])
def login_page():
	if request.method == 'GET':
		return render_template('login_page.html')
	else:
		

@app.route('/delete')
def delete_profile():
	return render_template('delete_profile.html')

if __name__ == '__main__':
    app.run(debug=True)





