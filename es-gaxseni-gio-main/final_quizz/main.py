from flask import Flask, redirect, url_for, render_template, request, session, flash
import json
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
app = Flask(__name__)
app.config['SECRET_KEY'] ='Gio-Tazo'




@app.route('/')
def home():
    return render_template('index.html')




@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('login.html')


@app.route('/user', methods=["GET"])
def user():
    url = "https://horoskopi.ge/"
    conn = request.get(url)
    content = conn.text
    soup = BeautifulSoup(content, "html.parser")

    all_horoskopeBlock = soup.find('div', {'class': 'center'})
    all_horoskope = all_horoskopeBlock.find_all('div', class_="horoscope_box")

    for each in all_horoskope:
        name = each.find("div", class_="horoscope_box_title_text left").text
        date = each.find("div", class_="text_right").text
        photo = each.find("svg", class_="horoscope_image icon1")
        print(name, date)
        
    return render_template('user.html')



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/logout')
def logout():
    session.pop('username', render_template('login.html'))
    return render_template('login.html')


@app.route('/weather')
def weather():
    key = 'c3f4a1234628a0e9f356eb5a43648a89'
    city = 'Tbilisi'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c3f4a1234628a0e9f356eb5a43648a89'
    r = request.get(url).json()
    # weather = {
    #     'city': city,
    #     'temperature': r['main']['temp'],
    #     'description' : r['weather']['description'],
    #     'icon' : r['weather']['0']['3'],
    # }
    # print(weather)
    # print(r)
    return render_template('weather.html')


# @app.route('/horoskope')
# def horoskope():
#     return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)