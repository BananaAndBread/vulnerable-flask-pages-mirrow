import os
from urllib.parse import urljoin

from flask import Flask, render_template, request, flash, send_file, make_response
from db.db import close_connection, query_db, init_db
from wtforms import TextField
from flask import redirect
from flask_wtf import Form

# Init Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'


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
    

@app.route('/task4',  methods=['GET', 'POST'])
def task4():
    def urljoin_fallback(base, suffix):
        if "http" not in suffix:
            return urljoin('http://' + base, suffix)
        else:
            return suffix
    class RegistrationForm(Form):
        first_name = TextField('Nickname')
        password = TextField('Password')
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.password.data
        next = request.form["next"]
        next = urljoin_fallback(request.host, next)
        print(next)
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"

        else:
            if next == "http://xoxoxoyougothacked.com" or next == "https://xoxoxoyougothacked.com" or next == "http://www.xoxoxoyougothacked.com":
                next = urljoin_fallback(request.host, "/task4/UumduaZUtS")

                return redirect(next)

            return redirect(next)

    return render_template('task4/login.html', form=form, message=error)

@app.route('/task4/news')
def news():
    return render_template('task4/news.html')

@app.route('/task4/UumduaZUtS')
def flag():
    return 'flag{UumduaZUtS}'

@app.route('/task5')
def task5():
    image_name = request.args.get('image_name')
    print(image_name)
    if not image_name:
        return redirect("task5?image_name=static/yoda.png")
    return send_file(os.path.join(os.getcwd(), image_name))


@app.route('/task6', methods=['GET', 'POST'])
def task6():
    if request.method == 'GET':
        return render_template('task6.html')
    
    command = request.form.get('cmd') + ' kids_folder/linux_for_kids/' \
        + request.form.get('arg')
    command = command.replace('.', '')
    answer = os.popen(command).read()[:50]
    return render_template('task6.html', answer=answer)


@app.route('/task7')
def task7():
    link = request.args.get('link')
    if not link:
        link = ''
        return render_template('task7.html', link=link)
    else:
        resp = make_response(render_template('task7.html', link=link))
        resp.set_cookie('flag', '{84d_9uy}')
        return resp 



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
