from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aaldb.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(50))

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_user = User(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            email=request.form['email'],
            role=request.form['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('add-user.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()

