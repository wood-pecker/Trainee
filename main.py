# TODO: ask about path to users.json
# TODO: is response code required


from flask import Flask, render_template, request, Response, url_for
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        data = request.json
        login = data['login']
        password = data['password']

        with open('C:/Users/Egor Grozny/PycharmProjects/Trainee/users.json') as db:
            users = json.load(db)

        if login in users and users[login] == password:
            print('OK')
            return Response(status=200)
        return Response(status=401)
    else:
        return "Через браузер не можно. Можно через client.py. Хотя GET-запрос обработан"


@app.route('/user/<user>')
def username(user):
    return f"Hello, {user}. Nice to meet you!"


@app.route('/usage/<int:usage>')
def userage(usage):
    if usage >= 18:
        return "You're welcome!"
    return "This page is not for minors"


if __name__ == '__main__':
    app.run(debug=True)
