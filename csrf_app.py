from flask import Flask, make_response, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

is_deleted = False


@app.route('/accounts/delete', methods=['GET', 'POST'])
def american_bank():
    global is_deleted

    if request.cookies.get('sne_csrftoken') == '1337':
        is_deleted = True

    if request.method == 'GET' and \
            (is_deleted or request.cookies.get('sne_csrftoken') == '1337'):
        flag = 'flag{SNE_TASK1_ABCDEFG_1234}'

        return make_response(f'''
            <html>Here you go, kiddo {flag}</html>
        ''')

    return make_response('Forbidden, you are not logged in'), 403


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
