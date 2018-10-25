from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("homee.html")
@app.route('/shop')
def shop_page():
    items = ["bags", "shoes", "stuff"] 

    return render_template("shop.html", items=items)


if __name__ == '__main__':
   app.run(debug = True)