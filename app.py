from flask import Flask, render_template

app = Flask(__name__)

# ◕_◕ довойте нумеровать странички согласно их
# номеру в том списке с типами уязвимостей ◕_◕

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1')
def task1():
    return render_template('task1.html')


@app.route('/task2')
def task2():
    return render_template('task1.html')


@app.route('/task3')
def task3():
    return render_template('task1.html')


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
