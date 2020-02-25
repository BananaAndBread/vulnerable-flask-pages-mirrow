from flask import Flask, render_template, request, flash
from db.db import close_connection, query_db, init_db


# Init Flask application
app = Flask(__name__)

# ◕_◕ довойте нумеровать странички согласно их
# номеру в том списке с типами уязвимостей ◕_◕

# Давайте не надо, так как палевно, люди просто
# на миде будут знать, какой это тип

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1')
def task1():
    return render_template('task1.html')


@app.route('/task2', methods=['GET', 'POST'])
def task2():
    ''' SQL injection '''
    if request.method == 'GET':
        return render_template('task2.html')

    # Get the username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')

    # Try to login with username and password
    query = f"SELECT * FROM users WHERE name='{username}' AND 1 != 1"
    res = query_db(query)

    # Return flag if user in the DB
    if len(res) > 0:
        flash('YOUR FLAG FLAG{shitshitshit}')
    else:
        flash('Wrong username or password. Please try again')

    return render_template('task2.html')


@app.route('/task3', methods=['GET', 'POST'])
def task3():
    ''' HTTP Parameter Tempering '''
    if request.method == 'GET':
        return render_template('task3.html')

    # Get price from the form and generate response
    price = request.form.get('price')
    response = f'Thank you for purchase! The cost is <b>{price}$</b>.' 

    # If the price is less than original add flag to the response
    if price and float(price) < 99.99:
        response = response + 'Your flag flag{S051Je84}'

    return response
    

@app.route('/task4')
def task4():
    return render_template('task1.html')


@app.route('/task5')
def task5():
    return render_template('task1.html')


@app.route('/task6')
def task6():
    return render_template('task1.html')


@app.route('/task7')
def task7():
    return render_template('task1.html')


@app.route('/task8')
def task8():
    return render_template('task1.html')


if __name__ == '__main__':
    # Secret key and session type specification
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    # Necessary for db. It close db after each requests dead
    app.teardown_appcontext(close_connection)

    # Init DB
    init_db()

    app.run(debug=True)
