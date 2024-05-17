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
    #call the get all classmethod to get all users
    users = User.get_all_users()
    return render_template('users.html', users = users)

@app.route('/edit/user/<int:user_id>')
def edit(user_id):
    data = {
        "id": id
    }
    return render_template('/edit.html', user = User.get_one(user_id))

@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/user/<int:user_id>')

@app.route('/delete/user/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/all_users')

@app.route('/user/<int:user_id>')
def one_user(user_id):
    user = User.get_one(user_id)
    return render_template('view.html', user = user)




if __name__=="__main__":
    app.run(debug=True)