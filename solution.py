from flask import *

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/loop')
def loop():
    return render_template('loop.html', title='queue')


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<list>')
def list_prof(list):
    profs = [
        'инженер-исследователь',
        'пилот',
        'строитель',
        'экзобиолог',
        'врач',
        'инженер по терраформированию',
        'климатолог',
        'специалист по радиационной защите',
        'астрогеолог',
        'гляциолог',
        'инженер жизнеобеспечения',
        'метеоролог',
        'оператор марсохода',
        'киберинженер',
        'штурман',
        'пилот дронов',
    ]
    return render_template('list_prof.html', list=list, profs=profs)


"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)"""



if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')