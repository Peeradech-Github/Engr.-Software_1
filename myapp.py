from flask import Flask
from flask import render_template
from form import TopCities

# uncomment line below once you have created the
# TopCities class inside the form.py file


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/')
def home():
    name = 'Peeradech'
    top_cities = [
    'Paris',
    'London',
    'Rome',
    'Tahiti']
    title = 'TopCities'
    Form = TopCities()
    return render_template('home.html',name = name,top_cities=top_cities,title=title,form=Form)
    # top1=top_cities[0],top2=top_cities[1],
    # top3=top_cities[2],top4=top_cities[3]
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5555,debug = True)
