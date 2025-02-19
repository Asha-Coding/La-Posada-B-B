from flask import Flask, render_template, url_for

app = Flask(__name__)

app.secret_key = "Y3cFAcSbRi"

@app.route("/")
def home_page():
   return render_template("page.html")

@app.route("/about")
def about_page():
   return render_template("about.html")

@app.route("/services")
def services_page():
   return render_template("services.html")

@app.route("/news")
def news_page():
   return render_template("news.html")

@app.route("/contact")
def contact_page():
   return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(error):
   return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)
