from flask import Flask, render_template, request

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
    


@app.route('/task3', methods=['GET', 'POST'])
def task3():
    ''' HTTP Parameter Tempering '''
    if request.method == 'GET':
        return render_template('task3.html')

    price = request.form.get('price')
    if price and price != '99.99':
        return 'You are good! Your flag'
    else:
        return 'Thank you for purchase'
    

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
    app.run(debug=True)
