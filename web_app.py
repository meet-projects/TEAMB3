from flask import Flask, render_template
app = Flask(__name__)

#SQLAlchemy stuff
#from database_setup import Base Person <--- Import your tables here!!
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#engine = create_engine('sqlite:///crudlab.db')
#Base.metadata.create.all(engine) 
#DBSession = sessionmaker(bind=engine)
#session = DBSession()
#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main():
	return render_template('main_page.html')

@app.route('/profile')
def view_profile():
	return render_template('view_profile.html')

@app.route('/edit')
def edit_profile():
	return render_template('edit_profile.html')

@app.route('/login')
def login_page():
	return render_template('login_page.html')

@app.route('/delete')
def delete_profile():
	return render_template('delete_profile.html')

if __name__ == '__main__':
    app.run(debug=True)
