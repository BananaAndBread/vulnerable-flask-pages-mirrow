from flask import Flask, render_template

app = Flask(__name__)

# ◕_◕ довойте нумеровать странички согласно их
# номеру в том списке с типами уязвимостей ◕_◕

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1')
def page1():
    return render_template('task1.html')


if __name__ == '__main__':
    app.run(debug=True)
