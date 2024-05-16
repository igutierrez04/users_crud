from flask import Flask, render_template, redirect, request

from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/create_user", methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.create_user(data)
    return redirect('/all_users')

@app.route('/all_users')
def all_users():
    #call the geet all classmethod to get all users
    users = User.get_all_users()
    return render_template('users.html', users = users)




if __name__=="__main__":
    app.run(debug=True)